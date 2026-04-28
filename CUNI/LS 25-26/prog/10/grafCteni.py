class Graf:
    def __init__(self, n):
    '''
    účel: vytvoření instance třídy
    význam parametrů: počet vrcholů
    návratová hodnota: None, je to konstruktor
    '''
        self.n = n
        self.seznam_sousedu = [[] for _ in range(n)]

    def __repr__(self):
    '''
    účel: reprezentace objektu např. pro print()
    význam parametrů: nejsou
    návratová hodnota: str, výpis sousedů všech vrcholů
    '''
        return str(self.seznam_sousedu)

    def pridej_hranu(self, i, j):
    '''
    účel: přidání souseda -- hrany
    význam parametrů: vrcholy, druhý vrchol přidám jako souseda prvního
    návratová hodnota: None, soused se jen přidá a nic se nevrátí
    '''
        self.seznam_sousedu[i].append(j)

    def x(self): 
    '''
    účel: zjištění počtu vrcholů grafu
    význam parametrů: nejsou
    navrátová hodnota: int, počet vrcholů grafu
    '''
        return self.n

    def y(self, u):
    '''
    účel: zjištění počtu sousedů vrcholu grafu
    význam parametrů: číslo vrcholu, u kterého chceme zjistit počet sousedů
    navrátová hodnota: int, počet sousedů vrcholu
    '''
        return len(self.seznam_sousedu[u])

    def p(self):
    '''
    účel: zjištění počtu sousedů všech vrcholů grafu
    význam parametrů: nejsou
    navrátová hodnota: int, počet sousedů všech vrcholů
    '''
        return sum(len(self.seznam_sousedu[u]) for u in range(self.n))

    def mn(self):
    '''
    účel: zjištění vrcholů bez sousedů
    význam parametrů: nejsou
    navrátová hodnota: list, seznam vrcholů bez sousedů
    '''
        return [u for u in range(self.n) if len(self.seznam_sousedu[u]) == 0]

    def e(self, i, j):
    '''
    účel: zjištění jestli je vrchol sousedním vrcholem jiného vrcholu
    význam parametrů: dva vrcholy, zjišťujeme zda je druhý sousedem prvního
    navrátová hodnota: Bool, podle toho zda druhý vrchol je sousedem prvního, nebo ne
    '''
        return j in self.seznam_sousedu[i]

    def k(self, u):
    '''
    účel: vypsání všech sousedů vrcholu
    význam parametrů: číslo vrcholu, u kterého chcem zjistit všechny sousedy
    navrátová hodnota: None, pouze tiskne
    '''
        for v in self.seznam_sousedu[u]:
            print(v)

    def s(self):
    '''
    účel: vytvoření seznamu všech orientovaných hran grafu, tj. všech dvojic které jsou sousední, kde záleží na pořadí
    význam parametrů: nejsou
    navrátová hodnota: list, seznam všech hran grafu
    '''
        hrany = []

        for u in range(self.n):
            for v in self.seznam_sousedu[u]:
                hrany.append((u, v))

        return hrany

    def ms(self):
    '''
    účel: zjištění všech vrcholů s maximálním počtem sousedů
    význam parametrů: nejsou
    navrátová hodnota: list, seznam všech vrcholů s max. počtem sousedů
    '''
        pm = max(len(self.seznam_sousedu[u]) for u in range(self.n))
        return [u for u in range(self.n) if len(self.seznam_sousedu[u]) == pm]

    def eo(self):
    '''
    účel: zjištění zda jsou všechny hrany "oboustranné" - jestli v, soused u, má za souseda u - tedy jestli je graf neorientovaný
    význam parametrů: nejsou
    navrátová hodnota: Bool, podle toho zda je graf neorientovaný (True), nebo orientovaný (False)
    '''
        for u in range(self.n):
            for v in self.seznam_sousedu[u]:
                if u not in self.seznam_sousedu[v]:
                    return False
        return True

    def mp(self):
    '''
    účel: zjištění vrcholů, které nejsou sousedy žádných jiných vrcholů (odlišné od první "sousedské" funkce mn)
    význam parametrů: nejsou
    navrátová hodnota: list, seznam všech vrcholů, které nejsou sousedy
    '''
        vstupni = [0]*self.n
        for u in range(self.n):
            for v in self.seznam_sousedu[u]:
                vstupni[v] += 1
        return [i for i in range(self.n) if vstupni[i] == 0]

    def r(self):
    '''
    účel: vytvoření grafu s "překlopenou orientací" - pokud v byl soused u, nyní u bude soused v
    význam parametrů: nejsou
    navrátová hodnota: Graf, nový "překlopený" graf
    '''
        novy = GrafSS(self.n)
        for u in range(self.n):
            for v in self.seznam_sousedu[u]:
                novy.pridej_hranu(v,u)
        return novy

'''
chyby a omezení: 
    ve funkci r "GrafSS" není definováno, má být asi "Graf"
    metody s číslem vrcholu na vstupu nekontrolují, jestli číslo vrcholu existuje
    metoda pro přidání hrany nekontroluje, jestli už hrana neexistuje
'''


