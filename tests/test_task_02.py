#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 04 task 02."""


# Import Python libs
import unittest
import mock


class Lesson04Task02TestCase(unittest.TestCase):
    """
    Test cases for lesson 04 task 02.

    """

    def test_weekend(self):
        """
        Tests that it will snooze when expected to do so.

        Several test cases, spelings, times, and parameters will be tested for
        expected behavior.
        """
        test_cases = [
                ['Sunday', '0700', True],
                ['Sun', '0700', True],
                ['sUnDay', '0700', True],
                ['Monday', '0500', True],
                ['Monday', '2300', False],
        ]

        msg = 'Expected SNOOZE to be {2}. (Day: {0}, Time: {1})'
        for case in test_cases:
            with mock.patch('__builtin__.raw_input', side_effect=case[:2]):
                try:
                    task_02 = reload(task_02)
                except NameError:
                    import task_02

            self.assertIs(task_02.SNOOZE, case[2], msg.format(*case))


if __name__ == '__main__':
    unittest.main()
