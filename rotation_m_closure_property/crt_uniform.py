import time
from rotation_m_closure_property.is_rotation_m_closure_property import is_rotation_m_closure_property
import random
import matplotlib.pyplot as plt
import copy
import pandas as pd


def create_one_crt_quorum(p, N):
    p_list = list()
    for i in range(N):
        if i % p == 0:
            p_list.append(i)
    return p_list


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


def add_number_to_one_quorum(quorum, N, num):
    q2 = copy.deepcopy(quorum)
    # 如果此quorum原本就比num大->直接return(不加隨機數)
    if len(quorum) >= num:
        return quorum
    # 如果此quorum比num小->加隨機數
    while len(q2) < num:
        a = random.randint(0, N-1)
        if a not in q2:
            q2.append(a)
    q2.sort()
    return q2

# 下面的版本可使每次從上一輪的況狀再加入隨機數
# def add_number_to_one_quorum(quorum, N, total_time):
#     if len(quorum) >= total_time:
#         return quorum
#     while len(quorum) < total_time:
#         a = random.randint(0, N)
#         if a not in quorum:
#             quorum.append(a)
#     quorum.sort()
#     return quorum


def add_number_to_all_quorum(quorum_system, N, final_k):
    crt_uniform_quorum_system = list()
    for quorum in quorum_system:
        crt_uniform_quorum_system.append(add_number_to_one_quorum(quorum, N, final_k))
    return crt_uniform_quorum_system


p1 = 4
p2 = 3
p3 = 5
# 4, 5, 9 ok
# 2, 3, 5 ok
# 3, 4, 5 ok

# p4 = 7
N = p1 * p2 * p3
pm_list = [p1, p2, p3]

start_time = time.time()

crt_quorum_system = create_all_crt_quorum(pm_list, N)
print(crt_quorum_system)

# add uniform_k_arbiter
average_intersection_list = list()
for i in range(N+1):
    print(i, ":")
    crt_uniform_quorum_system = add_number_to_all_quorum(crt_quorum_system, N, i)
    print(crt_uniform_quorum_system)
    is_rotation_m, average_intersection = is_rotation_m_closure_property(crt_uniform_quorum_system, N)
    print(is_rotation_m, ', average_intersection:', average_intersection)
    average_intersection_list.append(average_intersection)
    print('percentage intersection: ', average_intersection/N)


# draw
print(average_intersection_list)
plt.plot([x for x in range(N+1)], average_intersection_list)
plt.xlabel('each quorum number')
plt.ylabel('average_intersection')
plt.show()

# 表格
df = pd.DataFrame(average_intersection_list, [x for x in range(N+1)])
print(df)


end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
