data_len, queries_len = [int(x) for x in input().split()]

data = [int(x) for x in input().split()]

queries = [ int(x) for x in input().split()]

def bin_search(data, query):
    left = 0
    right = data_len - 1

    while left <= right:
        pos = (left + right) // 2

        if (data[pos] == query and data[pos-1] != query) or (data[pos] == query and pos == 0):
            return pos + 1

        if data[pos] == query and data[pos-1] == query:
            right -= 1

        if data[pos] < query:
            left = pos + 1
        else:
            right = pos - 1

    return 0

for i in queries:
    print(bin_search(data, i), end = " ")
print()




