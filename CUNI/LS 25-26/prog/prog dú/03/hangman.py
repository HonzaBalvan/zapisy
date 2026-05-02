from random import random

def vygeneruj_zviratko():
    zviratka = ["zirafa", "ptak", "pes", "kocka", "lev", "slov", "tygr"]
    index = int(random() * len(zviratka))
    return list(zviratka[index])

def vykresli_hangmana(pocet_zivotu):
    hangman = ['''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
    _|___''',

           '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
    _|___''',

           '''
      _______
     |/      |
     |      
     |      
     |      
     |      
    _|___''',
           '''
      _______
     |/     
     |      
     |      
     |      
     |      
    _|___''',
           '''
      
     |
     |      
     |      
     |      
     |      
    _|___''',
           '''
     |  
    _|___''']

    print(hangman[pocet_zivotu])

def vykresli_slovo(slovo):
    print(slovo)

def nacti_vstup():
    return input("Vstup: ")

def je_tam(pismenko, cil):
    for cast_cile in cil:
        if cast_cile == pismenko:
            return True
    return False

def nahrad(pismenko, slovo, cil):
    for i in range(len(cil)):
        if cil[i] == pismenko:
            slovo[i] = pismenko
            
def je_uhodnuto(cil, slovo):
    if cil == slovo:
        return True
    return False

pocet_zivotu = 5

cil = vygeneruj_zviratko()

slovo = list(len(cil) * "*")

while not je_uhodnuto(cil, slovo) and pocet_zivotu > 0:
    vykresli_slovo(slovo)
    vykresli_hangmana(pocet_zivotu)

    pismenko = nacti_vstup()

    if je_tam(pismenko, cil):
        nahrad(pismenko, slovo, cil)
    else:
        pocet_zivotu -= 1

if je_uhodnuto(cil, slovo):
    vykresli_slovo(slovo)
    print("Uhodnuto!")

if pocet_zivotu == 0:
    vykresli_hangmana(pocet_zivotu)
    print("Umrel*a jsi!")

