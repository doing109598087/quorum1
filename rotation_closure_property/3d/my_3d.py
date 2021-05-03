import numpy as np
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


# 改N可以改grid方陣
# 取 斜線上的點
def create_grid_quorum(N):
    matrix_np = (np.arange(N)).reshape(int(np.power(N, 1 / 3)), int(np.power(N, 1 / 3)),
                                       int(np.power(N, 1 / 3)))  # 建立三維矩陣
    print(matrix_np)
    return [matrix_np[i, i, i] for i in range(int(np.power(N, 1 / 3)))]


N = 27
grid_3d_quorum_system = list()
create_grid_quorum(N)
grid_3d_quorum1 = [0, 1, 2]
# grid_3d_quorum2 = [0, 3, 6, 9, 12, 15, 18, 21, 24]  # ok
# grid_3d_quorum2 = [1, 4, 7, 10, 13, 16, 19, 22, 25]  # ok
grid_3d_quorum2 = [2, 5, 8, 11, 14, 17, 20, 23, 26]  # ok
# grid_3d_quorum2 = [0, 1, 2, 9, 10, 11, 18, 19, 20]  # 取前面
# grid_3d_quorum2 = create_grid_quorum(N, 2, 2)
grid_3d_quorum_system.append(grid_3d_quorum1)
grid_3d_quorum_system.append(grid_3d_quorum2)
#
print(is_rotation_closure_property(grid_3d_quorum_system, N))
