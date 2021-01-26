from itertools import product
import numpy as np

from numba import njit, jit


@njit  # for 加速
def create_one_quorum_rotation(quorum, N):
    return [[(n + i) % N for n in quorum] for i in range(N)]


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
    return [i for i in range(N) if i % p == 0]


# find two quorum intersection
# non continuous
def get_two_quorum_intersection(quorum1, quorum2):
    return set(quorum1).intersection(quorum2)


# continuous
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
