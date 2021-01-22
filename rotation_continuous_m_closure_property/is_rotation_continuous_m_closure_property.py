import copy


def get_two_quorum_continuous_overlap(quorum1, quorum2):
    all_continuous_overlap = list()
    for i in range(len(quorum1) - 1):
        for j in range(len(quorum2) - 1):
            if quorum1[i] == quorum2[j] and quorum1[i + 1] == quorum2[j + 1]:
                all_continuous_overlap.append([quorum1[i], quorum1[i + 1]])
    return all_continuous_overlap


def get_all_quorum_continuous_overlap(quorum_system):
    first_two_quorum_continuous_overlap = get_two_quorum_continuous_overlap(quorum_system[0], quorum_system[1])
    all_quorum__continuous_overlap = copy.deepcopy(first_two_quorum_continuous_overlap)
    for i in range(len(first_two_quorum_continuous_overlap)):
        for quorum in quorum_system:
            if first_two_quorum_continuous_overlap[i][0] in quorum and first_two_quorum_continuous_overlap[i][
                1] in quorum:
                continue
            else:
                all_quorum__continuous_overlap.remove(first_two_quorum_continuous_overlap[i])

    return all_quorum__continuous_overlap


# print(get_all_quorum_continuous_overlap([[0, 1, 2], [0, 1, 2], [0, 1]]))
# print(get_all_quorum_continuous_overlap([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1]]))
# print(get_all_quorum_continuous_overlap([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2]]))
