import unittest
from rotation_m_closure_property.crt import create_one_crt_quorum


class test_rotation_m_intersection(unittest.TestCase):
    def test_get_two_quorum_intersection(self):
        self.assertEqual([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28], create_one_crt_quorum(2, 30))
