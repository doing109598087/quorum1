def create_one_crt_quorum(p, N):
    quorum = list()
    for i in range(N):
        if i % p == 0:
            quorum.append(i)
    return quorum
    # return [i for i in range(N) if i % p == 0]


def create_all_crt_quorum(p_list, N):
    all_crt_quorum = list()
    for p in p_list:
        all_crt_quorum.append(create_one_crt_quorum(p, N))
    return all_crt_quorum
    # return [create_one_crt_quorum(p, N) for p in pm_list]
