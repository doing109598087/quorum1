from rotation_continuous_m_closure_property.is_rotation_continuous_m_closure_property import \
    is_rotation_continuous_m_closure_property


def create_uniform_c_arbiter_quorum_system(N, m):
    uniform_c_arbiter_quorum_system = list()
    for i in range(m):
        uniform_C_arbiter_quorum = list()
        for j in range(int((pow(2, m - 1) * N) / ((pow(2, m - 1)) + 1)) + 1):  # 可改
            uniform_C_arbiter_quorum.append((i + j) % N)
        uniform_c_arbiter_quorum_system.append(uniform_C_arbiter_quorum)
    return uniform_c_arbiter_quorum_system


if __name__ == '__main__':
    N = 30
    m = 3
    uniform_C_arbiter_quorum_system = create_uniform_c_arbiter_quorum_system(N, m)
    print(uniform_C_arbiter_quorum_system)

    # uniform_C_arbiter_quorum_system = \
    #     [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    #      [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    #      [15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    # # for q in uniform_C_arbiter_quorum_system:
    # #     print(len(q))
    #
    print(is_rotation_continuous_m_closure_property(uniform_C_arbiter_quorum_system, N))
