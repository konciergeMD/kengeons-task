import unittest
from src.main import solution
import pytest


class TestMain(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(5, solution([1, 3, 6, 4, 1, 2]))
        self.assertEqual(4, solution([1, 2, 3]))
        self.assertEqual(1, solution([-1, -3]))
