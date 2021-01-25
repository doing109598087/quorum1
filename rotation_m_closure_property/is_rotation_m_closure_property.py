from same_function import create_all_product_of_all_rotation_of_all_quorom, sort_quorum_system_by_len

from itertools import product
import numpy as np
# intersection refactor: https://www.coderbridge.com/@kuanghsuan/2b75b952ea6f402ba11a0de654077b91
from numba import njit, jit  # for 加速運算


def get_two_quorum_intersection(quorum1, quorum2):
    return set(quorum1).intersection(quorum2)


def get_all_quorum_continuous_intersection(quorum_system):
    # quorum_system = sort_quorum_system_by_len(quorum_system)
    intersection_list = get_two_quorum_intersection(quorum_system[0], quorum_system[1])
    for i in range(len(quorum_system)):
        intersection_list = get_two_quorum_intersection(intersection_list, quorum_system[i])
    return intersection_list


def is_rotation_m_closure_property(quorum_system, N):
    all_product_of_all_rotation_of_all_quorom_list = create_all_product_of_all_rotation_of_all_quorom(quorum_system, N)
    total = len(all_product_of_all_rotation_of_all_quorom_list)
    intersection_count = 0
    len_of_quorum = len(quorum_system)
    total_intersection_count = 0
    for i in range(pow(N, len_of_quorum)):
        # print(all_product_of_all_rotation_of_all_quorom_list[i], end='')
        intersection_of_list = get_all_quorum_continuous_intersection(all_product_of_all_rotation_of_all_quorom_list[i])
        # print(intersection_of_list)
        # print(len(intersection_of_list))
        total_intersection_count += len(intersection_of_list)
        if len(get_all_quorum_continuous_intersection(all_product_of_all_rotation_of_all_quorom_list[i])):
            intersection_count += 1
    average_intersection = total_intersection_count / total
    print('total 組合:', total)
    print('intersection_count: ', intersection_count)
    print('total_intersection: ', total_intersection_count)
    print('average_intersection', total_intersection_count / total)  # 總交集數 / 所有時間飄移組合
    print('average_intersection_count', intersection_count / total)  # 有交集的時間飄移組合 / 所有時間飄移組合
    if intersection_count == pow(N, len_of_quorum):
        return True, average_intersection
    return False, average_intersection


if __name__ == '__main__':
    # N = 9
    # C = [[0, 1, 2, 4, 5, 7, 8], [0, 2, 3, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6]]

    N = 30
    C = [[0, 5, 10, 15, 20, 25], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27],
         [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]]
    print(is_rotation_m_closure_property(C, N))
