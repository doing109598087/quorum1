from itertools import product, combinations
import numpy as np


def create_one_quorom_rotation(quorum, N):
    all_rotation_of_one_quorom = np.zeros([N, len(quorum)])
    for i in range(N):
        all_rotation_of_one_quorom[i] = np.array([(n + i) % N for n in quorum])
    return all_rotation_of_one_quorom


def create_all_quorom_rotation(quorum_system, N):
    all_rotation_of_all_quorom = np.zeros(len(quorum_system))
    # for i in range(len(quorum_system)):
    #     # print(create_one_quorom_rotation(quorum_system[i], N))
    #     all_rotation_of_all_quorom[i] = create_one_quorom_rotation(quorum_system[i], N)
    return all_rotation_of_all_quorom


if __name__ == '__main__':
    N = 8
    C1 = [[0, 1, 2, 4], [3, 4, 5, 7], [0, 2, 6, 7]]

    # N = 16
    # C_grid = [[1, 4, 5, 6, 7, 9, 13], [14, 15, 3, 7, 11, 12, 13]]
    print(create_all_quorom_rotation(C1, N))
