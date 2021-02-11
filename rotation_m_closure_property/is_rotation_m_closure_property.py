from same_function import create_all_product_of_all_rotation_of_all_quorom


def get_two_quorum_intersection(quorum1, quorum2):
    return set(quorum1).intersection(quorum2)


def get_all_quorum_continuous_intersection(quorum_system):
    # quorum_system = sort_quorum_system_by_len(quorum_system)
    intersection_list = get_two_quorum_intersection(quorum_system[0], quorum_system[1])
    for i in range(len(quorum_system)):
        intersection_list = get_two_quorum_intersection(intersection_list, quorum_system[i])
    return intersection_list


def is_rotation_m_closure_property(quorum_system, N):
    all_product_of_all_rotation_of_all_quorom_list = create_all_product_of_all_rotation_of_all_quorom(quorum_system, N)
    all_rotation_count = len(all_product_of_all_rotation_of_all_quorom_list)
    intersection_count = 0
    for i in range(all_rotation_count):
        intersection_of_list = get_all_quorum_continuous_intersection(all_product_of_all_rotation_of_all_quorom_list[i])
        if len(intersection_of_list):
            intersection_count += 1
    if intersection_count == all_rotation_count:
        return True
    return False


if __name__ == '__main__':
    # N = 9
    # C = [[0, 1, 2, 4, 5, 7, 8], [0, 2, 3, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6]]

    N = 30
    C = [[0, 5, 10, 15, 20, 25], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27],
         [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]]
    print(is_rotation_m_closure_property(C, N))
