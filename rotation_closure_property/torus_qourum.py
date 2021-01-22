import numpy as np
import is_rotation_closure_property
from random import choice
from is_rotation_closure_property import is_rotation_closure


# create torus 矩陣


def create_one_torus_quorum(n_temp, t_temp, w_temp, column):
    n = n_temp  # 16
    t = t_temp  # 2
    w = w_temp  # 8
    tail_number = int(w / 2)  # 元素個數
    nd_array = (np.arange(n)).reshape(t, w)
    print(nd_array)

    test = column  # 取第test column一整個
    nd_0 = nd_array[:, test]
    for i in range(test, tail_number + test):
        if i >= w - 1:
            # print('i', i)
            t = i % (w-1)
            one_column = nd_array[:, t]
            nd_0 = np.append(nd_0, choice(one_column))
        else:
            one_column = nd_array[:, i + 1]
            # print(one_column)
            # print(i)
            nd_0 = np.append(nd_0, choice(one_column))
    return list(nd_0)


# print(create_one_torus_quorum(16, 2, 9, 0))
different_column_list = list()
for i in range(8):
    temp_list = create_one_torus_quorum(16, 2, 8, i)
    different_column_list.append(temp_list)
    print(temp_list)

print(is_rotation_closure(different_column_list, 16))


