n = int(input())
trojuhelnik = [[1]]

def pascaluv_trojuhelnik(n, trojuhelnik):
    tohle_patro = [1]
    predchozi_patro = trojuhelnik[-1]
    counter = len(predchozi_patro)

    for i in range(1, counter, 1):
        tohle_patro.append(predchozi_patro[i-1] + predchozi_patro[i])

    tohle_patro.append(1)

    trojuhelnik.append(tohle_patro)

    n -= 1

    if n > 1:    
        pascaluv_trojuhelnik(n, trojuhelnik)
    elif n <= 1:
        return trojuhelnik

if n > 1:
    pascaluv_trojuhelnik(n, trojuhelnik)

#for j in trojuhelnik:
#    print(j, end=", ")

print("[", end = "")
print(*trojuhelnik, sep = ", ", end = "")
print("]")
