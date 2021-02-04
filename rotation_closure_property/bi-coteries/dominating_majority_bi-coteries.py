# cluster head 取grid quorum one row and one column
# cluster member 取grid quorum one column or one row? 需驗證


import random
import math
from random import choice


def create_domination_majority_bi_coteries_clustered_head_quorum(N):
    num = random.randint(0, N - 1)
    return [(num + i) % N for i in range(math.floor(N / 2) + 1)]


def create_domination_majority_bi_coteries_clustered_member_quorum(N):
    all_maxgap_list = list()
    for x1 in range(N):
        for x2 in range(N):
            list1 = [(x1 - x2 - 1) % N, (x2 - x1 - 1) % N]
            if max(list1) == math.floor(N / 2):
                all_maxgap_list.append([x1, x2])

    return choice(all_maxgap_list)


create_domination_majority_bi_coteries_clustered_member_quorum(10)
