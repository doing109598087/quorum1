import copy
from itertools import product


# overlap refactor: https://www.coderbridge.com/@kuanghsuan/2b75b952ea6f402ba11a0de654077b91
def overlap(list1, list2):
    return list(set(list1).intersection(list2))


def overlap_of_lists(lists):
    intersection_list = overlap(lists[0], lists[1])
    for i in range(len(lists)):
        intersection_list = overlap(intersection_list, lists[i])

    return intersection_list


def create_one_quorom_rotation(quorum, N):
    all_rotation_of_one_quorom = list()
    for i in range(N):
        all_rotation_of_one_quorom.append([(n + i) % N for n in quorum])
    return all_rotation_of_one_quorom


def create_all_quorom_rotation(quorum_system, N):
    all_rotation_of_all_quorom = list()
    for i in range(len(quorum_system)):
        # print(create_one_quorom_rotation(quorum_system[i], N))
        all_rotation_of_all_quorom.append(create_one_quorom_rotation(quorum_system[i], N))
    return all_rotation_of_all_quorom


def create_all_product_of_all_rotation_of_all_quorom(all_rotation_of_all_quorom, N, len_of_quorum):
    comb = list(product([n for n in range(N)], repeat=len_of_quorum))
    all_product_of_all_rotation_of_all_quorom_list = list()
    for com in comb:
        temp_list = list()
        for i in range(3):
            temp_list.append(all_rotation_of_all_quorom[i][com[i]])
        all_product_of_all_rotation_of_all_quorom_list.append(temp_list)
    return all_product_of_all_rotation_of_all_quorom_list


def is_rotation_m_closure_property(list1, N, len_of_quorum):
    all_product_of_all_rotation_of_all_quorom_list = create_all_product_of_all_rotation_of_all_quorom(list1, N,
                                                                                                      len_of_quorum)
    count = 0
    for i in range(pow(N, len_of_quorum)):
        print(all_product_of_all_rotation_of_all_quorom_list[i], end='')
        print(overlap_of_lists(all_product_of_all_rotation_of_all_quorom_list[i]))
        if len(overlap_of_lists(all_product_of_all_rotation_of_all_quorom_list[i])) != 0:
            count += 1
    if count == pow(N, len_of_quorum):
        print(count)
        return True


N = 30
C1 = [[0, 5, 10, 15, 20, 25], [0, 3, 6, 10, 9, 12, 15, 18, 21, 24, 27],
      [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]]

list1 = create_all_quorom_rotation(C1, N)

all_product_of_all_rotation_of_all_quorom_list = create_all_product_of_all_rotation_of_all_quorom(list1, N, 3)

is_rotation_m_closure_property(list1, N, 3)

# for i in range(5000):
#     print(all_product_of_all_rotation_of_all_quorom_list[i], end='')
#     print(overlap_of_lists(all_product_of_all_rotation_of_all_quorom_list[i]))
