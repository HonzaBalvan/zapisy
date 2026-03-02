length_x = int(input())

list_x = [int(input()) for i in range(length_x)]

length_y = int(input())

list_y = [int(input()) for i in range(length_y)] #INPUT

def append_and_sort(list_x, item_y):
    list_x.append(item_y)
    i = len(list_x) - 2 #APPEND

    while i > -1 and list_x[i] > list_x[i+1]: #SORT
        list_x[i], list_x[i+1] = list_x[i+1], list_x[i]
        i -=1

    return list_x

for i in range(length_y): 
    list_x = append_and_sort(list_x, list_y[i])

print(*list_x, sep = "\n") #OUTPUT

