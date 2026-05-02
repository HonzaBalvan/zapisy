class Prvek:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.ano = None
        self.ne = None
        self.je_list = True

    def pridani_ano(self, prvek):
        self.ano = prvek
        self.je_list = False

    def pridani_ne(self, prvek):
        self.ne = prvek
        self.je_list = False

    def vypis(self):
        if self.je_list == True:
            print(f"Je to {self.hodnota}? ")
        else:
            print(self.hodnota)

    def udelej_novou_otazku(self):
        stary_list = Prvek(self.hodnota)

        print("Co je to za zvíře? ")
        novy_list = Prvek(input())

        print("Jak by ses zeptal*a tak, aby odpověď pro toto zvíře byla ano a pro to předchozí ne? ")
        self.hodnota = input()

        self.pridani_ano(novy_list)
        self.pridani_ne(stary_list)

    def vyhodnoceni(self):
        self.vypis()
        vstup = input()

        if self.je_list == False:
            if vstup == "ano":
                self.ano.vyhodnoceni()
            elif vstup == "ne":
                self.ne.vyhodnoceni()
        elif vstup == "ano":
            print("Jupí!")
        elif vstup == "ne":
            self.udelej_novou_otazku() 

koren = Prvek("Myslíš si zvíře? ")
koren.pridani_ano(Prvek("Je to šelma? "))
koren.ano.pridani_ano(Prvek("lev"))
koren.ano.pridani_ne(Prvek("jelen"))

while True:
    koren.vyhodnoceni()