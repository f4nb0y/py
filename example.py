#!/usr/bin/python3

import dataclasses
import unittest


def example(arg: str) -> bool:
    return bool(arg)


class TestExample(unittest.TestCase):

    def test_example(self):
        @dataclasses.dataclass
        class Data:
            arg: str
            result: bool

        data = [
            Data('', False),
            Data('0', True),
            Data('1', True),
            Data('False', True),
            Data('True', True),
            Data('Any non-empty string', True),
        ]

        for d in data:
            with self.subTest(**dataclasses.asdict(d)):
                self.assertEqual(example(d.arg), d.result)


if __name__ == '__main__':
    unittest.main()
