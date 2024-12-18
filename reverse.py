#!/usr/bin/python3

import argparse
import io
import os


def smallfile(name: str):
    with open(name, 'r', encoding='utf-8') as file:
        print(''.join(_reverse_text(file)), end='')


def largefile(name: str, size: int):
    with open(name, 'rb') as file:
        for block in _reverse_file(file, size):
            print(block, end='')


def _reverse_text(file: io.TextIOBase):
    return reversed(file.readlines())


def _reverse_file(file: io.BufferedIOBase, size: int):
    if not file.seekable():
        exit(f'{name} is not seekable - please specify a regular file')

    while block := file.read(size).decode():
        yield block


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--smallfile')
    parser.add_argument('-F', '--largefile')
    parser.add_argument('-b', '--blocksize', default=1024 * 1024, type=int)
    args = parser.parse_args()

    if args.smallfile:
        smallfile(args.smallfile)
    elif args.largefile:
        largefile(args.largefile, args.blocksize)
    else:
        exit('Please specify a file argument')
