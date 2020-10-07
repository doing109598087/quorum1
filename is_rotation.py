import copy


def is_two_quorum_intersection(quorum1, quorum2):
    for num in quorum1:
        if num in quorum2:
            return True
    return False


def find_N(Quorum_system):
    new_C_list = list()
    for Q in Quorum_system:
        for num in Q:
            new_C_list.append(num)
    return max(new_C_list) + 1


def create_one_rotation_quorum_system(Quorum_system, r, N):
    temp_list = copy.deepcopy(Quorum_system)
    for i in range(len(Quorum_system)):
        for j in range(len(Quorum_system[i])):
            temp_list[i][j] = (Quorum_system[i][j] + r) % N

    return temp_list


def create_all_rotation(Quorum_system, N):
    C_total = list()
    for r in range(1, N):
        C_total.append(create_one_rotation_quorum_system(Quorum_system, r, N))
    return C_total


def is_rotation_closure(Quorum_system, all_rotation_Quorum_system, N):
    count = 0
    for Quorum_system in all_rotation_Quorum_system:
        for Q in Quorum_system:
            for i in range(len(Quorum_system)):
                if is_two_quorum_intersection(Quorum_system[i], Q):
                    count += 1
    if count == (N-1) * len(Quorum_system) * len(Quorum_system):
        return True
    else:
        return False


C = [[0, 1, 2, 4], [3, 4, 5, 7], [0, 2, 6, 7]]
print(is_rotation_closure(C, create_all_rotation(C, find_N(C)), find_N(C)))

## - one 參數

