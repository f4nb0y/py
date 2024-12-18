#!/usr/bin/python3

import dataclasses
import unittest

import reverse


class TestReverseText(unittest.TestCase):

    def test_reverse_text(self):
        @dataclasses.dataclass
        class Data:
            arg: str
            result: bool

        data = [
            Data(None, False),
            Data('', False),
            Data('0', True),
            Data('1', True),
            Data('False', True),
            Data('True', True),
            Data('Any non-empty string', True),
        ]

        for d in data:
            with self.subTest(**dataclasses.asdict(d)):
                self.assertEqual(reverse.reverse_text(d.arg), d.result)


class TestReverseFile(unittest.TestCase):

    def test_reverse_file(self):
        @dataclasses.dataclass
        class Data:
            arg: str
            result: bool

        data = [
            Data(None, False),
            Data('', False),
            Data('0', True),
            Data('1', True),
            Data('False', True),
            Data('True', True),
            Data('Any non-empty string', True),
        ]

        for d in data:
            with self.subTest(**dataclasses.asdict(d)):
                self.assertEqual(reverse.reverse_file(d.arg), d.result)


if __name__ == '__main__':
    unittest.main()
