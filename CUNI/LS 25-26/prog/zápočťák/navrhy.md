### 3.1 `prectiDatabazi(args) -> list[list[str]]`

**⚠️ Známe omezení:** Neověřuje se, že řádek má ≥ 5 položek. Řádek s méně položkami vyvolá později `IndexError` při přístupu k `[4]` (kategorie). Viz sekce 7.

---

### 3.2 `ulozDatabazi(args, databaze)`

> ⚠️ Implementační detail: Soubor se maže zápisem `soubor.write("")` v režimu `"w"`, pak se zapisuje v `"a"`. Druhý krok je redundantní – lze psát přímo v `"w"`.

---

### 3.3 `dataValidacePridat(jmeno, datum, pocet, kategorie) -> bool`

> ⚠️ Validace data neověřuje skutečnou platnost kalendářního data (např. `2026/02/31` projde). Datum je čistě lexikální.

---

### 3.4 `dataValidaceOdebrat(databaze, polozka, pocet) -> bool`

> ⚠️ Známe omezení: Při **prázdné databázi** přístup `databaze[-1][0]` vyvolá `IndexError`. Viz sekce 7.

---

### 4.1 `udelejOknoHlavni(args, databaze)`

> ⚠️ Architektonická poznámka: Přepínání oken se děje přes `destroy()` aktuálního okna + vytvoření nového `tk.Tk()`. To je neobvyklý vzor – vytváří se více instancí `Tk`. Robustnější by bylo použití `Toplevel` nad jediným `Tk`. Viz sekce 7.

---

### 4.2 `udelejOknoPridat(args, databaze, okno_hlavni)`

> ⚠️ Detail: `databaze.append` vkládá **surové stringy z `Entry.get()`** (bez `.strip()`). Při ukládání se to srovná až v `ulozDatabazi` formátováním, ale v paměti mohou být hodnoty s mezerami. Porovnávání `int(...)` při odebírání to snese, ale je nekonzistentní.

---

### 4.3 `udelejOknoOdebrat(args, databaze, okno_hlavni)`

Formulář pro odebrání položky / snížení množství.

**Parametry:** stejné jako u Přidat.

**Pole:** `polozka` (id), `pocet` (kusů k odebrání).

**Akce (`udelejOdebrat`):**
1. Validace přes `dataValidaceOdebrat`.
2. Pokud `int(pocet) == int(databaze[id-1][3])` → `databaze.pop(id-1)` a **přepočítání id** (`databaze[i][0] = i+1`) + `.strip()` všech hodnot.
3. Jinak → `databaze[id-1][3] = str(int(...) - int(pocet))` (snížení množství).
4. `zrusitOknoOdebrat` → návrat do hlavního okna.

> ⚠️ Logika: `.strip()` se volá **jen při úplném smazání**, ne při částečném odebrání. To je asymetrie – při snížení množství zůstávají případné mezery v ostatních polích.

---

### 4.5 `udelejOknoUpozorneni()`

> ⚠️ Tato funkce vytváří **nový `tk.Tk()`** paralelně s existujícím oknem formuláře. V tkinteru se důrazně nedoporučuje mít dva `Tk()` instance – může způsobit zaseknutí zpracování událostí. Robustnější: `tk.messagebox.showerror`.

---

### 5.1 `posliEmail(subject, body, nastaveni)`

> ⚠️ `starttls()` je vždy voláno. Server bez TLS by selhal. Port 465 (implicitní SSL) není podporován – funguje jen STARTTLS na 587/25.

---

### 5.2 `kontrolaLhut(databaze)`

> ⚠️ Známe omezení: Pevná cesta `"nastaveni_emailu.txt"` – nelze přepnout přes `--soubor` (na rozdíl od databáze). Viz sekce 7.
> ⚠️ Porovnání je `== timedelta(days=DAYS_IN_ADVANCE)` – upozorní **pouze jednou**, v přesný den. Pokud program ten den neskončí, položka se už neohlásí. Lze zmírnit uložením "již upozorněno".

---

## 6. Skript: `email_setup.py`

> ⚠️ Neexistuje žádná kontrola formátu e-mailové adresy.

---

## 7. Známá omezení a doporučení pro údržbu

Tato sekce shrnuje technický dluh a místa, která je při rozšiřování třeba mít na paměti.

### 7.1 Rizika `IndexError`

1. **`prectiDatabazi`** – řádek s méně než 5 položkami po `@` se načte, ale pozdější přístup k `[4]` (kategorie, např. v GUI) vyvolá `IndexError`. Doporučení: `if radek_split[0] == "@" and len(radek_split) >= 5`.
2. **`dataValidaceOdebrat`** – prázdná databáze → `databaze[-1][0]` → `IndexError`. Doporučení: `if not databaze: return False`.
3. **`kontrolaLhut`** – méně než 7 řádků v `nastaveni_emailu.txt` → `nastaveni[6]` → `IndexError`. Doporučení: `if len(nastaveni) < 7: return`.

### 7.2 Architektura GUI

- Více `tk.Tk()` instancí při přepínání oken. Doporučeno: jeden `Tk()` + `Toplevel` pro podokna.
- `udelejOknoUpozorneni` vytváří `Tk()` paralelně. Doporučeno: `tk.messagebox.showerror("Špatný formát", "Špatný formát vstupu.")`.
- Vstupy z `Entry.get()` se ne `.strip()`-ou při přidávání. Doporučeno: `.strip()` v `udelejPridat`.

### 7.3 Konfigurace

- `kontrolaLhut` používá **pevnou cestu** `"nastaveni_emailu.txt"`. Pokud se přidává `--soubor` pro databázi, konzistentní by bylo přidat i `--email-config`.
- Žádná kontrola existence souboru `nastaveni_emailu.txt` – chybějící soubor → `FileNotFoundError`.

### 7.4 Logika lhůt

- Upozornění se posílá **jen v přesný den** rovnosti. Pokud program ztichne, položka propásne. Doporučeno: uložit do databáze flag `upozorneno` nebo porovnávat `<=` s kontrolou, zda již bylo odesláno.

### 7.5 Validace

- `dataValidacePridat` neověřuje kalendářní platnost data (`2026/02/31` projde). Lze použít `datetime.strptime(datum, "%Y/%m/%d")` s `try/except`.
- `email_setup.py` nevaliduje formát e-mailové adresy.

### 7.6 Bezpečnost

- Heslo SMTP je v `nastaveni_emailu.txt` **v čitelné podobě**. Pro shipping zvaž:
  - `.gitignore` pro `nastaveni_emailu.txt` a `databaze.txt`.
  - Ukládání hesla přes `keyring` nebo environment variable.
  - Podpora OAuth2 / aplikáčních hesel (zejména pro Gmail).

### 7.7 I/O detaily

- `ulozDatabazi` i `email_setup.py` mažou soubor zápisem `""` v `"w"` a pak zapisují v `"a"`. Druhý krok je redundantní – lze psát přímo v `"w"`.

---

## 8. Extension points

Pokud chceš program rozšířit, doporučené body zásahu:

| Cílová funkce | Co přidat |
|---------------|-----------|
| `dataValidacePridat` | Ověření kalendářního data přes `datetime.strptime`. |
| `prectiDatabazi` | Kontrola délky řádku + skip/log chybných řádků. |
| `udelejOknoHlavni` | Přidat sloupec "Zbývá dní" vypočítaný z `datum`. |
| `kontrolaLhut` | Parametrizovat cestu k e-mailovému configu přes `args`. |
| `evidence.py` | Přidat `--email-config` argument a předat do `kontrolaLhut`. |
| Nový modul | Export databáze do CSV/JSON – znovupoužití `prectiDatabazi`. |
| `delani_oken.py` | Nahradit `tk.Tk()` v podoknech za `Toplevel`. |
| `ulozDatabazi` | Volat při každé změně databáze, aby se ukládala automaticky
| všude | Přidat typecasting u funkcí nebo jak se to jmenuje type hint
