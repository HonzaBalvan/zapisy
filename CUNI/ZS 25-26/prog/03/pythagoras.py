from math import gcd

n = int(input())
ctverce = []
pocet = 0

for x in range(1, n + 1, 1):
   ctverce.append(x ** 2)

for a in ctverce:
    for b in ctverce:
        if a < b and gcd(a, b) == 1 and a + b in ctverce:
            pocet += 1
            
print(pocet)
