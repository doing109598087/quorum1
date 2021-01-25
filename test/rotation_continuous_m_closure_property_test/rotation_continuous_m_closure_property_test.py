import unittest
from rotation_continuous_m_closure_property.is_rotation_continuous_m_closure_property import \
    get_two_quorum_continuous_intersection, get_all_quorum_continuous_intersection, sort_quorum_system_by_len


class Test_continuous_intersection(unittest.TestCase):
    def test_get_two_quorum_continuous_intersection(self):
        self.assertEqual(get_two_quorum_continuous_intersection([0, 1, 2], [1, 2], 3), [[1, 2]])
        self.assertEqual(get_two_quorum_continuous_intersection([0, 1, 2, 3, 4], [0, 2, 4], 5), [[4, 0]])
        self.assertEqual(get_two_quorum_continuous_intersection([0, 2, 4], [0, 1, 2, 3, 4], 5), [[4, 0]])
        self.assertEqual(get_two_quorum_continuous_intersection([0, 2, 4], [4, 0, 1, 2, 3], 5), [[4, 0]])
        self.assertEqual(get_two_quorum_continuous_intersection([4, 0, 1, 2, 3], [0, 2, 4], 5), [[4, 0]])
        self.assertEqual(get_two_quorum_continuous_intersection([0, 1, 2, 4, 6, 7, 8], [0, 1, 2, 7, 8], 9),
                         [[0, 1], [1, 2], [7, 8], [8, 0]])
        self.assertEqual(get_two_quorum_continuous_intersection([0, 1, 2, 5], [1, 2, 5], 6), [[1, 2]])

    def test_get_all_quorum_continuous_intersection(self):
        self.assertEqual(get_all_quorum_continuous_intersection([[0, 1, 2], [0, 1, 2], [0, 1]], 3), [[0, 1]])
        self.assertEqual(get_all_quorum_continuous_intersection([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1]], 4), [[0, 1]])
        self.assertEqual(get_all_quorum_continuous_intersection([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2]], 4),
                         [[0, 1], [1, 2]])
        self.assertEqual(get_all_quorum_continuous_intersection([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2], [1, 2]], 4),
                         [[1, 2]])
        self.assertEqual(get_all_quorum_continuous_intersection([[0, 1, 2, 3, 5], [0, 1, 2, 3, 5]], 6),
                         [[0, 1], [1, 2], [2, 3], [5, 0]])

    def test_sort_quorum_system_by_len(self):
        self.assertEqual(sort_quorum_system_by_len([[0, 1, 2], [0, 1]]), [[0, 1], [0, 1, 2]])
        self.assertEqual(sort_quorum_system_by_len([[0, 1, 2], [0, 1], [0]]), [[0], [0, 1], [0, 1, 2]])
