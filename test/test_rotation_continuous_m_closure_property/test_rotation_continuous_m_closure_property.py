import unittest
from rotation_continuous_m_closure_property.is_rotation_continuous_m_closure_property import \
    get_two_quorum_continuous_intersection, get_all_quorum_continuous_intersection, sort_quorum_system_by_len, \
    get_intersection_of_all_quorum, get_all_of_all_quorum_continuous_intersection


class Test_continuous_intersection(unittest.TestCase):
    def test_get_two_quorum_continuous_intersection(self):
        self.assertEqual([[1, 2]], get_two_quorum_continuous_intersection([0, 1, 2], [1, 2], 3))
        self.assertEqual([[4, 0]], get_two_quorum_continuous_intersection([0, 1, 2, 3, 4], [0, 2, 4], 5))
        self.assertEqual([[4, 0]], get_two_quorum_continuous_intersection([0, 2, 4], [0, 1, 2, 3, 4], 5))
        self.assertEqual([[4, 0]], get_two_quorum_continuous_intersection([0, 2, 4], [4, 0, 1, 2, 3], 5))
        self.assertEqual([[4, 0]], get_two_quorum_continuous_intersection([4, 0, 1, 2, 3], [0, 2, 4], 5))
        self.assertEqual([[0, 1], [1, 2], [7, 8], [8, 0]],
                         get_two_quorum_continuous_intersection([0, 1, 2, 4, 6, 7, 8], [0, 1, 2, 7, 8], 9))
        self.assertEqual([[1, 2]], get_two_quorum_continuous_intersection([0, 1, 2, 5], [1, 2, 5], 6))

    def test_get_all_quorum_continuous_intersection(self):
        self.assertEqual([[0, 1]], get_all_quorum_continuous_intersection([[0, 1, 2], [0, 1, 2], [0, 1]], 3))
        self.assertEqual([[0, 1]], get_all_quorum_continuous_intersection([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1]], 4))
        self.assertEqual([[0, 1], [1, 2]],
                         get_all_quorum_continuous_intersection([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2]], 4))
        self.assertEqual([[1, 2]],
                         get_all_quorum_continuous_intersection([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2], [1, 2]], 4))
        self.assertEqual([[0, 1], [1, 2], [2, 3], [5, 0]],
                         get_all_quorum_continuous_intersection([[0, 1, 2, 3, 5], [0, 1, 2, 3, 5]], 6))

    # todo: 6/29
    def test_sort_quorum_system_by_len(self):
        self.assertEqual([[0, 1], [0, 1, 2]], sort_quorum_system_by_len([[0, 1, 2], [0, 1]]))
        self.assertEqual([[0], [0, 1], [0, 1, 2]], sort_quorum_system_by_len([[0, 1, 2], [0, 1], [0]]))

    def test_get_intersection_of_all_quorum(self):
        self.assertEqual([0, 1, 2, 3], get_intersection_of_all_quorum([[0, 1, 2, 3, 4], [0, 1, 2, 3]]))
        self.assertEqual([0, 3], get_intersection_of_all_quorum([[0, 1, 2, 3, 4], [0, 1, 2, 3], [0, 3, 4, 5]]))

    def test_get_one_of_all_quorum_continuous_intersection(self):
        self.assertEqual([[0, 1]],
                         get_all_of_all_quorum_continuous_intersection([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1]], 5))
        self.assertEqual([[0, 1, 2, 3], [5, 6, 7]],
                         get_all_of_all_quorum_continuous_intersection([[0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 5, 6, 7]],
                                                                       10))
        self.assertEqual([[0, 1, 2, 8, 9]],
                         get_all_of_all_quorum_continuous_intersection(
                             [[0, 1, 2, 7, 8, 9], [0, 1, 2, 7, 8, 9], [0, 1, 2, 8, 9]], 10))
        self.assertEqual([[0, 1, 2], [8, 9]],
                         get_all_of_all_quorum_continuous_intersection(
                             [[0, 1, 2, 7, 8, 9], [0, 1, 2, 7, 8, 9], [0, 1, 2, 8, 9]], 20))
        self.assertEqual([[0, 1, 2, 18, 19], [7, 8, 9]],
                         get_all_of_all_quorum_continuous_intersection(
                             [[0, 1, 2, 7, 8, 9, 18, 19], [0, 1, 2, 7, 8, 9, 18, 19], [0, 1, 2, 7, 8, 9, 18, 19]], 20))
        self.assertEqual([[0, 1, 2, 19], [7, 8, 9]],
                         get_all_of_all_quorum_continuous_intersection(
                             [[0, 1, 2, 7, 8, 9, 19], [0, 1, 2, 7, 8, 9, 19], [0, 1, 2, 7, 8, 9, 19]], 20))
        self.assertEqual([[7, 8, 9], [18, 19, 0]],
                         get_all_of_all_quorum_continuous_intersection(
                             [[0, 7, 8, 9, 18, 19], [0, 7, 8, 9, 18, 19], [0, 7, 8, 9, 18, 19]], 20))
        self.assertEqual([[7, 8, 9], [0, 19]],
                         get_all_of_all_quorum_continuous_intersection(
                             [[0, 7, 8, 9, 19], [0, 7, 8, 9, 19], [0, 7, 8, 9, 19]], 20))
