# cluster head => p1*k1(mod N)| 0 <= k1 <=N/p1-1 U p2*k2(mod N)| 0 <= k2 <=N/p2-1
# cluster member => p3*k3(mod N)| 0 <= k3 <=N/p3-1
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property
from same_function import create_one_crt_quorum


def create_CRT_bi_coteries_clustered_head_quorum(p1, p2, N):
    return create_one_crt_quorum(p1, N) + create_one_crt_quorum(p2, N)


def create_CRT_bi_coteries_clustered_member_quorum(p, N):
    return create_one_crt_quorum(p, N)


def create_CRT_bi_coteries_clustered_head_and_member_quorum(list_of_three_p):
    # 計算N
    N = 1  # 初始化
    for p in list_of_three_p:
        N *= p
    p1 = list_of_three_p[0]
    p2 = list_of_three_p[1]
    CRT_bi_coteries_clustered_head_quorum = create_CRT_bi_coteries_clustered_head_quorum(p1, p2, N)
    p3 = list_of_three_p[2]
    CRT_bi_coteries_clustered_member_quorum = create_CRT_bi_coteries_clustered_member_quorum(p3, N)
    return [set(CRT_bi_coteries_clustered_head_quorum),
            set(CRT_bi_coteries_clustered_head_quorum),
            CRT_bi_coteries_clustered_member_quorum]


p_list = [2, 3, 5]
N = 2 * 3 * 5
CRT_bi_coteries_clustered_head_and_member_quorum_system = create_CRT_bi_coteries_clustered_head_and_member_quorum(
    p_list)
print(CRT_bi_coteries_clustered_head_and_member_quorum_system)
print(len(CRT_bi_coteries_clustered_head_and_member_quorum_system[0]),
      len(CRT_bi_coteries_clustered_head_and_member_quorum_system[1]),
      len(CRT_bi_coteries_clustered_head_and_member_quorum_system[2]))
print(is_rotation_closure_property(CRT_bi_coteries_clustered_head_and_member_quorum_system, N))
