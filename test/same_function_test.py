import unittest
from same_function import get_one_of_two_quorum_continuous_intersection, get_all_of_two_quorum_continuous_intersection


class Test_continuous_intersection(unittest.TestCase):
    def test_get_one_of_two_quorum_continuous_intersection(self):
        self.assertEqual([0, 1, 2], get_one_of_two_quorum_continuous_intersection([0, 1, 2], [0, 1, 2], 4, 0), )
        self.assertEqual([2, 3, 4], get_one_of_two_quorum_continuous_intersection([0, 2, 3, 4], [0, 1, 2, 3, 4], 6, 2))
        self.assertEqual([2, 3, 0], get_one_of_two_quorum_continuous_intersection([0, 2, 3], [0, 1, 2, 3], 4, 2))
        self.assertEqual([],
                         get_one_of_two_quorum_continuous_intersection([0, 1, 2, 7, 8, 9], [0, 1, 2, 7, 8, 9], 10, 0))

    def test_get_all_of_two_quorum_continuous_intersection(self):
        self.assertEqual(
            get_all_of_two_quorum_continuous_intersection([0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 5, 6, 7], 10),
            [[0, 1, 2, 3], [5, 6, 7]])
        self.assertEqual([[0, 1, 2, 7, 8, 9]],
                         get_all_of_two_quorum_continuous_intersection([0, 1, 2, 7, 8, 9], [0, 1, 2, 7, 8, 9], 10))
        self.assertEqual([[0, 1, 2], [7, 8, 9]],
                         get_all_of_two_quorum_continuous_intersection([0, 1, 2, 7, 8, 9], [0, 1, 2, 7, 8, 9], 20))
        self.assertEqual([[0, 1, 2, 18, 19], [7, 8, 9]],
                         get_all_of_two_quorum_continuous_intersection([0, 1, 2, 7, 8, 9, 18, 19],
                                                                       [0, 1, 2, 7, 8, 9, 18, 19], 20))
        self.assertEqual([[0, 1, 2, 19], [7, 8, 9]],
                         get_all_of_two_quorum_continuous_intersection([0, 1, 2, 7, 8, 9, 19],
                                                                       [0, 1, 2, 7, 8, 9, 19], 20))

        self.assertEqual([[7, 8, 9], [18, 19, 0]],
                         get_all_of_two_quorum_continuous_intersection([0, 7, 8, 9, 18, 19],
                                                                       [0, 7, 8, 9, 18, 19], 20))
        self.assertEqual([[7, 8, 9], [0, 19]],
                         get_all_of_two_quorum_continuous_intersection([0, 7, 8, 9, 19],
                                                                       [0, 7, 8, 9, 19], 20))
