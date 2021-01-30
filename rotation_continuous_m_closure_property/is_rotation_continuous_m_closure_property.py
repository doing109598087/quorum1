from same_function import create_all_product_of_all_rotation_of_all_quorom, sort_quorum_system_by_len
import copy
import time
import numpy as np
from numba import njit, jit  # for 加速運算
import warnings

warnings.filterwarnings('ignore')


@jit(nopython=True, parallel=True)  # for 加速
def get_two_quorum_continuous_intersection(quorum1, quorum2, N):
    quorum1 = np.array(quorum1)
    quorum2 = np.array(quorum2)
    quorum1.sort()
    quorum2.sort()
    all_continuous_intersection = [[quorum1[i], quorum1[i + 1]] for i in range(len(quorum1) - 1) for j in
                                   range(len(quorum2) - 1) if
                                   quorum1[i] == quorum2[j] and quorum1[i + 1] == quorum2[j + 1] and quorum1[i] + 1 ==
                                   quorum1[i + 1]]
    if quorum1[-1] == quorum2[-1] == N - 1 and quorum1[0] == quorum2[0] == 0:
        all_continuous_intersection.append([quorum1[-1], 0])

    return all_continuous_intersection


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
    average_length_list = list()
    for i in range(pow(N, len_of_quorum)):
        ##########################test#################
        # if i % 1000 == 0:
        #     print(i)
        # if i == 20000:
        #     break
        ##########################test#################

        print(all_product_of_all_rotation_of_all_quorom_list[i], end='')
        intersection_of_list = get_all_quorum_continuous_intersection(all_product_of_all_rotation_of_all_quorom_list[i],
                                                                      N)
        intersection_of_list_length, length = get_all_of_all_quorum_continuous_intersection(
            all_product_of_all_rotation_of_all_quorom_list[i], N)
        average_length_list.append(length)

        # print(intersection_of_list)
        # print(len(intersection_of_list))
        print(intersection_of_list_length, length)
        total_intersection_count += len(intersection_of_list)
        if len(intersection_of_list):
            intersection_count += 1
    average_intersection = total_intersection_count / total
    print('total 組合:', total)
    print('intersection_count: ', intersection_count)
    print('total_intersection: ', total_intersection_count)
    print('average_intersection', total_intersection_count / total)  # 總交集數 / 所有時間飄移組合
    print('average_intersection_count', intersection_count / total)  # 有交集的時間飄移組合 / 所有時間飄移組合
    print('average_intersection_length', np.average(average_length_list))  # 有交集的時間飄移組合 / 所有時間飄移組合
    if intersection_count == pow(N, len_of_quorum):
        return True, average_intersection
    return False, average_intersection


def get_intersection_of_all_quorum(quorum_system):
    q_intersection = list(set(quorum_system[0]) & set(quorum_system[1]))
    for i in range(len(quorum_system)):
        q_intersection = list(set(q_intersection) & set(quorum_system[i]))
    return q_intersection


def get_one_of_all_quorum_continuous_intersection(quorum_system, N, start_num):
    q3 = get_intersection_of_all_quorum(quorum_system)
    temp_num = q3[q3.index(start_num)]
    continuous_intersection = list()
    continuous_intersection.append(temp_num)
    for i in range(N):
        if temp_num + 1 in q3:
            continuous_intersection.append(temp_num + 1)
            temp_num += 1
        else:
            break

    return continuous_intersection


def get_all_of_all_quorum_continuous_intersection(quorum_system, N):  # for length
    q3 = get_intersection_of_all_quorum(quorum_system)
    all_continuous_intersection = list()
    index = 0
    while index != len(q3):
        start_num = q3[index]
        one_intersction = get_one_of_all_quorum_continuous_intersection(quorum_system, N, start_num)
        if len(one_intersction) > 1:
            all_continuous_intersection.append(one_intersction)
            index += len(one_intersction)
        else:
            index += 1

    if all_continuous_intersection[0][0] == 0 and all_continuous_intersection[-1][-1] == N - 1:
        all_continuous_intersection[0] += all_continuous_intersection[-1]
        all_continuous_intersection.pop()
    elif all_continuous_intersection[0][0] == 0 and N - 1 in q3:
        all_continuous_intersection[0].append(N - 1)
    elif all_continuous_intersection[-1][-1] == N - 1 and 0 in q3:
        all_continuous_intersection[-1].append(0)
    elif N - 1 in q3 and 0 in q3:
        all_continuous_intersection.append([0, N - 1])
    else:
        pass
    length = np.average([len(one_continuous_intersection) for one_continuous_intersection in all_continuous_intersection])
    # print(length)
    return all_continuous_intersection, length


if __name__ == '__main__':
    start_time = time.time()

    N = 20
    C = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
         [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
         [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    print(is_rotation_continuous_m_closure_property(C, N))
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
