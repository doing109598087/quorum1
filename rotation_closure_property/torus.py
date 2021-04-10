import numpy as np
from random import choice
from is_rotation_closure_property import is_rotation_closure_property
import pandas as pd


# create torus 矩陣
def create_one_torus_quorum(n_temp, t_temp, w_temp, column):
    n = n_temp  # 16
    t = t_temp  # 2
    w = w_temp  # 8
    tail_number = int(w / 2)  # 元素個數
    nd_array = (np.arange(n)).reshape(t, w)
    # print(nd_array)
    test = column  # 取第test column一整個
    nd_0 = nd_array[:, test]
    for i in range(test, tail_number + test):
        if i >= w - 1:
            t = i % (w - 1)
            one_column = nd_array[:, t]
            nd_0 = np.append(nd_0, choice(one_column))
        else:
            one_column = nd_array[:, i + 1]
            nd_0 = np.append(nd_0, choice(one_column))
    return nd_0


def find_all_factor(n):
    return [i for i in range(1, n + 1) if n % i == 0]


# for file
N_list = list()
t_list = list()
save_power_list = list()
average_intersection_list = list()
save_power_multiply_average_intersection_list = list()
for N in range(0, 100):
    find_all_factor_list = find_all_factor(N)
    for i in range(len(find_all_factor_list)):
        torus_quorum1 = create_one_torus_quorum(N, find_all_factor_list[i], int(N / find_all_factor_list[i]), 0)
        torus_quorum2 = create_one_torus_quorum(N, find_all_factor_list[i], int(N / find_all_factor_list[i]),
                                                int(N / find_all_factor_list[i] / 2))
        torus_quorum_system = list()
        torus_quorum_system.append(torus_quorum1)
        torus_quorum_system.append(torus_quorum2)

        is_rotation, average_intersection = is_rotation_closure_property(torus_quorum_system, N)

        # for file
        N_list.append(N)
        t_list.append(str(find_all_factor_list[i]) + '*' + str(int(N / find_all_factor_list[i])))
        save_power_list.append((N - len(torus_quorum1)) / N)
        average_intersection_list.append(average_intersection / N)
        save_power_multiply_average_intersection_list.append(
            ((N - len(torus_quorum1)) / N) * (average_intersection / N))

df = pd.DataFrame({
    'N': N_list,
    't': t_list,
    'save_power': save_power_list,
    'average_intersection': average_intersection_list,
    'save_power_*_average_intersection': save_power_multiply_average_intersection_list,
})
df.to_csv('torus_save_power_average_intersection.csv', index=False)
