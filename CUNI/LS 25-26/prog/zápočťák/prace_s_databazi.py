def prectiDatabazi(args):
    """
    otevře soubor databáze, do pracovní paměti programu do proměnné 'databaze' předá jen řádky začínající '@', a to jako seznamy [id, jméno, datum, počet, kategorie]
    """

    with open(args.soubor, encoding="utf-8") as vstup:
        vstup_radky = vstup.readlines()
        
        databaze = []

        for radek_vstupu in vstup_radky:
            radek_split = radek_vstupu.split(",")

            if radek_split[0] == "@": #kontrola formátu
                radek_split.pop(0)
                databaze.append(radek_split)

    for i in range(len(databaze)):
        databaze[i].insert(0, i + 1) #tady se vytváří id položky
        for j in range(1, len(databaze[i])):
            databaze[i][j] = databaze[i][j].strip()

    return databaze

def ulozDatabazi(args, databaze):
    """
    uloží pracovní databázi z proměnné 'databaze' přes formátování v proměnné 'vystup' zpět do souboru
    """

    vystup = []

    with open(args.soubor, encoding="utf-8") as soubor:
        soubor_radky = soubor.readlines()

        for radek_souboru in soubor_radky: #tady se do proměnné 'vystup' připíší všechny řádky, které NEzačínají '@'
            radek_split = radek_souboru.split(",")
            if radek_split[0] != "@":
                vystup.append(",".join(radek_split))

        for polozka in databaze: #tady se do proměnné výstup připíší položky z proměnné 'databaze'
            vystup.append(f"@, {polozka[1]}, {polozka[2]}, {polozka[3]}, {polozka[4]}\n")

    with open(args.soubor, "w", encoding="utf-8") as soubor: #tady se soubor vymaže
        soubor.write("")

    with open(args.soubor, "a", encoding="utf-8") as soubor: #tady se do souboru přepíše proměnná 'vystup'
        for radek in vystup:
            soubor.write(str(radek))

def dataValidacePridat(jmeno, datum, pocet, kategorie):
    """
    kontroluje správný formát položky, kterou se uživatel snaží přidat, tj. neprázdná pole, formát data, ...
    """

    """KONTROLA JMÉNA"""
    if len(jmeno) == 0:
        return False

    if jmeno.isnumeric():
        return False

    """KONTROLA DATA"""
    datum_split = datum.split("/")
        
    if len(datum_split) == 3:
        pass
    else:
        return False

    for kousek in datum_split:
        if kousek.isnumeric():
            pass
        else:
            return False

    if len(datum_split[0]) == 4 and len(datum_split[1]) == 2 and len(datum_split[2]) == 2:
        pass
    else:
        return False

    if int(datum_split[0]) > 1999 and int(datum_split[1]) < 13 and int(datum_split[2]) < 32:
        pass
    else:
        return False

    """KONTROLA POČTU"""
    if len(pocet) == 0:
        return False
    
    if pocet.isnumeric():
        pass
    else:
        return False

    """KONTROLA KATEGORIE"""
    if len(kategorie) == 0:
        return False
    
    if kategorie.isnumeric():
        return False

    return True

def dataValidaceOdebrat(databaze, polozka, pocet):
    """
    kontroluje správný formát čísla položky a počet položek, které se uživatel snaží odebrat, tj. neprázdný vstup a vstup v přípustném rozsahu
    """

    """POLOŽKA"""
    if len(polozka) == 0:
        return False    

    if polozka.isnumeric():
        pass
    else:
        return False

    if int(polozka) <= databaze[-1][0]:
        pass
    else:
        return False

    """POČET"""
    if len(pocet) == 0:
        return False

    if pocet.isnumeric():
        pass
    else:
        return False

    if int(pocet) <= int(databaze[int(polozka)-1][3]):
        pass
    else:
        return False
    
    return True
