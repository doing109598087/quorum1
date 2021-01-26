import unittest
from rotation_continuous_closure_property.torus_c import create_one_continuous_torus_quorum
import numpy as np


class Test_create_continuous_torus_quorum(unittest.TestCase):
    def test_get_two_quorum_continuous_intersection(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 8, 9, 16, 17], create_one_continuous_torus_quorum(24, 3, 8, 0))
        self.assertEqual([0, 2, 3, 10, 11, 18, 19, 20, 21, 22, 23], create_one_continuous_torus_quorum(24, 3, 8, 2))
        self.assertEqual([5, 6, 7, 8, 9, 10, 11, 13, 14, 21, 22], create_one_continuous_torus_quorum(24, 3, 8, 5))