def pripis_posloupnosti(hloubka, n, k, vypis):
  # má místo v listu
  # projede jím všechny čísla v rangei
  # pošle to rekurzí dokud nejsem na konci 
    if hloubka == k:
        for _ in vypis: print(_, end = " ")
        print()
        return

    for i in range(vypis[hloubka - 1] + 1, n + 1):
        vypis[hloubka] = i
        pripis_posloupnosti(hloubka + 1, n, k, vypis)

def vypis_posloupnosti(n):
    for k in range(1, n + 1):
        vypis = [0] * k
        hloubka = 0
        pripis_posloupnosti(hloubka, n, k, vypis)

vypis_posloupnosti(int(input()))
