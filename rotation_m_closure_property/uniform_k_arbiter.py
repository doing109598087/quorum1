from rotation_m_closure_property.is_rotation_m_closure_property import is_rotation_m_closure_property
from random import sample

N = 9
k = 2
U = [i for i in range(N)]
Q = int(k*N/(k+1)+1)


true_count = 0
for i in range(100):  # test 100次
    uniform_2_arbiter_quorum_system = list()
    for i in range(k+1):
        temp_list = sample(U, Q)
        uniform_2_arbiter_quorum_system.append(temp_list)
    print(is_rotation_m_closure_property(uniform_2_arbiter_quorum_system, N))
    if is_rotation_m_closure_property(uniform_2_arbiter_quorum_system, N):
        true_count += 1
print(true_count)
