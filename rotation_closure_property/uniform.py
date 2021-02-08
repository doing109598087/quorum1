from random import sample
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


def create_uniform_k_arbiter_quorum_system(N, quorum_size):
    U = [i for i in range(N)]
    return sample(U, quorum_size)


# test 多次
true_count = 0
for i in range(100):
    N = 10
    quorum_size = N // 2 + 1
    # quorum_size = N // 2 + 1 - 1

    q1 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
    q2 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
    q3 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
    # q4 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
    uniform_quorum = list()
    uniform_quorum.append(q1)
    uniform_quorum.append(q2)
    uniform_quorum.append(q3)
    # uniform_quorum.append(q4)
    if is_rotation_closure_property(uniform_quorum, N) == True:
        true_count += 1
print(true_count)
