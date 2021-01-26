from same_function import create_all_product_of_all_rotation_of_all_quorom, get_two_quorum_continuous_intersection
from numba import jit
import numpy as np
from itertools import combinations


def get_all_quorum_continuous_intersection(quorum_system, N):
    all_two_quorum_intersection = list()
    len_of_quorums = len(quorum_system)
    comb = list(combinations([n for n in range(len_of_quorums)], 2))
    count = 0
    for com in comb:
        intersection = get_two_quorum_continuous_intersection(quorum_system[com[0]], quorum_system[com[1]], N)
        all_two_quorum_intersection.append(intersection)
        if len(intersection) != 0:
            count += 1
    if count == len(comb):
        return True, all_two_quorum_intersection
    return False, all_two_quorum_intersection


def compute_one_rotation_average_intersection(all_two_quorum_intersection):
    count = 0
    for two_quorum_intersection in all_two_quorum_intersection:
        count += len(two_quorum_intersection)
    return count / len(all_two_quorum_intersection)


def is_rotation_continuous_closure_property(quorum_system, N):
    all_product_of_all_rotation_of_all_quorum_list = create_all_product_of_all_rotation_of_all_quorom(quorum_system, N)
    total = len(all_product_of_all_rotation_of_all_quorum_list)
    intersection_count = 0
    len_of_quorum = len(quorum_system)
    all_average_list = list()
    for i in range(pow(N, len_of_quorum)):
        print(all_product_of_all_rotation_of_all_quorum_list[i], end='')
        is_intersection = get_all_quorum_continuous_intersection(all_product_of_all_rotation_of_all_quorum_list[i], N)[
            0]
        intersection = get_all_quorum_continuous_intersection(all_product_of_all_rotation_of_all_quorum_list[i], N)[1]
        print(intersection, end='')
        one_rotation_average_intersection = compute_one_rotation_average_intersection(intersection)
        all_average_list.append(one_rotation_average_intersection)
        print(one_rotation_average_intersection)
        if is_intersection:
            intersection_count += 1
    print('total 組合:', total)
    print('average_intersection: ', np.average(all_average_list))
    print('average_intersection_count', intersection_count / total)  # 有交集的時間飄移組合 / 所有時間飄移組合
    if intersection_count == pow(N, len_of_quorum):
        return True
    return False


if __name__ == '__main__':
    N = 24
    C = [[0, 8, 16, 1, 9, 17, 2, 3, 4, 5, 6], [2, 10, 18, 3, 11, 19, 12, 13, 14, 15, 16]]
    print(is_rotation_continuous_closure_property(C, N))
