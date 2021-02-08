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
        quorum3 = set(quorum1).intersection(quorum2)
        quorum_system = list()
        quorum_system.append(quorum1)
        quorum_system.append(quorum2)
        quorum_system.append(quorum3)
        if is_rotation_closure_property(quorum_system, N) == True:
            true_count += 1
        else:
            break

    return true_count


start_time = time.time()
test_time = 10000
for N in range(1, 30):
    min_size = int(math.floor(2 * N / (2 + 1)) + 1)
    # min_size = int(N // 2 + 1)
    for quorum_size in range(min_size, N):
        true_count = test_times(N, quorum_size, test_time)
        if true_count == test_time:
            print(N, quorum_size, true_count)
            break
end_time = time.time()
print('time: ', end_time - start_time)
