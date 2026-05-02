"""
Objednavka
- cislo
- jidlo
- piti
- stav - nova / zpracovava se / hotova

- vytvorit rucne seznam objednavek
- vypsat objednavky vcetne stavu
"""

class Objednavka:
    cislo = 1

    def __init__(self, cislo, jidlo, piti):
        self.cislo = Objednavka.cislo
        self.jidlo = jidlo
        self.piti = piti
        self.stav = "nova"

        Objednavka.cislo += 1
    
    def zmena_stavu(self):
        if self.stav == "nova":
            self.stav = "zpracovava se"
        elif self.stav == "zpracovava se":
            self.stav = "hotova"

objednavka1 = Objednavka(1, "burger", "kola")
objednavka2 = Objednavka(2, "hranolky", "voda")

objednavka1.zmena_stavu()

print(objednavka1.stav)

objednavky = [objednavka1, objednavka2]

for o in objednavky:
    print(o.cislo, o.jidlo, o.piti, o.stav)

