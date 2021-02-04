from rotation_m_closure_property.is_rotation_m_closure_property import is_rotation_m_closure_property
from random import sample
import math


def uniform_k_arbiter_quorum_system(N, k):
    U = [i for i in range(N)]
    Q = int(math.floor(k * N / (k + 1)) + 1)
    print("Q: ", Q)

    # get k+1個 quorum，每個quorum有Q個元素
    return [sample(U, Q) for _ in range(k + 1)]


N = 9  #
k = 2  # 在2+1=3個 quorum 中有共同交集

# uniform_2_arbiter_quorum_system_list = uniform_k_arbiter_quorum_system(N, k)
# print(uniform_2_arbiter_quorum_system_list)
# print(is_rotation_m_closure_property(uniform_2_arbiter_quorum_system_list, N))

# test 100次
true_count = 0
for i in range(100):
    uniform_2_arbiter_quorum_system_list = uniform_k_arbiter_quorum_system(N, k)
    # print(uniform_2_arbiter_quorum_system_list)
    # print(is_rotation_m_closure_property(uniform_2_arbiter_quorum_system_list, N))
    if is_rotation_m_closure_property(uniform_2_arbiter_quorum_system_list, N)[0]:
        true_count += 1
print(true_count)
