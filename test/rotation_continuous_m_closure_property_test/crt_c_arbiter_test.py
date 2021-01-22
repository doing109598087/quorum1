import unittest
from rotation_continuous_m_closure_property.crt_c_arbiter import create_crt_c_arbiter_quorum_system, create_one_crt_quorum


class Test_continuous_overlap(unittest.TestCase):
    def test_create_crt_c_arbiter_quorum_system(self):
        self.assertEqual(create_crt_c_arbiter_quorum_system([2, 3, 5, 7]), 210)


