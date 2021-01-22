from itertools import product, combinations
import numpy as np


def is_two_quorum_intersection(quorum1, quorum2):
    if list(set(quorum1).intersection(quorum2)) != 0:
        return True
    return False


def is_quorums_intersection(quorum_system):
    len_of_quorums = len(quorum_system)
    comb = list(combinations([n for n in range(len_of_quorums)], 2))
    count = 0
    for com in comb:
        if is_two_quorum_intersection(quorum_system[com[0]], quorum_system[com[1]]):
            count += 1
    if count == len(comb):
        return True
    return False


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


#
def is_rotation_closure(quorum_system, N):
    all_product_of_all_rotation_of_all_quorom_list = create_all_product_of_all_rotation_of_all_quorom(quorum_system, N)
    count = 0
    len_of_quorum = len(quorum_system)
    total_overlap_count = 0
    for i in range(pow(N, len_of_quorum)):
        print(all_product_of_all_rotation_of_all_quorom_list[i], end='')
        print(is_quorums_intersection(all_product_of_all_rotation_of_all_quorom_list[i]))

        if is_quorums_intersection(all_product_of_all_rotation_of_all_quorom_list[i]):
            count += 1
    if count == pow(N, len_of_quorum):
        print(count)
        return True
    return False


if __name__ == '__main__':

    N = 8
    C1 = [[0, 1, 2, 4], [3, 4, 5, 7], [0, 2, 6, 7]]
    print(is_rotation_closure(C1, N))
    # N = 16
    # C_grid = [[1, 4, 5, 6, 7, 9, 13], [14, 15, 3, 7, 11, 12, 13]]
    # print(is_rotation_closure(C_grid, N))

