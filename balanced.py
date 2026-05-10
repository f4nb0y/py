#!/usr/bin/python3

import dataclasses
import unittest


def is_balanced(arg: str) -> bool:
    level = 0

    for c in arg:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1

        if level < 0:
            return False

    return level == 0


class TestIsBalanced(unittest.TestCase):

    def test_is_balanced(self):
        @dataclasses.dataclass
        class Data:
            arg: str
            result: bool

        data = [
            Data('', True),
            Data('(', False),
            Data('((', False),
            Data('()', True),
            Data('()()', True),
            Data('(())', True),
            Data(')', False),
            Data('))', False),
            Data(')(', False),
            Data(')()(', False),
            Data('))((', False),
            Data('XYZ', True),
            Data('(XYZ', False),
            Data('(XYZ)', True),
            Data('XYZ)', False),
            Data('X(Y)Z', True),
            Data('X(YZ', False),
            Data('XY)Z', False),
            Data('(X(YZ)', False),
            Data('(XY)Z)', False),
            Data('(X(Y)Z)', True),
            Data('(X)Y(Z)', True),
        ]

        for d in data:
            with self.subTest(**dataclasses.asdict(d)):
                self.assertEqual(is_balanced(d.arg), d.result)


if __name__ == '__main__':
    unittest.main()
