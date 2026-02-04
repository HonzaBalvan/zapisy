n = 0
posloupnost = []

while n != -1:
    n = float(input())
    posloupnost.append(n)
posloupnost.pop()

def minima_maxima(posloupnost):
    maxima = [posloupnost[0]]
    
    for i in range(1, len(posloupnost)):
        if posloupnost[i] > maxima[i-1]:
            maxima.append(posloupnost[i])
        else:
            maxima.append(maxima[i-1])

    opac_posloupnost = posloupnost[::-1]
    opac_minima = [opac_posloupnost[0]]

    for i in range(1, len(opac_posloupnost)):
        if opac_posloupnost[i] < opac_minima[i-1]:
            opac_minima.append(opac_posloupnost[i])
        else:
            opac_minima.append(opac_minima[i-1])

    minima = opac_minima[::-1]

    return minima, maxima

def deliciBod(posloupnost):
    if len(posloupnost) == 0:
        return -1

    if len(posloupnost) == 1:
        return 0

    minima, maxima = minima_maxima(posloupnost)

    if posloupnost[0] <= minima[0]:
        return 0

    for i in range(1, len(posloupnost)-1):
        if maxima[i - 1] <= posloupnost[i] <= minima[i + 1]:
            return i

    if posloupnost[-1] >= maxima[-1]:
        return len(posloupnost) - 1

    return -1

print(deliciBod(posloupnost))
