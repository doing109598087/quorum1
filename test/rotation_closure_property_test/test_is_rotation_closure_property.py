import unittest
from rotation_closure_property.is_rotation_closure_property import get_two_quorum_intersection, \
    is_and_get_quorum_system_intersection, compute_one_rotation_average_intersection


class Test_intersection(unittest.TestCase):
    def test_get_two_quorum_intersection(self):
        self.assertEqual({0}, get_two_quorum_intersection([0], [0]))
        self.assertEqual({0}, get_two_quorum_intersection([0, 1], [0]))
        self.assertEqual({0, 1}, get_two_quorum_intersection([0, 1], [0, 1]))

    def test_is_and_get_quorum_system_intersection(self):
        self.assertTrue(is_and_get_quorum_system_intersection([[0, 1], [0]])[0])
        self.assertEqual([{0}], is_and_get_quorum_system_intersection([[0, 1], [0]])[1])
        self.assertEqual([{0}, {0}, {0}], is_and_get_quorum_system_intersection([[0, 1], [0], [0]])[1])
        self.assertEqual([{0}, {0, 2}, {0}], is_and_get_quorum_system_intersection([[0, 1, 2], [0], [0, 2]])[1])

    def test_compute_one_rotation_average_intersection(self):
        self.assertEqual(1.5, compute_one_rotation_average_intersection([{0, 1}, {0}]))
        self.assertEqual(2, compute_one_rotation_average_intersection([{0, 1}, {0}, {0, 1, 2}]))

    # def test_get_average_intersection_count(self):
        # self.assertEqual()


