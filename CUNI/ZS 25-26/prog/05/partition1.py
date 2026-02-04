n = 0
posloupnost = []

while n != -1:
    n = float(input())
    posloupnost.append(n)
posloupnost.pop()

def delicibod(posloupnost, k):
    for l in range(len(posloupnost)-k):
        if posloupnost[l] > posloupnost[k]:
            return False
        
    for m in range(k, len(posloupnost)):
        if posloupnost[m] < posloupnost[k]:
            return False

    return True

for i in range(len(posloupnost)):
    if delicibod(posloupnost, i):
        print(i, posloupnost[i], sep = ", ")
        break
