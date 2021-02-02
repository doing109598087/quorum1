from rotation_continuous_m_closure_property.is_rotation_continuous_m_closure_property import \
    is_rotation_continuous_m_closure_property
import time


# from same_function import create_one_crt_quorum


def create_one_crt_quorum(p, N):
    return [i for i in range(N) if i % p == 0]


def create_crt_c_arbiter_quorum_system(prime_number_list):
    N = 1
    for p in prime_number_list:
        N *= p
    return [set(create_one_crt_quorum(prime_number_list[0], N) + create_one_crt_quorum(prime_number_list[i], N)) for i in
            range(1, len(prime_number_list))]


start_time = time.time()

p1 = 2
p2 = 3
p3 = 5
p4 = 7
N = p1 * p2 * p3 * p4
crt_c_arbiter_quorum_system = create_crt_c_arbiter_quorum_system([p1, p2, p3, p4])
print(crt_c_arbiter_quorum_system)
# print(is_rotation_continuous_m_closure_property(crt_c_arbiter_quorum_system, N))

end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
