#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 04 task 03."""


# Import Python libs
import unittest
import mock
import random
import decimal
import sys


class Lesson04Task03TestCase(unittest.TestCase):
    """
    Test cases for lesson 04 task 03.
    """

    def setUp(self):
        self.test_data = [
                [1, 199999, 1, 15, True, '3.63'],
                [1, 199999, 1, 15, False, '4.65'],
                [1, 199999, 16, 20, True, '4.04'],
                [1, 199999, 16, 20, False, '4.98'],
                [1, 199999, 21, 30, True, '5.77'],
                [1, 199999, 21, 30, False, '6.39'],
                [200000, 999999, 1, 15, True, '3.02'],
                [200000, 999999, 1, 15, False, '3.98'],
                [200000, 999999, 16, 20, True, '3.27'],
                [200000, 999999, 16, 20, False, '4.08'],
                [200000, 999999, 21, 30, True, '4.66'],
                [1000000, sys.maxint, 1, 15, True, '2.05'],
                [1000000, sys.maxint, 16, 20, True, '2.62'],
                [-200000, -100000, 1, 15, True, None],
                [200000, 999999, 21, 30, False, None],
                [1000000, sys.maxint, 1, 15, False, None],
                [1000000, sys.maxint, 21, 30, True, None],
                [1, 199999, 31, 40, True, None],
        ]


    def calculate_interest(self, principal, rate, yrs):
        """
        Calculates a total for interest + principal when compounded monthly.
        """
        if rate:
            dec_rt = decimal.Decimal(rate) / 100
            total = int(round(principal * ((1 + (dec_rt / 12)) ** (12 * yrs))))
        else:
            total = None

        return total


    def get_str_bool(self, value):
        """
        Returns a 1-3 character string of Yes/No for boolean values
        """
        return 'y' if value else 'n'


    def test_total(self):
        """
        Tests for the value of ``TOTAL``.

        This test tests multiple random and non-random values for each of the
        possible variations in user-input. It even tests values that *should* be
        illegal in the program.
        """
        for raw_data in self.test_data:
    
            low_data = [raw_data[0], raw_data[0], raw_data[2], raw_data[2],
                        raw_data[4], raw_data[5]]
            high_data = [raw_data[1], raw_data[1], raw_data[3], raw_data[3],
                         raw_data[4], raw_data[5]]

            for data in [low_data, raw_data, high_data]:
                principal = random.randint(data[0], data[1])
                years = random.randint(data[2], data[3])
                total = self.calculate_interest(principal, data[5], years)

                mock_input = ['Mountebank Singes', str(principal), str(years),
                              self.get_str_bool(data[4])]
                with mock.patch('__builtin__.raw_input',
                                side_effect=mock_input):
                    try:
                        task_03 = reload(task_03)
                    except NameError:
                        import task_03
                    self.assertEqual(total, task_03.TOTAL)


if __name__ == '__main__':
    unittest.main()
