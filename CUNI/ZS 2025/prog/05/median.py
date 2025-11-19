n = 0
posloupnost = []

while n != -1:
    n = int(input())
    posloupnost.append(n)
posloupnost.pop()

def bubblesort(posloupnost):
    d = len(posloupnost)
    for i in range(d-1):
        for j in range(d-i-1):
            if posloupnost[j] > posloupnost[j+1]:
                posloupnost[j], posloupnost[j+1] = posloupnost[j+1], posloupnost[j]

    return posloupnost

bubblesort(posloupnost)

d = len(posloupnost)
if d % 2 == 1:
    print(posloupnost[d//2])
else:
    print((posloupnost[d//2-1] + posloupnost[d//2])/2)
