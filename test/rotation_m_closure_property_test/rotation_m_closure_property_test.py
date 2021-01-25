import unittest
from rotation_m_closure_property.is_rotation_m_closure_property import get_two_quorum_intersection, \
    get_all_quorum_continuous_intersection, c


class test_rotation_m_intersection(unittest.TestCase):
    def test_get_two_quorum_intersection(self):
        self.assertEqual(get_two_quorum_intersection([0, 1, 2], [0]), {0})
        self.assertEqual(get_two_quorum_intersection([0, 1, 2], [0, 1]), {0, 1})

    def test_get_all_quorum_continuous_intersection(self):
        self.assertEqual(get_all_quorum_continuous_intersection([[0, 1, 2], [0]]), {0})
        self.assertEqual(get_all_quorum_continuous_intersection([[0, 1, 2], [0], [1, 2]]), set())

