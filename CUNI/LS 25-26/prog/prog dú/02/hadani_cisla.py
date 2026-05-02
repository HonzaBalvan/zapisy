from random import random

hadane_cislo = int(100*random())

tip = int(input("Tipni si cislo: "))

pocet_pokusu = 1

while tip != hadane_cislo:

    if tip < hadane_cislo:
        print("Hadane cislo je vetsi. Zkus to znovu.")
    elif tip > hadane_cislo:
        print("Hadane cislo je mensi. Zkus to znovu.")

    pocet_pokusu += 1

    tip = int(input("Tipni si cislo: "))

print(f"Ano spravne! Hadane cislo bylo {hadane_cislo}.")
print(f"Tipoval*a jsi {pocet_pokusu}krat.")

