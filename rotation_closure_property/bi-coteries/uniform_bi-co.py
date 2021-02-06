from random import sample
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


def create_uniform_k_arbiter_quorum_system(N, quorum_size):
    U = [i for i in range(N)]
    return sample(U, quorum_size)


def test_times(N, quorum_size, test_time):
    true_count = 0
    for i in range(1000):
        quorum1 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
        quorum2 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
        quorum3 = set(quorum1).intersection(quorum2)
        quorum_system = list()
        quorum_system.append(quorum1)
        quorum_system.append(quorum2)
        quorum_system.append(quorum3)
        if is_rotation_closure_property(quorum_system, N) == True:
            true_count += 1
    return true_count


for N in range(1, 30):
    min_size = int(N // 2 + 1)
    for quorum_size in range(min_size, N):
        true_count = test_times(N, quorum_size, 1000)
        if true_count == 1000:
            print(N, quorum_size, true_count)
            break

# N = 20
# quorum_size = 14
# true_count = test_1000(N, quorum_size)
# print(true_count)

# # test 多次
# true_count = 0
# for i in range(1000):
#     quorum1 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
#     quorum2 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
#     quorum3 = set(quorum1).intersection(quorum2)
#     quorum_system = list()
#     quorum_system.append(quorum1)
#     quorum_system.append(quorum2)
#     quorum_system.append(quorum3)
#     if is_rotation_closure_property(quorum_system, N) == True:
#         true_count += 1
# print(true_count)

# quorum1 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
# quorum2 = create_uniform_k_arbiter_quorum_system(N, quorum_size)
# print('quorum1: ', quorum1)
# print('quorum2: ', quorum2)
# quorum3 = set(quorum1).intersection(quorum2)
# print(set(quorum1).intersection(quorum2))
