# Evidence trvanlivosti – programátorská dokumentace

---

## Popis programu

Evidence trvanlivosti je program určený k evidenci zásob potravin v domácnosti (lednice, mrazák, spíž) a jejich data minimální trvanlivosti. Program automaticky hlídá data minimální trvanlivosti (popř. manuálně nastavenou lhůtu pro věci typu ovoce, zelenina, ...) a uživateli pošle e-mail, když má nějaká potravina projít. Program má grafický režim pro úpravu databáze a režim bez grafiky pro automatizaci kontroly lhůt a rozesílání e-mailů.

Toto je programátorská dokumentace.

---

## Požadavky a knihovny

Program je napsán v Pythonu 3 a využivá knihovny `tkinter`, `argparse`, `smtplib`, `email`, `datetime` a `time`.

---

## Architektura

Program se skládá z hlavního soubor `evidence.py`, který volá funkce z ostatních souborů, dále ze tří souborů, `prace_s_databazi.py`, `delani_oken.py` a `kontrola_lhut.py`, s funkcemi rozřazenými podle toho, co dělají, a nakonec z pomocného skriptu `email_setup.py`, který slouží pro nastavení služby posílání e-mailů. Soubory se importují přes `from <soubor> import *`, takže jsou všechny funkce importovaného souboru dostupné přímo jménem. Dále se používají textové soubory `databaze.txt`, ve kterém se ukládá databáze, a `nastaveni_emailu.txt`, ve kterém se ukládá nastavení pro službu posílání e-mailů.

## Formáty dat

### Databáze v pracovní paměti

Databáze je uložena v proměnné `databaze`, která je seznam seznamů. Každý vnitřní seznam je jedna položka ve formátu `[id, název, datum, počet, kategorie]`, například `[1, "vysočina", "2026/12/31", "5", "salám"]`. `id` je int odpovídající pozici v seznamu + 1, slouží jako klíč pro odebírání v GUI. Po odebrání celé položky se přepočítává, aby mezi id položek nebyla mezera. Všechny hodnoty kromě `id` jsou uloženy jako řetězce, aritmetika s `počet` se provádí přes `int()`.

### Formát souboru `databaze.txt`

Do progamu se načítají pouze řádky začínající `@`, řádky jsou obdobně jako v `databaze` ve formátu `@, název, datum, počet, kategorie`. Oddělovačem je čárka, po načtení se provede `.strip()`. `id` se v souboru neukládá, generuje se z pozice (protože se mění při odebrání celé položky). Řádky nezačínající `@` jsou při načítání ignorovány, ale při zápisu zachovány -- slouží jako komentáře.

### Formát souboru `nastaveni_emailu.txt`

Soubor po nastavení obsahuje 7 řádků začínajících `@`, v pořadí: SMTP server; port; uživatelské jméno; heslo; e-mail odesílatele; e-mail/y příjemce/příjemců; počet dní před lhůtou, kdy se zašle e-mail. Do paměti se načítá jako seznam seznamů v proměnné `nastaveni`. Políčko `nastaveni[5]` (e-mail/y příjemce/příjemců) je seznam zadaných e-mailových adres, ostatní políčka jsou jednoprvkové seznamy přístupné přes `[0]`.

---

## Soubor `prace_s_databazi.py`

Soubor načítá databázi ze souboru, validuje uživatelské vstupy při změnách databáze a při ukončení ukládá databázi zpět do souboru.

### Funkce `prectiDatabazi(args)`

Otevře soubor `databaze.txt` (popř. `args.soubor`), přečte řádky a pro každý řádek provede `split(",")`. Pokud řádek začíná znakem `@`, odstraní tento znak a zbytek připojí do `databaze`. Po načtení všech řádků každému přiřadí podle pořadí v `databaze` jeho `id` na index 0 (o jedno větší, aby se začínalo jedničkou) a provede `.strip()` na zbylé položky. Vrací `databaze`.

### Funkce `ulozDatabazi(args, databaze)`

Přečte původní soubor databáze a do `vystup` zkopíruje řádky nezačínající `@`. Ke `vystup` připojí formátované položky z `databaze` ve tvaru `@, název, datum, počet, kategorie\n`. Soubor přemaže a zapíše do souboru `vystup`. `id` se neukládá.

### Funkce `dataValidacePridat(jmeno, datum, pocet, kategorie)`

Vrací `True`, pokud je `jmeno` neprázdné a ne-číselné, `datum` lze rozdělit na 3 číselné části délek 4/2/2 s rokem > 1999, měsícem < 13 a dnem < 32, `pocet` je neprázdné číslo a `kategorie` je neprázdná a ne-číselná. Jinak vrací `False`.

### Funkce `dataValidaceOdebrat(databaze, polozka, pocet)`

Vrací `True`, pokud je `polozka` neprázdné číslo menší nebo rovno poslednímu `id` v databázi (proto se `id` přepočítavají, aby v nich nebyla mezera) a `pocet` je neprázdné číslo menší nebo rovno aktuálnímu počtu dané položky. Jinak vrací `False`.

---

## Soubor `delani_oken.py`

Soubor který vytváří veškerá grafická rozhraní programu.

### Funkce `udelejOknoHlavni(args, databaze)`

Vytvoří hlavní okno s tabulkou `ttk.Treeview` a tlačítky `Přidat`, `Odebrat` a `Uložit a ukončit`. Tabulka má sloupce pro kategorii (stromový rodič), `id`, název, datum a počet. Položky se seskupují podle kategorie, pro každou kategorii se vytvoří rodičovský uzel a do něj se vloží příslušné položky. Řádky se střídavě barví bíle a šedě pomocí tagů `sudé` a `liché`.

### Funkce `udelejOknoPridat(args, databaze, okno_hlavni)`

Zavře hlavní okno a vytvoří formulář s políčky pro název, datum, počet a kategorii. Tlačítkem `Potvrdit` nebo klávesou `Enter` se validuje přes `dataValidacePridat` a při úspěchu připojí položku `[len(databaze) + 1, jmeno, datum, pocet, kategorie]` do `databaze` a vrátí se do hlavního okna. Tlačítkem `Zrušit` nebo klávesou `Escape` se vrátí beze změn. Do hlavního okna se vrací pomocí funkce `zrusitOknoPridat`.

### Funkce `udelejOknoOdebrat(args, databaze, okno_hlavni)`

Zavře hlavní okno a vytvoří formulář s políčky pro `id` potraviny a počet kusů k odebrání. Tlačítkem `Potvrdit` nebo klávesou `Enter` se validuje přes `dataValidaceOdebrat`. Pokud odebíraný počet odpovídá aktuálnímu počtu položky, tj. odeberou se všechny položky, položka se odstraní (`databaze.pop`) a `id` všech položek se přepočítá. Jinak se počet kusů u položky jen sníží o zadaný počet. Poté se program vrátí do hlavního okna. Tlačítkem `Zrušit` nebo klávesou `Escape` se vrátí beze změn. Do hlavního okna se vrací pomocí funkce `zrusitOknoOdebrat`.

### Funkce `zrusitOknoPridat` / `zrusitOknoOdebrat`

Zavolají `destroy()` na aktuální okno a `udelejOknoHlavni(args, databaze)`. Slouží jako návrat do hlavního okna.

### Funkce `udelejOknoUpozorneni()`

Vytvoří okno s textem `Špatný formát vstupu.` a tlačítkem `Zavřít`. Volá se, když validace selže, tj. `dataValidacePridat` nebo `dataValidaceOdebrat` vrátí `False`.

### Funkce `ukonciProgram(args, databaze, okno_hlavni)`

Zavolá `ulozDatabazi(args, databaze)` a `okno_hlavni.destroy()`.

---

## Soubor `kontrola_lhut.py`

Soubor který kontroluje lhůty a rozesílá e-maily.

### Funkce `posliEmail(subject, body, nastaveni)`

Rozbalí konfiguraci z `nastaveni[0]` až `nastaveni[5]`, vytvoří `MIMEText(body)` s hlavičkami `Subject`, `From` a `To` a odešle e-mail přes `smtplib.SMTP` voláním `starttls()`, `login()` a `sendmail()`.

### Funkce `kontrolaLhut(databaze)`

Otevře soubor `nastaveni_emailu.txt` (pevná cesta), naparsuje obdobně jako funkce `prectiDatabazi` řádky začínající `@` do `nastaveni` a přečte `DAYS_IN_ADVANCE` z `nastaveni[6][0]`. Pro každou položku databáze porovná rozdíl mezi datem položky a dnešním datem s `timedelta(days=DAYS_IN_ADVANCE)`. Pokud se rovnají, odešle e-mail s upozorněním. Při úspěšném odeslání e-mailu funkce vypíše do terminálu zprávu.

---

## Skript `email_setup.py`

Interaktivní konzolový skript bez argumentů. Přečte existující `nastaveni_emailu.txt` a do `vystup` zkopíruje řádky nezačínající `@`. Poté vyzve uživatele k zadání 7 hodnot, v pořadí: SMTP server; port; uživatelské jméno; heslo; e-mail odesílatele; e-mail/y příjemce/příjemců; počet dní před lhůtou, kdy se zašle e-mail; každou validuje, aby byla neprázdná (u čísla portu a počtu dní navíc aby byly číselné) a připojí k proměnné `vystup` ve formátu `@, <hodnota>\n`. Nakonec soubor `nastaveni_emailu.txt` přemaže a zapíše do něj `vystup`.

---

Jan Romanovský, 2026
