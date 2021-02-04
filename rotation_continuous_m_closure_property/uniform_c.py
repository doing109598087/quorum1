from rotation_continuous_m_closure_property.is_rotation_continuous_m_closure_property import \
    is_rotation_continuous_m_closure_property
import time


def create_uniform_c_arbiter_quorum_system(N, m):
    uniform_c_arbiter_quorum_system = list()
    for i in range(m):
        uniform_C_arbiter_quorum = list()
        for j in range(int((pow(2, m - 1) * N) / ((pow(2, m - 1)) + 1)) + 1):  # 有問題
            uniform_C_arbiter_quorum.append((i + j) % N)
        uniform_c_arbiter_quorum_system.append(uniform_C_arbiter_quorum)
    return uniform_c_arbiter_quorum_system


if __name__ == '__main__':
    start_time = time.time()
    # =============================================#
    N = 20
    m = 3
    uniform_C_arbiter_quorum_system = create_uniform_c_arbiter_quorum_system(N, m)
    print(uniform_C_arbiter_quorum_system)
    print(is_rotation_continuous_m_closure_property(uniform_C_arbiter_quorum_system, N))
    # =============================================#
    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
