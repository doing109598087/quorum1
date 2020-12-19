import numpy as np
from is_rotation_closure_property import is_rotation_closure


# 改N可以改grid方陣
N = 16
matrix_np = (np.arange(N)).reshape(int(np.sqrt(N)), int(np.sqrt(N)))  # 建立二維矩陣
print(matrix_np)
grid_matrix_total = list()

# 建立所有grid quorum(一行一列 = 1grid_quorum)
for i in range(int(np.sqrt(N))):
    for j in range(int(np.sqrt(N))):
        one_c_r_list = list(set(matrix_np[:, i].tolist() + matrix_np[j, :].tolist()))  # set: 移除重複
        # print(one_c_r_list)
        grid_matrix_total.append(one_c_r_list)
# print('grid_matrix_total: ', grid_matrix_total, len(grid_matrix_total))

# 兩grid_quorum做is_rotation_closure
for i in range(N):
    for j in range(N):
        grid_system = list()
        grid_system.append(grid_matrix_total[i])
        grid_system.append(grid_matrix_total[j])
        print(grid_matrix_total[i], grid_matrix_total[j])
        print(is_rotation_closure(grid_system, N))



