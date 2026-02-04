originalni = int(input())
prvocisla = [2]
prvocinitele = []

def je_prvocislo(p, prvocisla):
    for i in prvocisla:
        if p % i == 0:
            return False
    return True
 
def prvocisla_list(n, prvocisla):
    for i in range(2, int(n ** 0.5) + 1, 1):
        if je_prvocislo(i, prvocisla): 
            prvocisla.append(i)
        
    return prvocisla
    
def rozklad(n, prvocisla, prvocinitele):
    i = 2
    while i <= len(prvocisla):
        if n % i == 0:
            prvocinitele.append(i)
            n //= i
        else:
            i += 1
            
    return prvocinitele

prvocisla = prvocisla_list(originalni, prvocisla)    
for k in prvocisla:
    print(k, end = ",, ")
    
print()

prvocinitele = rozklad(originalni, prvocisla, prvocinitele)
for l in prvocinitele:
    print(l, end = ", ")
print
    
