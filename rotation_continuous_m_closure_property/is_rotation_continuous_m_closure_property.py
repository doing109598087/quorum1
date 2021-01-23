from same_function import create_all_product_of_all_rotation_of_all_quorom, sort_quorum_system_by_len
import copy
import time
import numpy as np
from numba import njit, jit  # for 加速運算
import warnings

warnings.filterwarnings('ignore')


@jit(nopython=True, parallel=True)  # for 加速
def get_two_quorum_continuous_overlap(quorum1, quorum2, N):
    quorum1 = np.array(quorum1)
    quorum2 = np.array(quorum2)
    quorum1.sort()
    quorum2.sort()
    all_continuous_overlap = [[quorum1[i], quorum1[i + 1]] for i in range(len(quorum1) - 1) for j in
                              range(len(quorum2) - 1) if
                              quorum1[i] == quorum2[j] and quorum1[i + 1] == quorum2[j + 1] and quorum1[i] + 1 ==
                              quorum1[i + 1]]
    if quorum1[-1] == quorum2[-1] == N - 1 and quorum1[0] == quorum2[0] == 0:
        all_continuous_overlap.append([quorum1[-1], 0])

    return all_continuous_overlap


def get_all_quorum_continuous_overlap(quorum_system, N):
    quorum_system = sort_quorum_system_by_len(quorum_system)
    first_two_quorum_continuous_overlap = get_two_quorum_continuous_overlap(quorum_system[0], quorum_system[1], N)
    all_quorum_continuous_overlap = copy.copy(first_two_quorum_continuous_overlap)
    for i in range(len(first_two_quorum_continuous_overlap)):
        for quorum in quorum_system:
            if first_two_quorum_continuous_overlap[i][0] in quorum and first_two_quorum_continuous_overlap[i][
                1] in quorum:
                continue
            else:
                if first_two_quorum_continuous_overlap[i] in all_quorum_continuous_overlap:
                    all_quorum_continuous_overlap.remove(first_two_quorum_continuous_overlap[i])
                else:
                    continue

    return all_quorum_continuous_overlap


def is_rotation_continuous_m_closure_property(quorum_system, N):
    all_product_of_all_rotation_of_all_quorom_list = create_all_product_of_all_rotation_of_all_quorom(quorum_system, N)
    total = len(all_product_of_all_rotation_of_all_quorom_list)
    overlap_count = 0
    len_of_quorum = len(quorum_system)
    total_overlap_count = 0
    for i in range(pow(N, len_of_quorum)):
        ##########################test#################
        # if i % 1000 == 0:
        #     print(i)
        # if i == 20000:
        #     break
        ##########################test#################

        # print(all_product_of_all_rotation_of_all_quorom_list[i], end='')
        overlap_of_list = get_all_quorum_continuous_overlap(all_product_of_all_rotation_of_all_quorom_list[i], N)
        # print(overlap_of_list)
        # print(len(overlap_of_list))
        total_overlap_count += len(overlap_of_list)
        if len(overlap_of_list):
            overlap_count += 1
    average_overlap = total_overlap_count / total
    print('total 組合:', total)
    print('overlap_count: ', overlap_count)
    print('total_overlap: ', total_overlap_count)
    print('average_overlap', total_overlap_count / total)  # 總交集數 / 所有時間飄移組合
    print('average_overlap_count', overlap_count / total)  # 有交集的時間飄移組合 / 所有時間飄移組合
    if overlap_count == pow(N, len_of_quorum):
        return True, average_overlap
    return False, average_overlap


if __name__ == '__main__':
    start_time = time.time()

    N = 20
    C = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
         [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
         [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    print(is_rotation_continuous_m_closure_property(C, N))
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
