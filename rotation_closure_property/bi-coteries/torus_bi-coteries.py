import numpy as np
from random import choice
import math
from math import floor


# create torus 矩陣
def create_one_grid_torus_clustered_head_quorum(n_temp, column):
    n = n_temp  # 16
    t = w = int(math.sqrt(n))
    tail_number = int(floor(w / 2))  # 元素個數
    nd_array = (np.arange(n)).reshape(t, w)
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


print(create_one_grid_torus_quorum(9, 0))
print(create_one_grid_torus_quorum(9, 1))
