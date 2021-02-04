# cluster head => p1*k1(mod N)| 0 <= k1 <=N/p1-1 U p2*k2(mod N)| 0 <= k2 <=N/p2-1
# cluster member => p3*k3(mod N)| 0 <= k3 <=N/p3-1
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


def create_CRT_bi_coteries_clustered_head_and_member_quorum(list_of_three_p):
    # 計算N
    N = 1  # 初始化
    for p in list_of_three_p:
        N *= p

    CRT_bi_coteries_clustered_head_quorum = list()
    p1 = list_of_three_p[0]
    p2 = list_of_three_p[1]
    k1 = int(N / p1 - 1)
    k2 = int(N / p2 - 1)
    for i in range(0, k1 + 1):
        CRT_bi_coteries_clustered_head_quorum.append(p1 * i % N)
    for i in range(0, k2 + 1):
        CRT_bi_coteries_clustered_head_quorum.append(p2 * i % N)

    p3 = list_of_three_p[2]
    k3 = int(N / p3 - 1)
    CRT_bi_coteries_clustered_member_quorum = [p3 * i % N for i in range(0, k3 + 1)]
    return list(set(CRT_bi_coteries_clustered_head_quorum)), CRT_bi_coteries_clustered_member_quorum


p_list = [2, 3, 5]
N = 2 * 3 * 5
print(create_CRT_bi_coteries_clustered_head_and_member_quorum(p_list))
# print(is_rotation_closure_property(create_CRT_bi_coteries_clustered_head_and_member_quorum(p_list), N))
