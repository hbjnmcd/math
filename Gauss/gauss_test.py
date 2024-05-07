import unittest
import numpy as np
from gauss import Gauss


class TestGauss(unittest.TestCase):
    # тесты для первого примера
    def test_classical(self):
        exam_1 = Gauss((np.array([[3, 5, -7, 9, 10], [1, -1, 1, -2, -1], [2, 2, 2, 2, 8], [15, -5, -5, -4, 1]],
                                 dtype=float), 4))
        self.assertEqual(exam_1.classical(), [1, 1, 1, 1])

    def test_optimal(self):
        exam_1 = Gauss((np.array([[3, 5, -7, 9, 10], [1, -1, 1, -2, -1], [2, 2, 2, 2, 8], [15, -5, -5, -4, 1]],
                                 dtype=float), 4))
        self.assertEqual(exam_1.optimal(), [1, 1, 1, 1])

    def test_jordan(self):
        exam_1 = Gauss((np.array([[3, 5, -7, 9, 10], [1, -1, 1, -2, -1], [2, 2, 2, 2, 8], [15, -5, -5, -4, 1]],
                                 dtype=float), 4))
        self.assertEqual(exam_1.jordan(), [1, 1, 1, 1])

    # тесты для второго примера
    def test_classical_2(self):
        exam_2 = Gauss((np.array([[5, 7, 6, 5, 23], [7, 10, 8, 7, 32], [6, 8, 10, 9, 33], [5, 7, 9, 10, 31]],
                                 dtype=float), 4))
        self.assertEqual(exam_2.classical(), [1, 1, 1, 1])

    def test_optimal_2(self):
        exam_2 = Gauss((np.array([[5, 7, 6, 5, 23], [7, 10, 8, 7, 32], [6, 8, 10, 9, 33], [5, 7, 9, 10, 31]],
                                 dtype=float), 4))
        self.assertEqual(exam_2.optimal(), [1, 1, 1, 1])

    def test_jordan_2(self):
        exam_2 = Gauss((np.array([[5, 7, 6, 5, 23], [7, 10, 8, 7, 32], [6, 8, 10, 9, 33], [5, 7, 9, 10, 31]],
                                 dtype=float), 4))
        self.assertEqual(exam_2.jordan(), [1, 1, 1, 1])
