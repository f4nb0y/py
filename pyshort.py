#!/usr/bin/python3

import argparse
import http.server
import json
import urllib.parse

from typing import List, MutableMapping

type Query = MutableMapping[str, List[str]]
type Links = MutableMapping[str, str]


_links = {
    'google': 'https://google.com',
    'py3lib': 'https://docs.python.org/3/library',
    'smh': 'https://smh.com.au',
}


class Handler(http.server.BaseHTTPRequestHandler):

    def _GET_command(self, cmd: str, query: Query, links: Links):
        match cmd:
            case 'list':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(_links, indent=2).encode())

            case 'get':
                if 'name' not in query:
                    self.send_error(
                        400,
                        explain='The "get" command requires the "name" query string',
                    )
                    return

                name = query['name'][0]
                if name not in links:
                    self.send_error(404, explain=f'No target defined for "{name}"')
                    return

                self.send_response(200)
                self.end_headers()
                self.wfile.write(str(links[name]).encode())

            case (
                'create' | 'update' | 'delete'
            ):  # XXX: Testing only - GET should not mutate state
                self._POST_command(cmd, query, links)

            case _:
                self.send_error(404, explain=f'No command defined for "{cmd}"')

    def _GET_redirect(self, name: str, text: str, links: Links):
        if name not in links:
            self.send_error(404, explain=f'No target defined for "{name}"')
            return

        target = links[name]
        if text:
            target += '/' + text
        self.send_response(301)
        self.send_header('Location', target)
        self.end_headers()

    def _POST_command(self, cmd: str, query: Query, links: Links):
        match cmd:
            case 'create':
                if 'name' not in query:
                    self.send_error(
                        400,
                        explain='The "create" command requires the "name" query string',
                    )
                    return

                if 'target' not in query:
                    self.send_error(
                        400,
                        explain='The "create" command requires the "target" query string',
                    )
                    return

                name = query['name'][0]
                target = query['target'][0]
                if name in links:
                    self.send_error(
                        403,
                        explain=f'Target defined for "{name}" - use the "update" command',
                    )
                    return

                links[name] = target
                self.send_response(200)
                self.end_headers()

            case 'update':
                if 'name' not in query:
                    self.send_error(
                        400,
                        explain='The "update" command requires the "name" query string',
                    )
                    return

                if 'target' not in query:
                    self.send_error(
                        400,
                        explain='The "update" command requires the "target" query string',
                    )
                    return

                name = query['name'][0]
                target = query['target'][0]
                links[name] = target
                self.send_response(200)
                self.end_headers()

            case 'delete':
                if 'name' not in query:
                    self.send_error(
                        400,
                        explain='The "delete" command requires the "name" query string',
                    )
                    return

                name = query['name'][0]
                if name not in links:
                    self.send_error(404, explain=f'No target defined for "{name}"')
                    return

                del links[name]
                self.send_response(200)
                self.end_headers()

            case _:
                self.send_error(404, explain=f'No command defined for "{cmd}"')

    def do_GET(self):
        chunks = self.path.split('/', maxsplit=2)
        name = chunks[1] if len(chunks) > 1 else ''
        text = chunks[2] if len(chunks) > 2 else ''

        match name:
            case '_':
                # For commands:
                #
                # - The first path component is '_'
                # - The second is the command, followed by optional parameters
                #
                # Commands:
                #
                #   GET /_/list
                #   GET /_/get?name=$name
                #
                url = urllib.parse.urlsplit(text)
                self._GET_command(
                    cmd=url.path, query=urllib.parse.parse_qs(url.query), links=_links
                )

            case _:
                # For redirections:
                #
                # - The first path component is the name
                # - Any further text is appended to the target
                #
                # Example:
                #
                #   Path: /py3lib/stdtypes.html#str.split
                #   Name: py3lib
                #   Target: https://docs.python.org/3/library
                #   Redirection: https://docs.python.org/3/library/stdtypes.html#str.split
                #
                self._GET_redirect(name=name, text=text, links=_links)

    def do_POST(self):
        chunks = self.path.split('/', maxsplit=2)
        name = chunks[1] if len(chunks) > 1 else ''
        text = chunks[2] if len(chunks) > 2 else ''

        match name:
            case '_':
                # For commands:
                #
                # - The first path component is '_'
                # - The second is the command, followed by optional parameters
                #
                # Commands:
                #
                #   POST /_/create?name=$name&target=$target
                #   POST /_/update?name=$name&target=$target
                #   POST /_/delete?name=$name
                #
                url = urllib.parse.urlsplit(text)
                self._POST_command(
                    cmd=url.path, query=urllib.parse.parse_qs(url.query), links=_links
                )

            case _:
                self.send_error(404)


def run(port: int):
    with http.server.HTTPServer(('', port), Handler) as httpd:
        httpd.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PyShort', description='Python implementation of a shortlink server'
    )
    parser.add_argument('-p', '--port', default=8888, type=int)
    args = parser.parse_args()
    run(port=args.port)
