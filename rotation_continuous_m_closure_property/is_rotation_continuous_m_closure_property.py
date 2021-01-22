import copy
from itertools import product


def get_two_quorum_continuous_overlap(quorum1, quorum2):
    all_continuous_overlap = list()
    for i in range(len(quorum1) - 1):
        for j in range(len(quorum2) - 1):
            if quorum1[i] == quorum2[j] and quorum1[i + 1] == quorum2[j + 1] and quorum1[i] + 1 == quorum1[i + 1]:
                all_continuous_overlap.append([quorum1[i], quorum1[i + 1]])
    return all_continuous_overlap


def get_all_quorum_continuous_overlap(quorum_system):
    first_two_quorum_continuous_overlap = get_two_quorum_continuous_overlap(quorum_system[0], quorum_system[1])
    all_quorum_continuous_overlap = copy.deepcopy(first_two_quorum_continuous_overlap)
    for i in range(len(first_two_quorum_continuous_overlap)):
        # print(all_quorum_continuous_overlap)
        for quorum in quorum_system:
            if first_two_quorum_continuous_overlap[i][0] in quorum and first_two_quorum_continuous_overlap[i][
                1] in quorum:
                continue
            else:
                if first_two_quorum_continuous_overlap[i] in all_quorum_continuous_overlap:
                    all_quorum_continuous_overlap.remove(first_two_quorum_continuous_overlap[i])
                else:
                    continue

    return all_quorum_continuous_overlap


def create_one_quorum_rotation(quorum, N):
    return [[(n + i) % N for n in quorum] for i in range(N)]


def create_all_quorum_rotation(quorum_system, N):
    return [create_one_quorum_rotation(quorum_system[i], N) for i in range(len(quorum_system))]


def create_all_product_of_all_rotation_of_all_quorom(quorum_system, N):
    len_of_quorum = len(quorum_system)
    comb = list(product([n for n in range(N)], repeat=len_of_quorum))
    all_rotation_of_all_quorom = create_all_quorum_rotation(quorum_system, N)
    all_product_of_all_rotation_of_all_quorom_list = [
        [all_rotation_of_all_quorom[i][com[i]] for i in range(len_of_quorum)] for com in comb]
    return all_product_of_all_rotation_of_all_quorom_list


def is_rotation_continuous_m_closure_property(quorum_system, N):
    all_product_of_all_rotation_of_all_quorom_list = create_all_product_of_all_rotation_of_all_quorom(quorum_system, N)
    count = 0
    len_of_quorum = len(quorum_system)
    total_overlap_count = 0
    for i in range(pow(N, len_of_quorum)):
        print(all_product_of_all_rotation_of_all_quorom_list[i], end='')
        overlap_of_list = get_all_quorum_continuous_overlap(all_product_of_all_rotation_of_all_quorom_list[i])
        print(overlap_of_list)
        print(len(overlap_of_list))
        total_overlap_count += len(overlap_of_list)
        if len(overlap_of_list):
            count += 1
    print('total 組合:', count)
    print('total_overlap: ', total_overlap_count)
    average_overlap = total_overlap_count / count
    if count == pow(N, len_of_quorum):
        return True, average_overlap
    return False, average_overlap


if __name__ == '__main__':
    N = 20
    C = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
         [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
         [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    print(is_rotation_continuous_m_closure_property(C, N))

