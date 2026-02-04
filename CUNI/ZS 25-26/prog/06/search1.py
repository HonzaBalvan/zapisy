data_len, queries_len = [int(x) for x in input().split()]

data = [int(x) for x in input().split()]

queries = [ int(x) for x in input().split()]

#for i in data:
#    print(i)

#for i in queries:
#    print(i)

def bin_search(data, query, pos):
    if query == data[pos]:
        print("bingo ", pos)
        return pos
    elif query < data[pos]:
        print("mensi ", pos)
        pos = pos // 2 + 1
        return bin_search(data, query, pos)
    elif query > data[pos]:
        print("vetsi ", pos)
        pos += pos // 2 - 1
        return bin_search(data, query, pos)

for i in queries:
    if i == data [0]:
        print(0)
    elif i == data[-1]:
        print(data_len-1)
    else:
        print(bin_search(data, i, (data_len - 1) // 2))
