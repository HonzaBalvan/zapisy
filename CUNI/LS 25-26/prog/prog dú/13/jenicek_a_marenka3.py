class Uzel:
    def __init__(self, hodnota, levy = None, pravy = None):
        self.hodnota = hodnota
        self.levy = levy
        self.pravy = pravy

def vytvor_strom(seznam_intu):
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

def predelej_strom_do_sirky(koren):
    if not koren:
        return []
    sirkovy_strom = []
    fronta = [(koren, 0)]
    while fronta:
        uzel, uroven = fronta.pop(0)
        if uroven >= len(sirkovy_strom):
            sirkovy_strom.append([])
        sirkovy_strom[uroven].append(uzel.hodnota)
        if uzel.levy:
            fronta.append((uzel.levy, uroven + 1))
        if uzel.pravy:
            fronta.append((uzel.pravy, uroven + 1))
    return sirkovy_strom

pocet_stromu = int(input())
ciselne_stromy = [list(map(int, input().strip().split())) for _ in range(pocet_stromu)]

max_vyska = -1
max_koren = None
vystupy = []

for ciselny_strom in ciselne_stromy:
    stromovy_strom = vytvor_strom(ciselny_strom)
    sirkovy_strom = predelej_strom_do_sirky(stromovy_strom)
    vystupy.append(sirkovy_strom)

    if sirkovy_strom:
        if len(sirkovy_strom) > max_vyska:
            max_vyska = len(sirkovy_strom)
            max_koren = stromovy_strom.hodnota

for i, sirkovy_strom in enumerate(vystupy):
    if sirkovy_strom:
        for patro in sirkovy_strom:
            print(" ".join(map(str, patro)))
    else:
        print()
    
    print()

print(f"{max_vyska} {max_koren}")
