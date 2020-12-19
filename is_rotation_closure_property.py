import copy


def is_two_quorum_intersection(quorum1, quorum2):
    for num in quorum1:
        if num in quorum2:
            print(True)
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
    # print(C_total)
    return C_total


def flatten(q_s_all):
    q_s_all_f = list()  # quorum_system_all_flatten
    for q_s in q_s_all:
        for q in q_s:
            q_s_all_f.append(q)
    return q_s_all_f


def is_rotation_closure(Quorum_system, N):
    count = 0
    q_s_all = create_all_rotation(Quorum_system, N)
    q_s_all_f = flatten(q_s_all)
    for q1 in q_s_all_f:
        for q2 in q_s_all_f:
            print(q1, q2)
            if is_two_quorum_intersection(q1, q2):
                count += 1
    return count == (N * len(Quorum_system)) ** 2


if __name__ == '__main__':
    C1 = [[0, 1, 2, 4], [3, 4, 5, 7], [0, 2, 6, 7]]
    # C2 = [[0, 1], [0, 2], [1, 2]]
    # C_grid = [[1, 4, 5, 6, 7, 9, 13], [14, 15, 3, 7, 11, 12, 13]]

    # print(create_all_rotation(C1, 8))
    print(is_rotation_closure(C1, 8))

    # print(create_all_rotation(C2, 4))
    # print(is_rotation_closure(C2, 4))

    # print(is_rotation_closure(C_grid, 15))




