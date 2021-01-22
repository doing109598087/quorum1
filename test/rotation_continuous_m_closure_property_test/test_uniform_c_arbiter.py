import unittest
from rotation_continuous_m_closure_property.uniform_c_arbiter import create_uniform_c_arbiter_quorum_system


class Test_uniform_C_arbiter(unittest.TestCase):
    def test_create_uniform_C_arbiter_quorum_system(self):
        self.assertEqual(create_uniform_c_arbiter_quorum_system(20, 3),
                         [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]])
