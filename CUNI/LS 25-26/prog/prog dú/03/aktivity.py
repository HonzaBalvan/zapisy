def parse_input():
    input_cely = []

    inp = ""

    while inp != ".":
        inp = input()
        input_cely.append(inp)
    
    return input_cely

def je_datum(datum):
    datum_list = datum.split(".")

    for datum_cast in datum_list:
        if not datum_cast.isnumeric():
            return False

    if not int(datum_list[0]) < 32 or not int(datum_list[1]) < 13:
        return False

    return True

def je_cas(cas):
    cas_list = cas.split(":")

    for cas_cast in cas_list:
        if not cas_cast.isnumeric():
            return False

    if not int(cas_list[0]) < 24 or not int(cas_list[1]) < 60 or not int(cas_list[2]) < 60:
        return False

    return True

def rozkouskuj_a_over_radek(radek):
    radek_list = radek.split(" ")

    if not je_datum(radek_list[0]) or not je_datum(radek_list[-2]):
        return False 
    
    if not je_cas(radek_list[1]) or not je_cas(radek_list[-1]):
        return False

    return True

def spocitej_a_secti_cas(radek, soucet):
    radek_list = radek.split(" ")

    cas1_list = radek_list[1].split(":")
    cas2_list = radek_list[-1].split(":")

    datum_list = radek_list[0].split(".")
    mesic = int(datum_list[1])

    soucet[mesic] += int(cas2_list[0]) * 3600
    soucet[mesic] += int(cas2_list[1]) * 60
    soucet[mesic] += int(cas2_list[2])

    soucet[mesic] -= int(cas1_list[0]) * 3600
    soucet[mesic] -= int(cas1_list[1]) * 60
    soucet[mesic] -= int(cas1_list[2])

    return soucet

def sekundy_na_cas(soucet):
    cas = []

    cas.append(soucet // 3600)

    soucet %= 3600

    cas.append(soucet // 60)

    soucet %= 60

    cas.append(soucet)

    return cas

soucet = [0] * 13

output_celkem = 0

input_cely = parse_input()

for radek in input_cely:
    if rozkouskuj_a_over_radek(radek):
        soucet = spocitej_a_secti_cas(radek, soucet)

for i in range(1, 13):
    outp = sekundy_na_cas(soucet[i])
    if outp != [0, 0, 0]:
        print(f"{i:02}/2020: {outp[0]}:{outp[1]:02}:{outp[2]:02}")
    output_celkem += soucet[i]

konec = sekundy_na_cas(output_celkem)
print(f"celkem: {konec[0]}:{konec[1]:02}:{konec[2]:02}")
