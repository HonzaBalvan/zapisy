class Prvek:
    def __init__(self, x, dalsi):
        self.x = x
        self.dalsi = dalsi

def VytiskniLSS( p ):
    print( "LSS:", end=" " )
    while p!=None:
        print( p.x, end=" " )
        p = p.dalsi
    print(".")

def NactiLSS():
    """cte cisla z radku, dokud nenacte prazdny radek"""
    prvni = None
    posledni = None
    r = input()
    while r!="":
        radek = r.split()
        if len(radek)==0: # protoze ten test r!="" v RCDX neukoncil cyklus!
            break
        for s in radek:
            p = Prvek(int(s),None)
            if prvni==None:
                prvni = p
            else:
                posledni.dalsi = p
            posledni = p
        r = input()
    return prvni

#################################################

def UnionDestruct(a,b):
    """ destruktivni sjednoceni dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """

    if a.x < b.x:
        prvni = a
    elif b.x < a.x:
        prvni = b    

    while a.dalsi != None and b.dalsi != None:
        if a.x < b.x:
            if b.x < a.dalsi.x:
                tmp = a.dalsi
                tmp2 = b.dalsi
                a.dalsi = b
                b.dalsi = tmp
                b = tmp2

                a = a.dalsi
                
            elif b.x > a.dalsi.x:
                tmp = a.dalsi.dalsi
                a.dalsi.dalsi = b
                b = tmp

                a = a.dalsi
                
            else: # b.x == a.dalsi.x
                b = b.dalsi                

                a = a.dalsi

        elif b.x < a.x:
            if a.x < b.dalsi.x:
                tmp = b.dalsi
                tmp2 = a.dalsi
                b.dalsi = a
                a.dalsi = tmp
                a = tmp2

                b = b.dalsi

            elif a.x > b.dalsi.x:
                tmp = b.dalsi.dalsi
                b.dalsi.dalsi = a
                a = tmp

                b = b.dalsi

            else: #a.x == b.dalsi.x
                a = a.dalsi

                b = b.dalsi

        else: # a.x == b.x
            b = b.dalsi

    if a.dalsi == None:
            if a.x < b.x:
                a.dalsi = b

            elif b.x < a.x:
                    if a.x < b.dalsi:
                        AAAAAA

                    elif a.x > b.dalsi:
                        a.dalsi = b.dalsi
                        b.dalsi = a

                    else #a.x == b.dalsi:
                        AAAAAAA

            else: #b.x == a.x
                a.dalsi = b.dalsi

    if b.dalsi == None:
            AAAAAA

    print(a.x)
    print(a.dalsi)
    print(b.x)
    print(b.dalsi)
    return prvni

#################################################

VytiskniLSS( UnionDestruct( NactiLSS(), NactiLSS() ) )
