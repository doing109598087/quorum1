from rotation_continuous_m_closure_property.is_rotation_continuous_m_closure_property import \
    is_rotation_continuous_m_closure_property
import time
import random
import copy
import matplotlib.pyplot as plt
import pandas as pd
from numba import njit, jit  # for 加速運算

from same_function import sort_quorum_system_by_len


@njit  # for 加速
def create_one_crt_quorum(p, N):
    return [i for i in range(N) if i % p == 0]


def create_crt_c_arbiter_quorum_system(list_of_p):
    N = 1  # 初始化
    for p in list_of_p:
        N *= p
    return [list(set(create_one_crt_quorum(list_of_p[0], N) + create_one_crt_quorum(list_of_p[i], N))) for i in
            range(1, len(list_of_p))]


def add_number_to_one_quorum(quorum, N, num):
    q2 = copy.deepcopy(quorum)
    # 如果此quorum原本就比num大->直接return(不加隨機數)
    if len(quorum) >= num:
        return quorum
    # 如果此quorum比num小->加隨機數
    while len(q2) < num:
        a = random.randint(0, N - 1)
        if a not in q2:
            q2.append(a)
    q2.sort()
    return q2


def add_number_to_all_quorum(quorum_system, N, final_k):
    abc = list()
    for quorum in quorum_system:
        abc.append(add_number_to_one_quorum(quorum, N, final_k))
    return abc
    # return [add_number_to_one_quorum(quorum, N, final_k) for quorum in quorum_system]


def create_all_crt_uniform_quorum_system(crt_c_quorum_system, N):
    crt_c_quorum_system = sort_quorum_system_by_len(crt_c_quorum_system)
    start = len(crt_c_quorum_system[0])  # 改
    end = N + 1  # 改
    # crt_all_crt_uniform_quorum_system = list()
    # for i in range(start, end):
    #     crt_uniform_quorum_system = add_number_to_all_quorum(crt_c_quorum_system, N, i)
    #     crt_all_crt_uniform_quorum_system.append(crt_uniform_quorum_system)
    # return crt_all_crt_uniform_quorum_system
    return [add_number_to_all_quorum(crt_c_quorum_system, N, i) for i in range(start, end)]


start_time = time.time()

p1 = 2
p2 = 3
p3 = 5
p4 = 7
N = p1 * p2 * p3 * p4
crt_c_arbiter_quorum_system = create_crt_c_arbiter_quorum_system([p1, p2, p3, p4])
print(crt_c_arbiter_quorum_system)

crt_all_crt_uniform_quorum_system = create_all_crt_uniform_quorum_system(crt_c_arbiter_quorum_system, N)

# is_rotation_continuous_m_closure_property

for i in range(len(crt_all_crt_uniform_quorum_system)):
    print(len(crt_all_crt_uniform_quorum_system[i][0]), ":")
    print(crt_all_crt_uniform_quorum_system[i])
    is_rotation_m, average_intersection = is_rotation_continuous_m_closure_property(
        crt_all_crt_uniform_quorum_system[i], N)

# print(is_rotation_m, ', average_intersection:', average_intersection)
# average_intersection_list.append(average_intersection)

# draw
# print(average_intersection_list)
# plt.plot([x for x in range(start, end)], average_intersection_list)
# plt.xlabel('each quorum number')
# plt.ylabel('average_intersection')
# plt.show()
# plt.savefig('crt_2357_uniform.png')
#
# # 表格
# df = pd.DataFrame(average_intersection_list, [x for x in range(start, end)])
# print(df)
# df.to_csv('crt_2357_uniform.csv', index=False)
#
# end_time = time.time()
# print("--- %s seconds ---" % (end_time - start_time))
