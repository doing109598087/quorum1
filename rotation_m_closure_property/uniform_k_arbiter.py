from rotation_m_closure_property.is_rotation_m_closure_property import is_rotation_m_closure_property
from random import sample


def uniform_k_arbiter_quorum_system(N, k):
    U = [i for i in range(N)]
    Q = int(k * N / (k + 1) + 1) # 加取下底
    print("Q: ", Q)
    quorum_system_list = list()
    for i in range(k + 1):
        temp_list = sample(U, Q)
        quorum_system_list.append(temp_list)
    return quorum_system_list


N = 8
k = 2
# uniform_2_arbiter_quorum_system_list = uniform_k_arbiter_quorum_system(N, k)
# print(uniform_2_arbiter_quorum_system_list)
# print(is_rotation_m_closure_property(uniform_2_arbiter_quorum_system_list, N))

true_count = 0
for i in range(100):  # test 100次
    uniform_2_arbiter_quorum_system_list = uniform_k_arbiter_quorum_system(N, k)
    print(uniform_2_arbiter_quorum_system_list)
    # print(is_rotation_m_closure_property(uniform_2_arbiter_quorum_system_list, N))
    if is_rotation_m_closure_property(uniform_2_arbiter_quorum_system_list, N):
        true_count += 1
print(true_count)
