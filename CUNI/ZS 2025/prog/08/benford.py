n = 0
count = [0] * 9
cisla = []

while n != -1:
    n = int(input())
    cisla += [n]
cisla.pop()

for cislo in cisla:
    cislo_string = str(cislo)
    cislice_string = cislo_string[0]
    cislice = int(cislice_string)
    
    if cislice != 0:
        count[cislice-1] +=1

print(count)
