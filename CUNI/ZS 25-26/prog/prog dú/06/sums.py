n = 0
posloupnost = []

while n != -1:
    n = int(input())
    posloupnost += [n]
posloupnost.pop()

k = int(input())

posloupnost.sort()

min_sum = 0
for i in range(0, k):
    min_sum += posloupnost[i]
print(min_sum, end = " ")

max_sum = 0
for i in range(len(posloupnost)-1 , len(posloupnost) - k - 1, -1):
    max_sum += posloupnost[i]
print(max_sum)



