import numpy as np
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


# 改N可以改grid方陣
def create_grid_quorum(N, row, column):
    N = 25
    matrix_np = (np.arange(N)).reshape(int(np.sqrt(N)), int(np.sqrt(N)))  # 建立二維矩陣
    return list(set(list(matrix_np[row, :]) + list(matrix_np[:, column])))


print(create_grid_quorum(25, 0, 0))

# 驗證all grid quorum
# N = 25
# matrix_np = (np.arange(N)).reshape(int(np.sqrt(N)), int(np.sqrt(N)))  # 建立二維矩陣
# print(matrix_np)
# grid_matrix_total = list()

# # 建立所有grid quorum(一行一列 = 1grid_quorum)
# for i in range(int(np.sqrt(N))):
#     for j in range(int(np.sqrt(N))):
#         one_c_r_list = list(set(matrix_np[:, i].tolist() + matrix_np[j, :].tolist()))  # set: 移除重複
#         # print(one_c_r_list)
#         grid_matrix_total.append(one_c_r_list)
# # print('grid_matrix_total: ', grid_matrix_total, len(grid_matrix_total))
#
# # 兩grid_quorum做is_rotation_closure
# for i in range(N):
#     for j in range(N):
#         grid_system = list()
#         grid_system.append(grid_matrix_total[i])
#         grid_system.append(grid_matrix_total[j])
#         print(grid_matrix_total[i], grid_matrix_total[j])
#         print(is_rotation_closure_property(grid_system, N))
