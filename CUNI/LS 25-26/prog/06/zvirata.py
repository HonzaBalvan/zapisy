class Zvire:                           #CLASS ZVIRE
    def __init__(self, nazev):
        self.nazev = nazev
        self.dalsi = None

    def prichazi_za_mne(self, dalsi):
        self.dalsi = dalsi

    def kousni_dalsiho(self):
        if self.dalsi != None:
            return f{self.nazev}: {self.dalsi.nazev} ma ode me kousanec

        return f{self.nazev}: nikdo za mnou neni

vstup = input()                        #VSTUP PRVNI
prvni = Zvire(vstup)
predchozi = prvni
vstup = input()

while vstup != konec:                #CYKLUS VSTUP OSTATNI
    novy = Zvire(vstup)
    predchozi.prichazi_za_mne(novy)
    predchozi = novy
    vstup = input()

zvire = prvni                          #VYPIS ZVIRAT
while zvire.dalsi != None:
    print(zvire.nazev)
    zvire = zvire.dalsi
print(zvire.nazev)

prvni = prvni.dalsi                    #PRVNI ODEJDE Z FRONTY

predbihac = Zvire(ptakopysk)         #PREDBIHAC 1
predbihac.dalsi = prvni
prvni = predbihac

predbihac = Zvire(mravenec)          #PREDBIHAC 2
predbihac.dalsi = prvni
prvni = predbihac

zvire = prvni                          #KOUSANI
while zvire.dalsi != None:
    print(zvire.kousni_dalsiho())
    zvire = zvire.dalsi
print(zvire.kousni_dalsiho())