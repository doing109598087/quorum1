from same_function import create_all_product_of_all_rotation_of_all_quorom, \
    compute_one_rotation_average_intersection
from itertools import combinations
import numpy as np


def get_two_quorum_intersection(quorum1, quorum2):
    return set(quorum1).intersection(quorum2)


def is_and_get_quorum_system_intersection(quorum_system):
    all_two_quorum_intersection = list()
    len_of_quorums = len(quorum_system)
    comb = list(combinations([n for n in range(len_of_quorums)], 2))
    count = 0
    for com in comb:
        intersection = get_two_quorum_intersection(quorum_system[com[0]], quorum_system[com[1]])
        all_two_quorum_intersection.append(intersection)
        if len(intersection) != 0:
            count += 1
    if count == len(comb):
        return True, all_two_quorum_intersection
    return False, all_two_quorum_intersection


def is_rotation_closure_property(quorum_system, N):
    all_product_of_all_rotation_of_all_quorum_list = create_all_product_of_all_rotation_of_all_quorom(quorum_system, N)
    all_rotation_count = len(all_product_of_all_rotation_of_all_quorum_list)
    intersection_count = 0
    for i in range(all_rotation_count):
        is_intersection, intersection = is_and_get_quorum_system_intersection(all_product_of_all_rotation_of_all_quorum_list[i])
        if is_intersection:
            intersection_count += 1
    if intersection_count == all_rotation_count:
        return True
    return False


if __name__ == '__main__':
    # N = 8
    # C1 = [[0, 1, 2, 4], [3, 4, 5, 7], [0, 2, 6, 7]]
    # print(is_rotation_closure_property(C1, N))
    # N = 16
    # C_grid = [[1, 4, 5, 6, 7, 9, 13], [14, 15, 3, 7, 11, 12, 13]]
    # print(is_rotation_closure_property(C_grid, N))
    N = 10
    # C1 = [[0, 3, 6], [0, 1, 2, 4, 7]]
    # C1 = [[6, 7, 8], [0, 3, 6, 4, 7]]
    C1 = [[3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 9], [5, 9]]
    print(is_rotation_closure_property(C1, N))
