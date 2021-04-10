import numpy as np
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


# 改N可以改grid方陣
def create_grid_quorum(N, t, w):
    matrix_np = (np.arange(N)).reshape(int(np.power(N, 1 / 3)), int(np.power(N, 1 / 3)),
                                       int(np.power(N, 1 / 3)))  # 建立二維矩陣
    result = list()
    print(matrix_np)
    for n in matrix_np[:, :, t]:
        result += list(n)
    for n in matrix_np[:, w, :]:
        result += list(n)

    print(set(result))
    # print(matrix_np[:, :, 0])
    # print(matrix_np[:, 0, :])
    return set(result)


N = 27
grid_3d_quorum_system = list()
grid_3d_quorum1 = create_grid_quorum(N, 0, 0)
grid_3d_quorum2 = create_grid_quorum(N, 2, 2)
grid_3d_quorum_system.append(grid_3d_quorum1)
grid_3d_quorum_system.append(grid_3d_quorum2)

print(is_rotation_closure_property(grid_3d_quorum_system, N))
