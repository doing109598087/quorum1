from itertools import product

comb = list(product([n for n in range(30)], repeat=3))

# Print the obtained combinations

for i in comb:
    print(i)
print(len(list(comb)))
