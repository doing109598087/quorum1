import copy


def is_two_quorum_continous_intersection(quorum1, quorum2):
    quorum1.sort()
    quorum2.sort()
    for i in range(len(quorum1)-1):
        for j in range(len(quorum2)-1):
            print(Q1[i], Q2[j])
            if quorum1[i] == quorum2[j] and quorum1[i + 1] == quorum2[j + 1]:
                return True
    return False


def create_one_rotation_quorum_system(Quorum_system, r, N):
    temp_list = copy.deepcopy(Quorum_system)
    for i in range(len(Quorum_system)):
        for j in range(len(Quorum_system[i])):
            temp_list[i][j] = (Quorum_system[i][j] + r) % N

    return temp_list


def create_all_rotation(Quorum_system, N):
    C_total = list()
    for r in range(0, N):
        C_total.append(create_one_rotation_quorum_system(Quorum_system, r, N))
    return C_total


def flatten(q_s_all):
    q_s_all_f = list()  # quorum_system_all_flatten
    for q_s in q_s_all:
        for q in q_s:
            q_s_all_f.append(q)
    return q_s_all_f


def is_rotation_continous_closure(Quorum_system, N):
    count = 0
    q_s_all = create_all_rotation(Quorum_system, N)
    q_s_all_f = flatten(q_s_all)
    for q1 in q_s_all_f:
        for q2 in q_s_all_f:

            if is_two_quorum_continous_intersection(q1, q2):
                count += 1
    return count == (N * len(Quorum_system)) ** 2


Q_c_grid_system = []
Q1 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 1, 19, 25, 31, 2, 20, 26, 32]
Q2 = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 9, 15, 33, 4, 10, 16, 34]
Q_c_grid_system.append(Q1)
Q_c_grid_system.append(Q2)

print(is_rotation_continous_closure(Q_c_grid_system, 35))
