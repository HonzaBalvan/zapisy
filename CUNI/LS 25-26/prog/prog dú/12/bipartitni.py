def prevod_na_sousedy(mesta, silnice):
    for siln in silnice:
        mesta[siln[0]][1].append(siln[1])
        mesta[siln[1]][1].append(siln[0])
    
    return mesta

def kontrola(mesto, mesta):
    zasobnik = []
    zasobnik.append(mesto)    
    
    while zasobnik:
        mesto = zasobnik.pop()

        if mesto[2] == 1:
            for cislo in mesto[1]:
                if mesta[cislo][2] == 1:
                    return False
                
                if mesta[cislo][2] == -1:
                    zasobnik.append(mesta[cislo])
                mesta[cislo][2] = 0
                

        if mesto[2] == 0:
            for cislo in mesto[1]:
                if mesta[cislo][2] == 0:
                    return False

                if mesta[cislo][2] == -1:
                    zasobnik.append(mesta[cislo])
                mesta[cislo][2] = 1
        
    return True

pocet_mest = int(input())

mesta = [["", [], -1] for _ in range(pocet_mest + 1)]

pocet_silnic = int(input())

silnice = [["", ""] for _ in range(pocet_silnic)]

for i in range(pocet_silnic):
    x, y = input().split(" ")
    silnice[i][0], silnice[i][1] = int(x), int(y)

mesta = prevod_na_sousedy(mesta, silnice)

mesta[1][2] = 1

if kontrola(mesta[1], mesta):
    pulky = [[], []]

    for i in range(1, pocet_mest + 1):
        if mesta[i][2] == 0:
            pulky[0].append(i)
        elif mesta[i][2] == 1:
            pulky[1].append(i)

    pulky.sort()
    for pulka in pulky:
        print(*pulka)

else:
    print("Nelze")
