from unittest import TestCase
from nodes.filters import smallest


class Test(TestCase):
    def test_smallest(self):
        self.assertEqual(smallest([1, 2]), 1)
