#!/usr/bin/python3

import dataclasses
from typing import Any
import unittest


def example(arg: Any) -> bool:
    return bool(arg)


class TestExample(unittest.TestCase):

    def test_example(self):
        @dataclasses.dataclass
        class Data:
            arg: Any
            result: bool

        data = [
            Data(0, False),
            Data(1, True),
            Data('', False),
            Data('0', True),
            Data('1', True),
            Data('False', True),
            Data('True', True),
            Data('Any string', True),
            Data([], False),
            Data([False], True),
            Data({}, False),
            Data({0: False}, True),
        ]

        for d in data:
            with self.subTest(**dataclasses.asdict(d)):
                self.assertEqual(example(d.arg), d.result)


if __name__ == '__main__':
    unittest.main()
