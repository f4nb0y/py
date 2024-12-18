#!/usr/bin/python3

import argparse
import io
import os


def smallfile(name: str):
    with open(name, 'r', encoding='utf-8') as file:
        reverse_text(file)


def largefile(name: str, size: int):
    with open(name, 'rb') as file:
        if not file.seekable():
            exit(f'{name} is not seekable - please specify a regular file')

        reverse_file(file, size)


def reverse_text(file: io.TextIOBase):
    print(''.join(reversed(file.readlines())), end='')


def reverse_file(file: io.BufferedIOBase, size: int):
    print(file.read().decode())


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
