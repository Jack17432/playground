from unittest import TestCase
from nodes.filters import *


class Test(TestCase):
    def test_smallest(self):
        self.assertEqual(smallest([1, 2]), 1)

    def test_largest(self):
        self.assertEqual(largest([1, 2]), 2)
