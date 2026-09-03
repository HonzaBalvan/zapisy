#Evidence trvanlivosti

##Funkcionality -- Implementace

###Databáze
V době, kdy se program nepoužívá je databáze uložena v textovém souboru (zpravidla ve stejné složce). Přímo při spuštění programu se zadává cesta k tomuto souboru a ten je pomocí funkce 'prectiDatabazi' přečten, formátován a uložen do proměnné 'databaze' jako seznam seznamů, kde každá položka obsahuje id, jméno, datum (trvanlivosti), počet a kategorii. Tato proměnná ´databaze' je nadále používána po celou dobu běhu programu a při zavření okna tlačítkem 'Uložit a ukončit' je pomocí funkce 'ulozDatabazi' uložena do stejného souboru, ze kterého byla původně přečtena, a to se zachováním všech řádků, které nebyly ve správném formátu pro přečtení jakožto položek databáze (viz soubor databaze.txt).

###Systém upozornění
Po zavření hlavního okna se zavolá funkce 'kontrolaLhut', která pro každou položku zkontroluje, zda zbývá přesně 'DAYS\_IN\_ADVANCE' dní do uvedeného datumu a pokud ano, tak pošle e-mail za pomoci funkce 'posliEmail'.

###Obrazovky

####Hlavní okno
Hlavní okno tvoří funkce 'vytvorHlavniOkno' využívající knihovnu 'tkinter'. Sestavá z tabulky databáze, tvořené pomocí 'treeview' a tlačítek tvořených pomocí 'button'. Tyto prvky jsou zasazeny do prvků 'frame', aby měly vyžadované umístění. Pro zobrazení prvků se používá metoda 'pack'. Každé tlačítko má svou funkci, které jsou popsány níže.

####Okno pro přidání potraviny
Okno pro přidání potraviny tvoří funkce 'vytvorOknoInput' volaná tlačítkem 'Přidat' v hlavním okně. TODO

####Okno pro odstranění potraviny
Okno pro odstranění potraviny tvoří funkce 'vytvorOknoOdstranit' volaná tlačítkem 'Odstranit' v hlavním okně. TODO

##Návody

###Spuštění
Program se dá taktéž spustit ve složce z konzole jako './main.py \[soubor\]'
