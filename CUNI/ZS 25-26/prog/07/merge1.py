arr1 = [int(x) for x in input().split()]

arr2 = [int(x) for x in input().split()]

def array_merge(arr1, arr2):
    if len(arr1) == len(arr2) == 1:
        if arr1[0] >= arr2[0]:
            arr1.insert(0, arr2[0])
        else:
            arr1 += [arr2[0]]
        return arr1

    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1

    j = 0
    for i in range(len(arr1)):
        if arr1[i] <= arr2[j] and arr1[i+1] > arr2[j]: 
            arr1.insert(i + 1, arr2[j])
            j += 1

        if j == len(arr2) - 1:
            break

    if arr1[0] > arr2[0]:
        arr1.insert(0, arr2[0])

    if arr1[-1] <= arr2[-1]:
        arr1 += [arr2[-1]]
    else:
        arr1.insert(-1, arr2[-1])

    return arr1

for i in array_merge(arr1, arr2):
    print(i, end = " ")
print()
