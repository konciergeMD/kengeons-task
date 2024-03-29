import unittest
from src.main import solution
import pytest


class TestMain(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(5, solution([1, 3, 6, 4, 1, 2]))
        self.assertEqual(4, solution([1, 2, 3]))
        self.assertEqual(2, solution([-2, -1, 1]))
        self.assertEqual(1, solution([-2, -1, 4]))
        self.assertEqual(1, solution([-2, -1, 0, 4]))
        self.assertEqual(1, solution([-1, -3]))

    @pytest.mark.timeout(6)
    def test_big_numbers(self):
        f = open("tests/list.txt", "r")
        big_array = f.readline()
        f.close()
        self.assertEqual(50997, solution(eval(big_array)))

    @pytest.mark.timeout(6)
    def test_big_array(self):
        f = open("tests/list_from_1.txt", "r")
        big_array = f.readline()
        f.close()
        self.assertEqual(100000, solution(eval(big_array)))

