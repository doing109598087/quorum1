import time
from rotation_m_closure_property.is_rotation_m_closure_property import is_rotation_m_closure_property
import random
import matplotlib.pyplot as plt


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


def add_number_to_one_quorum(quorum, N, total_time):
    if len(quorum) > total_time:
        return quorum
    while len(quorum) < total_time:
        a = random.randint(0, N)
        if a not in quorum:
            quorum.append(a)
    quorum.sort()
    return quorum


def add_number_to_all_quorum(quorum_system, N, final_k):
    crt_uniform_quorum_system = list()
    for i in range(len(quorum_system)):
        crt_uniform_quorum_system.append(add_number_to_one_quorum(quorum_system[i], N, final_k))
    return crt_uniform_quorum_system


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

# add uniform_k_arbiter
average_overlap_list = list()
for i in range(32):
    print(i, ":")
    crt_uniform_quorum_system = add_number_to_all_quorum(crt_quorum_system, N, i)
    print(crt_uniform_quorum_system)
    is_rotation_m, average_overlap = is_rotation_m_closure_property(crt_uniform_quorum_system, N)
    print(is_rotation_m, ', average_overlap:', average_overlap)
    average_overlap_list.append(average_overlap)

# draw
print(average_overlap_list)
plt.plot([x for x in range(32)], average_overlap_list)
plt.xlabel('each quorum number')
plt.ylabel('average_overlap')
plt.show()

end_time = time.time()

print("--- %s seconds ---" % (end_time - start_time))
