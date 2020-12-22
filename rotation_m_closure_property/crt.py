import time
from rotation_m_closure_property.is_rotation_m_closure_property import is_rotation_m_closure_property


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


p1 = 4
p2 = 9
p3 = 5
# p4 = 7
N = p1 * p2 * p3
pm_list = [p1, p2, p3]

start_time = time.time()

crt_qrorum_system = create_all_crt_quorum(pm_list, N)
print(crt_qrorum_system)
print(is_rotation_m_closure_property(crt_qrorum_system, N))

end_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))
