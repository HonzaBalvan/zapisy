n = int(input())
i = 0

while True:
    n = n // 10
    i += 1
    if n == 0:
        break
print(i)
