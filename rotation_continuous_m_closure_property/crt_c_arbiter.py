def create_one_crt_quorum(p, N):
    p_list = list()
    for i in range(N):
        if i % p == 0:
            p_list.append(i)
    return p_list


def create_crt_c_arbiter_quorum_system(list_of_p):
    N = 1
    for p in list_of_p:
        N *= p

    crt_c_arbiter_quorum_system = list()
    p0_crt_quorum = create_one_crt_quorum(list_of_p[0], N)
    for i in range(1, len(list_of_p)):
        crt_c_arbiter_quorum = p0_crt_quorum + create_one_crt_quorum(list_of_p[i], N)
        crt_c_arbiter_quorum_system.append(crt_c_arbiter_quorum)

    return crt_c_arbiter_quorum_system


# print(create_one_crt_quorum(2, 210))

print(create_crt_c_arbiter_quorum_system([2, 3, 5, 7]))

