import numpy as np
import is_rotation

N = 16
matrix_np = (np.arange(N)+1).reshape(int(np.sqrt(N)), int(np.sqrt(N)))  # 建立二維矩陣
# print(matrix_np)
grid_matrix_total = list()

for i in range(int(np.sqrt(N))):
    for j in range(int(np.sqrt(N))):
        one_c_r_list = list(set(matrix_np[:, i].tolist() + matrix_np[j, :].tolist()))  # set: 移除重複
        # print(one_c_r_list)
        grid_matrix_total.append(one_c_r_list)
print(grid_matrix_total)

grid_system = list()
for i in range(N):
    for j in range(N):
        grid_system.append(grid_matrix_total[i])
        grid_system.append(grid_matrix_total[j])
        # print(grid_matrix_total[i], grid_matrix_total[j])
        print(is_rotation.is_rotation_closure(grid_system, N))  # 計算量太大



