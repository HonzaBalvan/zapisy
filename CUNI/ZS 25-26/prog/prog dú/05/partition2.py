n = 0
posloupnost = []

while n != -1:
    n = float(input())
    posloupnost.append(n)
posloupnost.pop()

def minimum(posloupnost):
    min = posloupnost[0]

    for i in posloupnost:
        if i < min:
            min = i

    return min

def maximum(posloupnost):
    max = posloupnost[0]

    for i in posloupnost:
        if i > max:
            max = i

    return max

def deliciBod(posloupnost):
    if len(posloupnost) == 0:
        return -1

    if len(posloupnost) == 1:
        return 0

    pravaPosloupnostNulta = posloupnost[1:]
    levaPosloupnostPosledni = posloupnost[:-1]

    minNulte = minimum(pravaPosloupnostNulta)
    maxPosledni = maximum(levaPosloupnostPosledni)

    if posloupnost[0] < minNulte:
        return 0

    for i in range(1, len(posloupnost) - 1):
        levaPosloupnost = posloupnost[:i]
        pravaPosloupnost = posloupnost[i+1:]

        max = maximum(levaPosloupnost)
        min = minimum(pravaPosloupnost)

        if max < posloupnost[i] and posloupnost[i] < min:
            return i

    if posloupnost[-1] > maxPosledni:
        return len(posloupnost) - 1

    return -1

print(deliciBod(posloupnost))
