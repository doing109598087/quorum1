import numpy as np
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property
import pandas as pd

# 改N可以改grid方陣
def create_grid_quorum(N, row, column):
    matrix_np = (np.arange(N)).reshape(int(np.sqrt(N)), int(np.sqrt(N)))  # 建立二維矩陣
    # print(matrix_np)
    return list(set(list(matrix_np[row, :]) + list(matrix_np[:, column])))


# 驗證all grid quorum
N_list = list()
save_power_list = list()
average_intersection_list = list()
save_power_multiply_average_intersection_list = list()
for sqrt_N in range(1, 11):
    N = pow(sqrt_N, 2)
    grid_quorum1 = create_grid_quorum(N, 0, 0)
    grid_quorum2 = create_grid_quorum(N, sqrt_N - 1, sqrt_N - 1)
    grid_quorum_system = list()
    grid_quorum_system.append(grid_quorum1)
    grid_quorum_system.append(grid_quorum2)
    is_rotation, average_intersection = is_rotation_closure_property(grid_quorum_system, N)

    # for file
    N_list.append(N)
    save_power_list.append((N - len(grid_quorum1)) / N)
    average_intersection_list.append(average_intersection / N)
    save_power_multiply_average_intersection_list.append(((N - len(grid_quorum1)) / N) * (average_intersection / N))

print(N_list)
print(save_power_list)
print(average_intersection_list)
print(save_power_multiply_average_intersection_list)

df = pd.DataFrame({
    'N': N_list,
    'save_power': save_power_list,
    'average_intersection': average_intersection_list,
    'save_power_*_average_intersection': save_power_multiply_average_intersection_list,
})
df.to_csv('grid_save_power_average_intersection.csv', index=False)

