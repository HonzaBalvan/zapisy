len_a, len_b = [int(x) for x in input().split()]

list_a = [int(x) for x in input().split()]

list_b = [int(x) for x in input().split()]

list_c = list_a + list_b

list_c.sort()

print(list_c)

indexes_a = []
indexes_b = []

a = list_a[0]
iterator_a = iter(list_a)

for l_bound in range(len_a + len_b):
    if a == list_c[l_bound]:
        indexes_a += [l_bound]
        a = next(iterator_a)
    else:
        indexes_b += [l_bound]

print(indexes_a)
print(indexes_b)
