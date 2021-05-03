import numpy as np
from random import choice
from rotation_closure_property.is_rotation_closure_property import is_rotation_closure_property


def create_one_torus_quorum(n, t, w):
    nd_array = (np.arange(n)).reshape(t, w)
    print(nd_array)
    result = list()
    for i in range(w):
        result.append(choice(nd_array[:, i]))
    return result


N = 30
t = 2
w = 15
quorum_system = list()
quorum1 = create_one_torus_quorum(N, t, w)
quorum2 = [0, 15]
# quorum2 = [0, 9, 18]
# quorum2 = [1, 10, 19]
# quorum2 = [2, 11, 20]
quorum_system.append(quorum1)
quorum_system.append(quorum2)

print(quorum_system)
print(is_rotation_closure_property(quorum_system, N))
