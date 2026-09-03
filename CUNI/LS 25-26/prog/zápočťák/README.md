#Evidence trvanlivosti

##Popis programu
Evidence trvanlivosti je program určený k evidenci zásob potravin v domácnosti (lednice, mrazák, spíž) a jejich data minimální trvanlivosti. Program automaticky hlídá data minimální trvanlivosti (popř. manuálně nastavenou lhůtu pro věci typu ovoce, zelenina, ...) a uživateli pošle e-mail, když má nějaká potravina projít.

##Funkcionality

###Databáze
Program má databázi potravin v domě. Uživatel může přidávat a odebírat položky. Každá položka obsahuje název (např. Primátor, mleté vepřové, mrkev, ...), datum minimální trvanlivosti (popř. manuální lhůtu) **ve formátu YYYY/MM/DD**, počet a kategorii (plátkový sýr, maso, zelenina, ...).

###Systém upozornění
Při nastavení pomocí služby 'cron' se program automaticky spustí a při blížící se lhůtě pošle e-mail na zadanou adresu.

###Obrazovky

####Hlavní okno
V pravé části okna je tabulka zobrazující všechny potraviny v evidenci, t.ž. v řádku je jedna položka, která má ve sloupcích vypsané všechny své hodnoty (název, datum, počet, kategorie). V levé části tlačítko 'Přidat', které vede na okno pro přidání potraviny, tlačítko 'Odstranit', které vede na okno pro odstranění potraviny a tlačítko 'Uložit a ukončit', kterým se tabulka přepíše do souboru s databází a program se ukončí, jindy se změny do souboru databáze **neukládají**.

#### Okno pro přidání potraviny
Okno s políčky pro název, datum, počet a kategorii a tlačítkem pro potvrzení přidání potraviny do evidence. Tlačítkem 'Potvrdit' se přídá položka do tabulky, tlačítkem 'Zrušit' se program vrátí na hlavní okno.

#### Okno pro odstranění potraviny
Okno s políčkem pro číslo potraviny, kterou chce uživatel odstranit. Tlačítkem 'Potvrdit' se daná položka odstraní, tlačítkem 'Zrušit' se program vrátí na hlavní okno.

##Návody

###Před spuštěním
Na zařízení je potřeba nainstalovaný Python, knihovny tkinter, date, datetime, smtplib a email. Před prvním spuštění je potřeba nastavit v souboru 'kontrola_lhut.py' e-mailový server a počet zbývajících dnů při zaslání upozornění pro účely funkcionality zasílání e-mailů, konkrétně proměnné, jejichž názvy jsou velkými písmeny.

###Spuštění
Program se spouští v konzoli pomocí příkazu 'python3 main.py \[soubor\]', kde \[soubor\] je třeba nahradit relativní cestou k souboru databáze.
