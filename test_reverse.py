#!/usr/bin/python3

import dataclasses
import glob
import io
import unittest

import reverse


class TestReverseText(unittest.TestCase):

    def test_reverse_text(self):
        for name in glob.glob('test_data/*'):
            if not name.endswith('.reversed'):
                with (
                    open(name, 'r', encoding='utf-8') as file,
                    open(f'{name}.reversed', 'r', encoding='utf-8') as r,
                    self.subTest(name=name),
                ):
                    result = r.read()
                    self.assertEqual(''.join(reverse._reverse_text(file)), result)


class TestReverseFile(unittest.TestCase):

    def test_reverse_file(self):
        for name in glob.glob('test_data/*'):
            for size in [10, 25, 50, 100, 1024, 1024 * 1024]:
                if not name.endswith('.reversed'):
                    with (
                        open(name, 'rb') as file,
                        open(f'{name}.reversed', 'r', encoding='utf-8') as r,
                        self.subTest(name=name, size=size),
                    ):
                        result = r.read()
                        self.assertEqual(''.join(reverse._reverse_file(file, size)), result)


if __name__ == '__main__':
    unittest.main()
