# Evidence trvanlivosti

---

## Popis programu

Evidence trvanlivosti je program určený k evidenci zásob potravin v domácnosti (lednice, mrazák, spíž) a jejich data minimální trvanlivosti. Program automaticky hlídá data minimální trvanlivosti (popř. manuálně nastavenou lhůtu pro věci typu ovoce, zelenina, ...) a uživateli pošle e-mail, když má nějaká potravina projít. Program má grafický režim pro úpravu databáze a režim bez grafiky pro automatizaci kontroly lhůt a rozesílání e-mailů.

---

## Požadavky

Na zařízení je potřeba nainstalovaný Python, knihovny 'tkinter', 'date', 'datetime', 'smtplib' a 'email'. Pro rozesílání e-mailů je taktéž potřeba připojení k internetu a e-mailová adresa s SMTP serverem (stačí např. Gmail nebo Seznam).

---

## Instalace a spuštění

### 1. Stažení souborů

Stáhněte si všechny soubory projektu do jedné složky.

### 2. První spuštění programu

Všechny další kroky předpokládají terminál spuštěný ve složce s projektem. Před prvním spuštěním je potřeba pro správné fungování rozesílání e-mailů tuto službu nastavit spuštěním souboru 'email_setup.py',

```bash
python3 email_setup.py
```

který vás nastavením interaktivně provede. Zde zadáte:

| Políčko | Popis | Příklad |
|---------|-------|---------|
| SMTP server | Adresa SMTP serveru vašeho e-mailového poskytovatele. | `smtp.gmail.com` (Gmail), `smtp.seznam.cz` (Seznam) |
| SMTP port | Port pro SMTP. | `587` |
| Uživatelské jméno | Vaše uživatelské jméno pro SMTP (většinou vaše e-mailová adresa). | `vas.email@gmail.com` |
| Heslo | Heslo pro SMTP server. | `••••••••` |
| Odesílatel | Vaše e-mailová adresa, ze které se budou odesílat upozornění. | `vas.email@gmail.com` |
| Příjemce | E-mailová adresa (nebo více adres oddělených čárkou), kam se mají odesílat upozornění. | `prijemce@seznam.cz, druhy.prijemce@email.cz` |
| Počet dní před lhůtou | Kolik dní před lhůtou se má odeslat upozornění. | `3` (odeslat e-mail 3 dny před lhůtou) |

> Poznámka pro Gmail:
> - Pokud používáte Gmail s dvoufázovým ověřením, budete muset vytvořit tzv. aplikační heslo (viz [návod od Google](https://support.google.com/accounts/answer/185833)).

### 3. Další spouštění

Je nekolik možností, jak program spustit.

#### Spuštění v grafickém režimu (výchozí):

```bash
python3 evidence.py
```

#### Spuštění bez grafického rozhraní (pouze kontrola lhůt):

```bash
python evidence.py --mode nogui
```

#### Použití jiného souboru databáze:

Ve výchozím nastavení se otevírá soubor 'databaze.txt', program ale umí i načítat z jiných souborů stejného formátu.

```bash
python evidence.py --soubor jina_databaze.txt
```

Nastavení lze samozřejmě kombinovat.

---

## Použití (Grafický režim – 'gui')

Po spuštění příkazem `python evidence.py` se otevře hlavní okno s tabulkou potravin z databáze.

### Hlavní okno

V pravé části okna je tabulka zobrazující všechny potraviny v evidenci, t.ž. v řádku je jedna položka, která má ve sloupcích vypsané své proměnlivé **id (sloupec '#')** pro účely odebírání a dále všechny své hodnoty (název, datum **ve formátu YYYY/MM/DD**, počet), položky jsou dále seskupené podle kategorie. V levé části tlačítko 'Přidat', které vede na okno pro přidání potraviny, tlačítko 'Odebrat', které vede na okno pro odebrání potraviny a tlačítko 'Uložit a ukončit', kterým se tabulka přepíše do souboru s databází a program se ukončí, jindy se změny do souboru databáze **neukládají**.

---

### Okno pro přidání potraviny

Okno s políčky pro název, datum, počet a kategorii a tlačítkem pro potvrzení přidání potraviny do evidence. **Zadávané datum musí být ve formátu YYYY/MM/DD.** Tlačítkem 'Potvrdit' nebo stisknutím klávesy 'Enter' se přídá položka do tabulky, tlačítkem 'Zrušit' nebo stisknutím klávesy 'Escape' se program vrátí beze změn na hlavní okno.

---

### Okno pro odebrání potraviny

Okno s políčky pro **id potraviny**, ze které chce uživatel odebírat a políčko pro počet kusů, které chce uživatel odebrat. Tlačítkem 'Potvrdit' nebo stisknutím klávesy 'Enter' se odebere daný počet dané položky z tabulky, v případě odebrání všech kusů se položka odstraní. Tlačítkem 'Zrušit' nebo stisknutím klávesy 'Escape' se program vrátí beze změn na hlavní okno.

---

## Použití (Bez grafického rozhraní – `nogui`)

Pokud spustíte program s parametrem `--mode nogui`, pouze se načte databáze, zkontrolují se lhůty a rozešlou se e-maily, tj. databázi nelze upravovat. Tento režim je vhodný pro automatické spouštění (např. přes `cron` na Linuxu nebo Plánovač úloh na Windows).

---

Jan Romanovský, 2026
