len_a, len_b = [int(x) for x in input().split()]

list_a = [int(x) for x in input().split()]
list_b = [int(x) for x in input().split()]

list_c = list_a + list_b

list_c.sort()

indexes_a = []
indexes_b = []

iterator_a = iter(list_a)
a = next(iterator_a)

for l_bound in range(len_a + len_b):
    if a == list_a[-1]:
        if a == list_c[l_bound]:
            indexes_a += [l_bound+1]
        else:
            indexes_b += [l_bound+1]
    elif a == list_c[l_bound]:
        indexes_a += [l_bound+1]
        a = next(iterator_a)
    else:
        indexes_b += [l_bound+1]

for i in indexes_a:
    print(i, end = " ")
print()
for i in indexes_b:
    print(i, end = " ")
print()
