import numpy as np
from random import choice
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


def create_one_torus_3d_quorum(n, t, h, w, column):
    tail_number = int(w / 2)  # 元素個數
    nd_array = (np.arange(n)).reshape(t, h, w)
    print(nd_array)

    nd_0 = list(nd_array[:, :, column])
    nd_0 = [nd_0[i][j] for i in range(len(nd_0)) for j in range(len(nd_0[i]))]

    # print(nd_0)
    # print(choice(nd_0))

    nd_result = list()
    nd_result += nd_0

    tail_number = w // 2
    # print(tail_number)

    for i in range(column, tail_number + column):
        if i >= w - 1:
            t = i % (w - 1)
            nd_0 = list(nd_array[:, :, t])
            nd_0 = [nd_0[i][j] for i in range(len(nd_0)) for j in range(len(nd_0[i]))]
            nd_result.append(choice(nd_0))
        else:
            nd_0 = list(nd_array[:, :, i + 1])
            nd_0 = [nd_0[i][j] for i in range(len(nd_0)) for j in range(len(nd_0[i]))]
            nd_result.append(choice(nd_0))

    print(nd_result)
    return nd_result


N = 63
torus_3d_quorum1 = create_one_torus_3d_quorum(N, 3, 3, 7, 5)
torus_3d_quorum2 = create_one_torus_3d_quorum(N, 3, 3, 7, 0)
torus_quorum_system = list()
torus_quorum_system.append(torus_3d_quorum1)
torus_quorum_system.append(torus_3d_quorum2)
print(is_rotation_closure_property(torus_quorum_system, N))
