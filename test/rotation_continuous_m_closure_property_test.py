import unittest
from rotation_continuous_m_closure_property.is_rotation_continuous_m_closure_property import \
    get_two_quorum_continuous_overlap, get_all_quorum_continuous_overlap


class Test_continuous_overlap(unittest.TestCase):
    def test_get_two_quorum_continuous_overlap(self):
        self.assertEqual(get_two_quorum_continuous_overlap([0, 1, 2], [1, 2]), [[1, 2]])
        self.assertEqual(get_two_quorum_continuous_overlap([0, 1, 2], [0, 1, 2]), [[0, 1], [1, 2]])
        self.assertEqual(get_two_quorum_continuous_overlap([0, 1, 2, 4, 6, 7, 8], [0, 1, 2, 7, 8]),
                         [[0, 1], [1, 2], [7, 8]])

    def test_get_all_quorum_continuous_overlap(self):
        self.assertEqual(get_all_quorum_continuous_overlap([[0, 1], [0, 1], [0, 1]]), [[0, 1]])
        self.assertEqual(get_all_quorum_continuous_overlap([[0, 1, 2], [0, 1, 2], [0, 1]]), [[0, 1]])
        self.assertEqual(get_all_quorum_continuous_overlap([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1]]), [[0, 1]])
        self.assertEqual(get_all_quorum_continuous_overlap([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2]]), [[0, 1], [1, 2]])
        self.assertEqual(get_all_quorum_continuous_overlap([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2], [1, 2]]),
                         [[1, 2]])
