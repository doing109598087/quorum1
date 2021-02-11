from random import sample
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property
import time
import math


def create_uniform_k_arbiter_quorum_system(N, quorum_size):
    U = [i for i in range(N)]
    return sample(U, quorum_size)


def test_times(N, quorum_size, test_time):
    true_count = 0
    for i in range(test_time):
        quorum1 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
        quorum2 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
        quorum3 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
        quorum1.sort()
        quorum2.sort()
        quorum3.sort()
        # quorum4 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
        qm1 = set(quorum1).intersection(quorum2)
        # qm2 = set(quorum1).intersection(quorum4)
        quorum_system = list()
        # quorum_system.append(quorum1)
        # quorum_system.append(quorum2)
        quorum_system.append(quorum3)
        # quorum_system.append(quorum4)
        quorum_system.append(qm1)
        # quorum_system.append(qm2)
        # print(quorum_system)

        if is_rotation_closure_property(quorum_system, N) == True:
            true_count += 1
        else:
            break

    return true_count


start_time = time.time()
test_time = 1000
N = 25
k = 2
quorum_size = int(math.floor(k * N / (k + 1)) + 1)
true_count = test_times(N, quorum_size, test_time)
print(true_count)

end_time = time.time()
print('time: ', end_time - start_time)
