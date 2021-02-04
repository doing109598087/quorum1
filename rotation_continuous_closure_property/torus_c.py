import numpy as np
from random import choice
from rotation_continuous_closure_property.is_rotation_continuous_closure_property import \
    is_rotation_continuous_closure_property


# create torus 矩陣
def create_one_continuous_torus_quorum(n_temp, t_temp, w_temp, column):
    n = n_temp  # 16
    t = t_temp  # 2
    w = w_temp  # 8
    tail_number = int(w / 2) + 1  # 元素個數
    nd_array = (np.arange(n)).reshape(t, w)

    # 初始化torus_quorum
    torus_quorum = list()

    # 取兩排
    nd_0 = nd_array[:, column]
    nd_1 = nd_array[:, column + 1]
    torus_quorum = list(nd_0) + list(nd_1)

    # 隨機取一排的後面
    n_list = [n for n in range(n)] + [n for n in range(n)]
    choiced_num = int(choice(nd_1))
    torus_quorum += n_list[choiced_num + 1:choiced_num + tail_number + 1]

    torus_quorum.sort()

    return [int(num) for num in torus_quorum]  # int32 to int64


N = 24
C = list()
torus_quorum1 = create_one_continuous_torus_quorum(24, 3, 8, 0)
torus_quorum2 = create_one_continuous_torus_quorum(24, 3, 8, 5)
print(torus_quorum1)
C.append(torus_quorum1)
C.append(torus_quorum2)

print(is_rotation_continuous_closure_property(C, N))
