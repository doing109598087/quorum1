from same_function import create_all_product_of_all_rotation_of_all_quorom, \
    compute_one_rotation_average_intersection
from numba import jit
import numpy as np
from itertools import combinations


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


def get_intersection_of_all_quorum(quorum_system):
    q_intersection = list(set(quorum_system[0]) & set(quorum_system[1]))
    for i in range(len(quorum_system)):
        q_intersection = list(set(q_intersection) & set(quorum_system[i]))
    return q_intersection


def get_one_of_two_quorum_continuous_intersection(quorum1, quorum2, N, start_num):
    q3 = list(set(quorum1) & set(quorum2))
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


def get_all_of_two_quorum_continuous_intersection(quorum1, quorum2, N):
    q3 = list(set(quorum1) & set(quorum2))
    all_continuous_intersection = list()
    index = 0
    while index != len(q3):
        start_num = q3[index]
        one_intersction = get_one_of_two_quorum_continuous_intersection(quorum1, quorum2, N, start_num)
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

    return all_continuous_intersection


if __name__ == '__main__':
    N = 24
    C = [[0, 8, 16, 1, 9, 17, 2, 3, 4, 5, 6], [2, 10, 18, 3, 11, 19, 12, 13, 14, 15, 16]]
    print(is_rotation_continuous_closure_property(C, N))
