from itertools import product
import numpy as np

from numba import njit, jit


@njit  # for 加速
def create_one_quorum_rotation(quorum, N):
    # return [[(n + i) % N for n in quorum] for i in range(N)]
    return [sorted([(n + i) % N for n in quorum]) for i in range(N)]


def create_all_quorum_rotation(quorum_system, N):
    return [create_one_quorum_rotation(quorum_system[i], N) for i in range(len(quorum_system))]


def create_all_product_of_all_rotation_of_all_quorom(quorum_system, N):
    len_of_quorum = len(quorum_system)
    comb = list(product([n for n in range(N)], repeat=len_of_quorum))
    all_rotation_of_all_quorom = create_all_quorum_rotation(quorum_system, N)
    return [[all_rotation_of_all_quorom[i][com[i]] for i in range(len_of_quorum)] for com in comb]


# other
def sort_quorum_system_by_len(quorum_system):
    len_list = [len(quorum) for quorum in quorum_system]
    return [x for _, x in sorted(zip(len_list, quorum_system))]


def compute_one_rotation_average_intersection(all_two_quorum_intersection):
    count = 0
    for two_quorum_intersection in all_two_quorum_intersection:
        count += len(two_quorum_intersection)
    return count / len(all_two_quorum_intersection)


# crt
def create_one_crt_quorum(p, N):
    return [p * k % N for k in range(0, int(N / p - 1 + 1))]



