# clustered_head_quorum: 從grid矩陣中取 one column + torus 尾巴
# clustered_member_quorum: 從grid矩陣中每一個column取一個數字

import numpy as np
from random import choice
import math
from math import floor
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


# create torus 矩陣
def create_one_grid_torus_clustered_head_quorum(N, t, w, column):
    # t = w = int(math.sqrt(N))
    tail_number = int(floor(w / 2))  # 元素個數
    nd_array = np.arange(N).reshape(t, w)
    print(nd_array)
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


def create_one_grid_torus_clustered_member_quorum(t, w):
    matrix_np = (np.arange(N)).reshape(int(np.sqrt(t)), int(np.sqrt(w)))  # 建立二維矩陣
    # print(matrix_np)
    return [choice(list(matrix_np[:, i])) for i in range(matrix_np.shape[1])]


# print(create_one_grid_torus_clustered_head_quorum(9, 0))
# print(create_one_grid_torus_clustered_head_quorum(9, 1))
# print(create_one_grid_torus_clustered_member_quorum(25))

N = 36
torus_bi_coteries_quorum_system = list()
grid_torus_clustered_head_quorum1 = create_one_grid_torus_clustered_head_quorum(N, 12, 3, 1)
grid_torus_clustered_head_quorum1 = list(grid_torus_clustered_head_quorum1)
# grid_torus_clustered_head_quorum1.sort()
grid_torus_clustered_head_quorum2 = create_one_grid_torus_clustered_head_quorum(N, 12, 3, 0)
grid_torus_clustered_head_quorum2 = list(grid_torus_clustered_head_quorum2)
# grid_torus_clustered_head_quorum2.sort()
# grid_torus_clustered_member_quorum = create_one_grid_torus_clustered_member_quorum(3, 12)
torus_bi_coteries_quorum_system.append(grid_torus_clustered_head_quorum1)
torus_bi_coteries_quorum_system.append(grid_torus_clustered_head_quorum2)
# torus_bi_coteries_quorum_system.append(grid_torus_clustered_member_quorum)

print(torus_bi_coteries_quorum_system)
# print(is_rotation_closure_property(torus_bi_coteries_quorum_system, N))
