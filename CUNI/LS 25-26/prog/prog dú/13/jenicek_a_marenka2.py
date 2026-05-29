class Uzel:
    def __init__(self, hodnota, levy = None, pravy = None):
        self.hodnota = hodnota
        self.levy = levy
        self.pravy = pravy


def vytvor_strom(seznam_intu):
    #print(*seznam_intu)
    koren = None
    
    for cislo in seznam_intu:                
        u = Uzel(cislo)
        # najdi misto
        k = koren        
        rodic = koren
        je_tam = False
        while k != None and not je_tam:
           rodic = k
           if cislo < k.hodnota:
               k = k.levy
           elif cislo > k.hodnota:
               k = k.pravy
           else: # cislo uz tam je  
               je_tam = True
        
        if rodic == None:
            koren = u            
        elif cislo < rodic.hodnota:
            rodic.levy = u
        elif cislo > rodic.hodnota:
            rodic.pravy = u
        else:
            pass
        
    return koren

def vypis_strom(koren):
    fronta = [koren]
    i = 0    

    while fronta:
        pracovni = fronta.pop(0)
        print(pracovni.hodnota)
        i += 1
        print(i)

        if pracovni.levy != None:
            fronta.append(pracovni.levy)
        if pracovni.pravy != None:
            fronta.append(pracovni.pravy)

def predelej_strom_do_sirky(koren, i, delka_stromu):
    sirkovy_strom = [[] for _ in range(delka_stromu)]
    #print(koren.hodnota)
    #print(koren.levy.hodnota)
    #print(koren.pravy.hodnota)

    sirkovy_strom[i].append(koren.hodnota)

    def sirka(vrchol, i):
        nonlocal sirkovy_strom

        sirkovy_strom[i].append(vrchol.hodnota)

        i += 1
        
        if vrchol.levy != None:
            sirka(vrchol.levy, i)

        if vrchol.pravy != None:
            sirka(vrchol.pravy, i)

    i += 1

    if koren.levy != None:
        sirka(koren.levy, i)

    if koren.pravy != None:
        sirka(koren.pravy, i)

    #print(*sirkovy_strom)
    return sirkovy_strom

def vypis_sirkovy_strom(sirkovy_strom):
    print()
    
    for patro in sirkovy_strom:
        print(patro)

pocet_stromu = int(input())
i = pocet_stromu

ciselne_stromy = []

while i > 0:
    ciselny_strom = input()
    ciselny_strom = ciselny_strom.split()

    for cislo in ciselny_strom:
        cislo = int(cislo)

    ciselne_stromy.append(ciselny_strom)

    i -= 1

for ciselny_strom in ciselne_stromy:
    stromovy_strom = vytvor_strom(ciselny_strom)
    #vypis_strom(stromovy_strom)
    vypis_sirkovy_strom(predelej_strom_do_sirky(stromovy_strom, 0, len(ciselny_strom)))
