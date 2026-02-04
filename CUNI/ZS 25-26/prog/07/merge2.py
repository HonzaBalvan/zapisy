arr1 = [int(x) for x in input().split()]

arr2 = [int(x) for x in input().split()]

def array_merge(a, b):
    i = 0
    j = 0
    sorted = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            sorted += [arr1[i]]
            i += 1
        else:
            sorted += [arr2[j]]
            j += 1

    sorted.extend(arr1[i:])
    sorted.extend(arr2[j:])

    return sorted

for i in array_merge(arr1, arr2):
    print(i, end = " ")
print()
