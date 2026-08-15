n = abs(int(input()))
bina = []

if n == 0:
    print(0)

while n > 0:
    bina.append(n % 2)
    n = n // 2

for i in reversed(bina):
    print(i, end='')
