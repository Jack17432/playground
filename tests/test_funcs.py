from unittest import TestCase
from funcs import *


class basic_fun_test(TestCase):
    def test_adding(self):
        self.assertEqual(adding(1, 2), 3)

    def test_adding_more(self):
        self.assertNotEqual(adding(2, 2), 3)

    def test_minusing(self):
        self.assertEqual(minusing(2, 1), 1)

    def test_timzing(self):
        self.assertEqual(timzing(2, 2), 4)
