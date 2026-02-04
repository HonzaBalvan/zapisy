orig = int(input())
n = orig
prvoc = []

def je_prvocislo(p):
    a = 2
    while a < p:
        if p % a == 0:
            return False
        else:
            a += 1
    return True

x = 2
while x <= n:
    if n % x == 0 and je_prvocislo(x):
        n /= x
        prvoc.append(x)
    else:
        x += 1

stri = ""
for k in prvoc[0:-1]:
    stri += str(k) + "*" 
stri += str(prvoc[-1])    
    
print(str(orig) + "=" + stri)
