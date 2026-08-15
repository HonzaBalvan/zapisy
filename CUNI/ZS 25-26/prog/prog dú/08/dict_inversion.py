d = {}
def dict_inversion(d):
    input_nerozdeleny = str(input())

    if input_nerozdeleny == "---":
        return d

    jmeno, atributy_nerozdelene = input_nerozdeleny.split(": ")
    atributy = atributy_nerozdelene.split(", ")
    for atributa in atributy:
        d[atributa] = d.get(atributa, []) + [jmeno]

    dict_inversion(d)

dict_inversion(d)

d = dict(sorted(d.items()))

for atributa, jmena in d.items():
    print(f"{atributa}: {', '.join(jmena)}")
print("---")
