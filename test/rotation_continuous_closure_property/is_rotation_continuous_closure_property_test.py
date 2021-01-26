import unittest
from rotation_continuous_closure_property.is_rotation_continuous_closure_property import \
    get_two_quorum_continuous_intersection, get_all_quorum_continuous_intersection


class Test_continuous_intersection(unittest.TestCase):
    def test_get_two_quorum_continuous_intersection(self):
        self.assertEqual(get_two_quorum_continuous_intersection([0, 1, 2], [0, 1], 3), [[0, 1]])

    def test_get_all_quorum_continuous_intersection(self):
        self.assertEqual(get_all_quorum_continuous_intersection([[0, 1, 2], [0, 1]], 3)[1], [[[0, 1]]])
        self.assertEqual(get_all_quorum_continuous_intersection([[0, 1, 2], [0, 1], [0, 1]], 3)[1], [[[0, 1]], [[0, 1]], [[0, 1]]])

