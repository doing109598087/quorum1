import numpy as np
from rotation_continuous_closure_property.is_rotation_continuous_closure_property import \
    is_rotation_continuous_closure_property


def create_one_continuous_grid_quorum(N, start_row, start_column):
    matrix_np = (np.arange(N)).reshape(int(np.sqrt(N)), int(np.sqrt(N)))  # 建立二維矩陣
    # print(matrix_np)
    if start_row == int(np.sqrt(N) - 1):
        two_row = list(matrix_np[start_row, :]) + list(matrix_np[0, :])
    else:
        two_row = matrix_np[start_row:start_row + 2, :].ravel()
    if start_column == int(np.sqrt(N) - 1):
        two_column = list(matrix_np[:, start_column]) + list(matrix_np[:, 0])
    else:
        two_column = matrix_np[:, start_column:start_column + 2].ravel()
    grid_quorum = list(set(list(two_row) + list(two_column)))
    grid_quorum.sort()
    return grid_quorum


N = 36
grid_quorum_system = list()
grid_quorum1 = create_one_continuous_grid_quorum(N, 2, 3)
grid_quorum2 = create_one_continuous_grid_quorum(N, 0, 0)
grid_quorum_system.append(grid_quorum1)
grid_quorum_system.append(grid_quorum2)
print(is_rotation_continuous_closure_property(grid_quorum_system, N))
