# cluster head => x, x + 1,...,(x + floor(N/2)) (mod N)
# cluster member => {x1, x2 } where maxgap(x1x2) =max{x1 − x2 − 1(mod N), x2 − x1− 1 (mod N)}=floor(N/2)


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
    # 不用list 產生器比較快
    return choice(all_maxgap_list)


print(create_domination_majority_bi_coteries_clustered_member_quorum(10))
