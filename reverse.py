#!/usr/bin/python3

import argparse
import os


def smallfile(name: str):
    with open(name, 'r', encoding='utf-8') as f:
        print(''.join(reversed(f.readlines())), end='')


def largefile(name: str, size: int):
    with open(name, 'rb') as f:
        if not f.seekable():
            exit(f'{name} is not seekable - please specify a regular file')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--smallfile')
    parser.add_argument('-F', '--largefile')
    parser.add_argument('-b', '--blocksize', default=1024, type=int)
    args = parser.parse_args()

    if args.smallfile:
        smallfile(args.smallfile)
    elif args.largefile:
        largefile(args.largefile, args.blocksize)
    else:
        exit('Please specify a file argument')
