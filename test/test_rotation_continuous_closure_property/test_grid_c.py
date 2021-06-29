import unittest
from rotation_continuous_closure_property.c_grid import create_one_continuous_grid_quorum


class Test_create_continuous_grid_quorum(unittest.TestCase):
    def test_create_one_continuous_grid_quorum(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 19, 24, 25, 30, 31],
                         create_one_continuous_grid_quorum(36, 0, 0))
        self.assertEqual([3, 4, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 27, 28, 33, 34],
                         create_one_continuous_grid_quorum(36, 2, 3))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 18, 19, 24, 25, 30, 31, 32, 33, 34, 35],
                         create_one_continuous_grid_quorum(36, 5, 0))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 11, 12, 17, 18, 23, 24, 29, 30, 31, 32, 33, 34, 35],
                         create_one_continuous_grid_quorum(36, 5, 5))
