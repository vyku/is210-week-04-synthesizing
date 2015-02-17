#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 04 task 01."""


# Import Python libs
import unittest
import mock
import random


class Lesson04Task01TestCase(unittest.TestCase):
    """
    Test cases for lesson 04 task 01.

    """

    def test_color_choices(self):
        """
        Tests that the user decision tree is followed in selecting colors.

        This randomly selects colors from the color tree on each execution.
        """
        colors = {
            'Seattle Gray': {
                'Ceramic Glaze': ['Basically White', 'White'],
                'Cumulus Nimbus': ['Off-White', 'Paper White']
            },
            'Manatee': {
                'Platinum Mist': ['Bone White', 'Just White'],
                'Spartan Sage': ['Fractal White', 'Not White']
            }
        }

        for base, accents in colors.iteritems():
            for accent, highlights in accents.iteritems():
                for highlight in highlights:
                    mock_input = [base, accent, highlight]
                    with mock.patch('__builtin__.raw_input',
                            side_effect=mock_input):
                        try:
                            task_01 = reload(task_01)
                        except NameError:
                            import task_01

                        self.assertEqual(task_01.BASE, base)
                        self.assertEqual(task_01.ACCENT, accent)
                        self.assertEqual(task_01.HIGHLIGHT, highlight)


if __name__ == '__main__':
    unittest.main()
