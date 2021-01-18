import numpy as np


def create_one_quorum_rotation(quorum, N):
    # return [[(n + i) % N for n in quorum] for i in range(N)]
    one_rotation_array = np.zeros([N, len(quorum)])
    for i in range(N):
        one_rotation_array[i] = np.array([(n + i) % N for n in quorum])  # np化
    return one_rotation_array


def create_all_quorum_rotation(quorum_system, N):
    return np.array([create_one_quorum_rotation(quorum_system[i], N) for i in range(len(quorum_system))])

def create_all_product_of_all_rotation_of_all_quorom(quorum_system, N):
    

N = 9
C2 = [[0, 1, 2, 4, 5, 7, 8], [0, 2, 3, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6]]
C2 = np.array(C2)
# N = 30
# C = [[0, 5, 10, 15, 20, 25], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27],
#      [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]]
print(create_all_quorum_rotation(C2, N))
