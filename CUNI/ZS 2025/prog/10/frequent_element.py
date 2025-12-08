counter = {}
inp = int(input())

while inp != -1:
    if inp in counter.keys():
        counter[inp] += 1
    else:
        counter[inp] = 1

    inp = int(input())

sorted_counter = sorted(counter.items(), key = lambda x: x[1], reverse = True)

most_frequent = sorted_counter[0]

print(most_frequent[0])
