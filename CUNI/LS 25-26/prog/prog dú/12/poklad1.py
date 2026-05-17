def vypis_mapu(mapa):
    for radek in mapa:
        print(*radek)

def najdi_pocatek(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "o":
                return i, j

def sousedi(mapa, radek, sloupec):
    seznam_sousedu = []
    for zmena_radek, zmena_sloupec in smery:
        novy_radek = radek + zmena_radek
        novy_sloupec = sloupec + zmena_sloupec
        if novy_radek >= 0 and novy_radek < max_radek and novy_sloupec >= 0 and novy_sloupec < max_sloupec:
            if mapa[novy_radek][novy_sloupec] == "$":
                seznam_sousedu.append((novy_radek, novy_sloupec, True))
            if mapa[novy_radek][novy_sloupec] == ".":
                seznam_sousedu.append((novy_radek, novy_sloupec, False))
    
    return seznam_sousedu

def vlna(mapa, i, j):
    fronta = [(i, j, False)]

    while len(fronta) > 0:
        i_pracovni, j_pracovni, poklad = fronta[0]
        fronta.pop(0)

        for soused in sousedi(mapa, i_pracovni, j_pracovni):
            if soused[2] == True:
                return True

            fronta.append(soused)
            mapa[soused[0]][soused[1]] = "o"

            vypis_mapu(mapa)
            input()

        return False

with open("vstup.blud", encoding="utf-8") as f:
    vstup1 = f.readlines()

vstup = []
for radek in vstup1:
    radek = radek.strip()
    vstup.append(list(radek))

smery = [(1,0), (-1,0), (0,1), (0,-1)]

max_radek = len(vstup)
max_sloupec = len(vstup[0])

i_pocatek, j_pocatek = najdi_pocatek(vstup)
print(i_pocatek, j_pocatek)
print(vlna(vstup, i_pocatek, j_pocatek))
