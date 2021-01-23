from itertools import product

# overlap refactor: https://www.coderbridge.com/@kuanghsuan/2b75b952ea6f402ba11a0de654077b91
from typing import List, Any, Union


def overlap(quorum1, quorum2):
    return set(quorum1).intersection(quorum2)


def overlap_of_lists(quorums):
    intersection_list = overlap(quorums[0], quorums[1])
    for i in range(len(quorums)):
        intersection_list = overlap(intersection_list, quorums[i])
    # print('intersection_list_num', len(intersection_list))
    return intersection_list


def create_one_quorum_rotation(quorum, N):
    return [[(n + i) % N for n in quorum] for i in range(N)]


def create_all_quorum_rotation(quorum_system, N):
    return [create_one_quorum_rotation(quorum_system[i], N) for i in range(len(quorum_system))]


def create_all_product_of_all_rotation_of_all_quorom(quorum_system, N):
    len_of_quorum = len(quorum_system)
    comb = list(product([n for n in range(N)], repeat=len_of_quorum))
    all_rotation_of_all_quorom = create_all_quorum_rotation(quorum_system, N)
    all_product_of_all_rotation_of_all_quorom_list = [
        [all_rotation_of_all_quorom[i][com[i]] for i in range(len_of_quorum)] for com in comb]
    return all_product_of_all_rotation_of_all_quorom_list


def is_rotation_m_closure_property(quorum_system, N):
    all_product_of_all_rotation_of_all_quorom_list = create_all_product_of_all_rotation_of_all_quorom(quorum_system, N)
    total = len(all_product_of_all_rotation_of_all_quorom_list)
    overlap_count = 0
    len_of_quorum = len(quorum_system)
    total_overlap_count = 0
    for i in range(pow(N, len_of_quorum)):
        # print(all_product_of_all_rotation_of_all_quorom_list[i], end='')
        overlap_of_list = overlap_of_lists(all_product_of_all_rotation_of_all_quorom_list[i])
        # print(overlap_of_list)
        # print(len(overlap_of_list))
        total_overlap_count += len(overlap_of_list)
        if len(overlap_of_lists(all_product_of_all_rotation_of_all_quorom_list[i])):
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
    # N = 9
    # C = [[0, 1, 2, 4, 5, 7, 8], [0, 2, 3, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6]]

    N = 30
    C = [[0, 5, 10, 15, 20, 25], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27],
         [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]]
    print(is_rotation_m_closure_property(C, N))
