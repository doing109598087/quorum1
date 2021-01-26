from same_function import create_all_product_of_all_rotation_of_all_quorom, sort_quorum_system_by_len, \
    get_two_quorum_continuous_intersection
import copy
import time
import numpy as np
from numba import njit, jit  # for 加速運算
import warnings

warnings.filterwarnings('ignore')


def get_all_quorum_continuous_intersection(quorum_system, N):
    quorum_system = sort_quorum_system_by_len(quorum_system)
    first_two_quorum_continuous_intersection = get_two_quorum_continuous_intersection(quorum_system[0],
                                                                                      quorum_system[1], N)
    all_quorum_continuous_intersection = copy.copy(first_two_quorum_continuous_intersection)
    for i in range(len(first_two_quorum_continuous_intersection)):
        for quorum in quorum_system:
            if first_two_quorum_continuous_intersection[i][0] in quorum and first_two_quorum_continuous_intersection[i][
                1] in quorum:
                continue
            else:
                if first_two_quorum_continuous_intersection[i] in all_quorum_continuous_intersection:
                    all_quorum_continuous_intersection.remove(first_two_quorum_continuous_intersection[i])
                else:
                    continue

    return all_quorum_continuous_intersection


def is_rotation_continuous_m_closure_property(quorum_system, N):
    all_product_of_all_rotation_of_all_quorom_list = create_all_product_of_all_rotation_of_all_quorom(quorum_system, N)
    total = len(all_product_of_all_rotation_of_all_quorom_list)
    intersection_count = 0
    len_of_quorum = len(quorum_system)
    total_intersection_count = 0
    for i in range(pow(N, len_of_quorum)):
        ##########################test#################
        # if i % 1000 == 0:
        #     print(i)
        # if i == 20000:
        #     break
        ##########################test#################

        # print(all_product_of_all_rotation_of_all_quorom_list[i], end='')
        intersection_of_list = get_all_quorum_continuous_intersection(all_product_of_all_rotation_of_all_quorom_list[i],
                                                                      N)
        # print(intersection_of_list)
        # print(len(intersection_of_list))
        total_intersection_count += len(intersection_of_list)
        if len(intersection_of_list):
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
    start_time = time.time()

    N = 20
    C = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
         [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
         [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    print(is_rotation_continuous_m_closure_property(C, N))
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
