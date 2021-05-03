import numpy as np
from random import choice
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


def create_one_torus_3d_quorum(n, t, h, w, column):
    tail_number = int(w / 2)  # 元素個數
    nd_array = (np.arange(n)).reshape(t, h, w)
    print(nd_array)
    result = list()
    for i in range(7):
        temp = [num for a in nd_array[:, :, i] for num in a]
        # print(choice(temp))
        result.append(choice(temp))
    return result


# return nd_result


N = 63
t = 3
h = 3
w = 7
column = 0

torus_3d_quorum1 = create_one_torus_3d_quorum(N, t, h, w, column)
print(torus_3d_quorum1)
# torus_3d_quorum2 = [0, 7, 14, 21, 28, 35, 42, 49, 56]
# torus_3d_quorum1.sort()
# torus_3d_quorum2.sort()
# print(torus_3d_quorum1)
# print(torus_3d_quorum2)
# torus_3d_quorum_system = list()
# torus_3d_quorum_system.append(torus_3d_quorum1)
# torus_3d_quorum_system.append(torus_3d_quorum2)
# print(is_rotation_closure_property(torus_3d_quorum_system, N))
