import time
from rotation_m_closure_property.is_rotation_m_closure_property import is_rotation_m_closure_property
import random
import matplotlib.pyplot as plt
import copy
import pandas as pd
import numpy as np
from same_function import create_one_crt_quorum


def create_all_crt_quorum(pm_list, N):
    return [create_one_crt_quorum(p, N) for p in pm_list]


def is_coprime(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    if num1 == 1:
        return True
    else:
        return False


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


#
def add_number_to_one_quorum(quorum, N, num):
    q2 = copy.copy(quorum)
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
    return [add_number_to_one_quorum(quorum, N, final_k) for quorum in quorum_system]


p1 = 5
p2 = 3
p3 = 2
# 4, 5, 9 ok
# 2, 3, 5 ok
# 3, 4, 5 ok

# p4 = 7
N = p1 * p2 * p3
pm_list = [p1, p2, p3]

start_time = time.time()

crt_quorum_system = create_all_crt_quorum(pm_list, N)
print(crt_quorum_system)
crt_uniform_quorum_system = add_number_to_all_quorum(crt_quorum_system, N, 7)
print(crt_uniform_quorum_system)
crt_uniform_quorum_system = add_number_to_all_quorum(crt_quorum_system, N, 8)
print(crt_uniform_quorum_system)
crt_uniform_quorum_system = add_number_to_all_quorum(crt_quorum_system, N, 9)
print(crt_uniform_quorum_system)

# # add uniform_k_arbiter
# average_intersection_list = list()
# for i in range(N + 1):
#     print(i, ":")
#     crt_uniform_quorum_system = add_number_to_all_quorum(crt_quorum_system, N, i)
#     print(crt_uniform_quorum_system)
#     is_rotation_m, average_intersection = is_rotation_m_closure_property(crt_uniform_quorum_system, N)
#     average_intersection_list.append(average_intersection)
#
# # draw
# print(average_intersection_list)
# plt.plot([x for x in range(N + 1)], average_intersection_list)
# plt.xlabel('quorum size')
# plt.ylabel('average_intersection')
# plt.show()
#
# # 表格
# df = pd.DataFrame(average_intersection_list, [x for x in range(N + 1)])
# print(df)
#
# end_time = time.time()
# print("--- %s seconds ---" % (end_time - start_time))
