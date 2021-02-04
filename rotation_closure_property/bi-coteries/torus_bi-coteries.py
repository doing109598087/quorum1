# clustered_head_quorum:從grid矩陣中取 one column + torus 尾巴
# clustered_member_quorum: 從grid矩陣中每一個column取一個數字

import numpy as np
from random import choice
import math
from math import floor
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


# create torus 矩陣
def create_one_grid_torus_clustered_head_quorum(N, column):
    t = w = int(math.sqrt(N))
    tail_number = int(floor(w / 2))  # 元素個數
    nd_array = np.arange(N).reshape(t, w)
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


def create_one_grid_torus_clustered_member_quorum(N):
    matrix_np = (np.arange(N)).reshape(int(np.sqrt(N)), int(np.sqrt(N)))  # 建立二維矩陣
    # print(matrix_np)
    return [choice(list(matrix_np[:, i])) for i in range(matrix_np.shape[1])]


# print(create_one_grid_torus_clustered_head_quorum(9, 0))
# print(create_one_grid_torus_clustered_head_quorum(9, 1))
# print(create_one_grid_torus_clustered_member_quorum(25))

N = 25
grid_torus_clustered_member_quorum = create_one_grid_torus_clustered_member_quorum(N)
grid_torus_clustered_head_quorum = create_one_grid_torus_clustered_head_quorum(N, 1)

torus_bi_coteries_quorum_system = [grid_torus_clustered_member_quorum, grid_torus_clustered_head_quorum]
print(is_rotation_closure_property(torus_bi_coteries_quorum_system, N))
