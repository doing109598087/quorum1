import unittest
from rotation_m_closure_property.is_rotation_m_closure_property import get_two_quorum_overlap, \
    get_all_quorum_continuous_overlap


class test_rotation_m_overlap(unittest.TestCase):
    def test_get_two_quorum_overlap(self):
        self.assertEqual(get_two_quorum_overlap([0, 1, 2], [0]), {0})
        self.assertEqual(get_two_quorum_overlap([0, 1, 2], [0, 1]), {0, 1})

    def test_get_all_quorum_continuous_overlap(self):
        self.assertEqual(get_all_quorum_continuous_overlap([[0, 1, 2], [0]]), {0})
        self.assertEqual(get_all_quorum_continuous_overlap([[0, 1, 2], [0], [1, 2]]), set())

