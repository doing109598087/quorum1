from rotation_continuous_closure_property.is_rotation_continuous_closure_property import \
    is_rotation_continuous_closure_property

q11 = {0, 1, 2, 3, 4, 5, 6}
q12 = {7, 8, 9, 10, 11, 12, 13}
q21 = {0, 1, 2, 7, 8, 9, 14, 15, 16}
q22 = {3, 4, 5, 10, 11, 12, 17, 18, 19}

C1 = [q11, q12]
C2 = [q21, q22]

C = [C1, C2]
N = 20
for q1 in C1:
    for q2 in C2:
        temp_quorum_system = list()
        temp_quorum_system.append(q1)
        temp_quorum_system.append(q2)
        print(q1, q2)
        print(is_rotation_continuous_closure_property(temp_quorum_system, N))
