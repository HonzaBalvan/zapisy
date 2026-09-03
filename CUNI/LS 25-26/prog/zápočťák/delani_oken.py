import tkinter as tk
from tkinter import ttk

from prace_s_databazi import *

def udelejOknoHlavni(args, databaze):
    """OKNA"""
    okno_hlavni = tk.Tk()
    okno_hlavni.title("Evidence – Hlavní okno")
    okno_hlavni.configure(bg = "grey80")

    ramcovy_frame = tk.Frame(okno_hlavni)

    frame_tabulky = tk.Frame(ramcovy_frame)

    lista_tlacitek = tk.Frame(ramcovy_frame, width = 100, height = 300)
    
    """TLAČÍTKA"""
    tlacitko_pridat = tk.Button(lista_tlacitek, text = "Přidat", command = lambda:udelejOknoPridat(args, databaze, okno_hlavni))

    tlacitko_odebrat = tk.Button(lista_tlacitek, text = "Odebrat", command = lambda:udelejOknoOdebrat(args, databaze, okno_hlavni))

    tlacitko_ukoncit = tk.Button(lista_tlacitek, text = "Uložit a ukončit", command = lambda:ukonciProgram(args, databaze, okno_hlavni))

    """TABULKA"""
    tabulka = ttk.Treeview(frame_tabulky)

    scrollbar_svisly = ttk.Scrollbar(frame_tabulky, orient ="vertical", command = tabulka.yview)
    tabulka.configure(xscrollcommand = scrollbar_svisly.set)

    tabulka["columns"] = ("#", "Jméno", "Datum", "Počet")

    tabulka.column("#0", width = 100, anchor = tk.W)
    tabulka.column("#", width = 30, anchor = tk.W)
    tabulka.column("Jméno", anchor = tk.W)
    tabulka.column("Datum", width = 100, anchor = tk.W)
    tabulka.column("Počet", width = 50, anchor = tk.W)

    tabulka.heading("#0", text = "Kategorie", anchor = tk.W)
    tabulka.heading("#", text = "#", anchor = tk.W)
    tabulka.heading("Jméno", text = "Jméno", anchor = tk.W)
    tabulka.heading("Datum", text = "Datum", anchor = tk.W)
    tabulka.heading("Počet", text = "Počet", anchor = tk.W)

    tabulka.tag_configure("liché", background="#E8E8E8")
    tabulka.tag_configure("sudé", background="#FFFFFF")

    pocitadlo_tagu = 0
    def udelejTag():
        nonlocal pocitadlo_tagu

        if pocitadlo_tagu % 2 == 0:
            pocitadlo_tagu += 1
            return "sudé"
        else:
            pocitadlo_tagu += 1
            return "liché"

    list_kategorii = []
    for polozka in databaze:
        list_kategorii.append(polozka[4])
    mnozina_kategorii = sorted(set(list_kategorii))

    for kategorie in mnozina_kategorii:
        level_kategorie = tabulka.insert(parent="", index=tk.END, text = kategorie, open=True, tags = (udelejTag(),))

        for polozka in databaze:
            if polozka[4] == kategorie:
                tabulka.insert(parent=level_kategorie, index=tk.END, values=polozka[:4], tags=(udelejTag(),))

    """ZOBRAZENÍ"""
    ramcovy_frame.pack(side = "top", expand=True, fill=tk.BOTH, padx = 10, pady = 10)

    lista_tlacitek.pack(side = "left", padx = (10, 0), pady = 10)

    tlacitko_pridat.pack(expand=True, fill=tk.BOTH, side = "top")
    tlacitko_odebrat.pack(expand=True, fill=tk.BOTH, side = "top")
    tlacitko_ukoncit.pack(expand=True, fill=tk.BOTH, side = "bottom")

    frame_tabulky.pack(side = "right", expand=True, fill=tk.BOTH, anchor = tk.NE, padx = 10, pady = 10)

    tabulka.pack(side = "left", expand=True, fill=tk.BOTH)

    scrollbar_svisly.pack(side ='right', anchor = tk.W, fill ="y")

    okno_hlavni.mainloop()

def udelejOknoPridat(args, databaze, okno_hlavni):
    okno_hlavni.destroy()

    okno_pridat = tk.Tk()
    okno_pridat.title("Evidence – Přidat položku")
    okno_pridat.configure(bg="grey80")

    frame_pridat = tk.Frame(okno_pridat)
    frame_pridat.pack(padx = 10, pady = 10)

    jmeno_label = tk.Label(frame_pridat, text = "Jméno")
    jmeno_label.grid(row = 0, column = 0, pady = (10, 0))

    datum_label = tk.Label(frame_pridat, text="Datum (YYYY/MM/DD)")
    datum_label.grid(row = 0, column = 1, pady = (10, 0))

    pocet_label = tk.Label(frame_pridat, text = "Počet")
    pocet_label.grid(row = 0, column = 2, pady = (10, 0))

    kategorie_label = tk.Label(frame_pridat,text="Kategorie")
    kategorie_label.grid(row = 0,column = 3, pady = (10, 0))

    jmeno_entry = tk.Entry(frame_pridat)
    jmeno_entry.grid(row = 1, column = 0, padx = (10, 0), pady = 10)

    datum_entry = tk.Entry(frame_pridat)
    datum_entry.grid(row = 1, column = 1, padx = (10, 0), pady = 10)

    pocet_entry = tk.Entry(frame_pridat)
    pocet_entry.grid(row = 1, column = 2, padx = (10, 0), pady = 10)

    kategorie_entry = tk.Entry(frame_pridat)
    kategorie_entry.grid(row = 1, column = 3, padx = 10, pady = 10)

    def udelejPridat(args, databaze):
        if dataValidacePridat(jmeno_entry.get(), datum_entry.get(), pocet_entry.get(), kategorie_entry.get()):
            databaze.append([len(databaze) + 1, jmeno_entry.get(), datum_entry.get(), pocet_entry.get(), kategorie_entry.get()])
            jmeno_entry.delete(0, tk.END)
            datum_entry.delete(0, tk.END)
            pocet_entry.delete(0, tk.END)
            kategorie_entry.delete(0, tk.END)
    
            zrusitOknoPridat(args, databaze, okno_pridat)
        else:
            udelejOknoUpozorneni()

    tlacitko_pridat = tk.Button(frame_pridat, text = "Potvrdit", command = lambda:udelejPridat(args, databaze))
    tlacitko_pridat.grid(row = 2, column = 1, pady = (0, 10))

    tlacitko_zrusit = tk.Button(frame_pridat, text = "Zrušit", command = lambda:zrusitOknoPridat(args, databaze, okno_pridat))
    tlacitko_zrusit.grid(row = 2, column = 2, pady = (0, 10))

    def stiskKlavesyPridat(udalost):
        nonlocal args, databaze, okno_pridat

        if udalost.keycode == 36: #klávesa Enter
            udelejPridat(args, databaze)
        if udalost.keycode == 9: #klávesa Escape
            zrusitOknoPridat(args, databaze, okno_pridat)

    okno_pridat.bind("<Key>", stiskKlavesyPridat)

def udelejOknoOdebrat(args, databaze, okno_hlavni):
    okno_hlavni.destroy()

    okno_odebrat = tk.Tk()
    okno_odebrat.title("Evidence – Odebrat položku")
    okno_odebrat.configure(bg="grey80")

    frame_odebrat = tk.Frame(okno_odebrat)
    frame_odebrat.pack(padx = 10, pady = 10)

    polozka_label = tk.Label(frame_odebrat, text = "Číslo položky, ze které chcete odebrat:")
    polozka_label.grid(row = 0, column = 0, padx = 10, pady = (10, 0))

    polozka_entry = tk.Entry(frame_odebrat)
    polozka_entry.grid(row = 0, column = 1, padx = (0, 10), pady = (10, 0))

    pocet_label = tk.Label(frame_odebrat, text = "Počet kusů položky k odebrání:")
    pocet_label.grid(row = 1, column = 0, padx = 10, pady = (10, 0))

    pocet_entry = tk.Entry(frame_odebrat)
    pocet_entry.grid(row = 1, column = 1, padx = (0, 10), pady = (10, 0))

    def udelejOdebrat(args, databaze):
        if dataValidaceOdebrat(databaze, polozka_entry.get(), pocet_entry.get()):
            if int(pocet_entry.get()) == int(databaze[int(polozka_entry.get()) - 1][3]):
                databaze.pop(int(polozka_entry.get()) - 1)
                polozka_entry.delete(0, tk.END)
                pocet_entry.delete(0, tk.END)

                for i in range(len(databaze)):
                    databaze[i][0] = i + 1
                    for j in range(1, len(databaze[i])):
                        databaze[i][j] = databaze[i][j].strip()
            else:
                databaze[int(polozka_entry.get()) - 1][3] = str(int(databaze[int(polozka_entry.get()) - 1][3]) - int(pocet_entry.get()))

            zrusitOknoOdebrat(args, databaze, okno_odebrat)
        else:
            udelejOknoUpozorneni()

    tlacitko_odebrat = tk.Button(frame_odebrat, text = "Potvrdit", command = lambda:udelejOdebrat(args, databaze))
    tlacitko_odebrat.grid(row = 2, column = 0, pady = 10)

    tlacitko_zrusit = tk.Button(frame_odebrat, text = "Zrušit", command = lambda:zrusitOknoOdebrat(args, databaze, okno_odebrat))
    tlacitko_zrusit.grid(row = 2, column = 1, pady = 10)

    def stiskKlavesyOdebrat(udalost):
        nonlocal args, databaze, okno_odebrat

        if udalost.keycode == 36: #klávesa Enter
            udelejOdebrat(args, databaze)
        if udalost.keycode == 9: #klávesa Escape
            zrusitOknoOdebrat(args, databaze, okno_odebrat)

    okno_odebrat.bind("<Key>", stiskKlavesyOdebrat)

def zrusitOknoPridat(args, databaze, okno_pridat):
    okno_pridat.destroy()
    udelejOknoHlavni(args, databaze)

def zrusitOknoOdebrat(args, databaze, okno_odebrat):
    okno_odebrat.destroy()
    udelejOknoHlavni(args, databaze)

def udelejOknoUpozorneni():
    okno_upozorneni = tk.Tk()
    okno_upozorneni.title("Evidence – Upozornění")

    upozorneni_label = tk.Label(okno_upozorneni, text = "Špatný formát vstupu.")
    upozorneni_label.grid(row = 0, column = 0, padx = 10, pady = 10)

    upozorneni_button = tk.Button(okno_upozorneni, text = "Zavřít", command = lambda:okno_upozorneni.destroy())
    upozorneni_button.grid(row = 1, column = 0, padx = 10, pady = (0, 10))

def ukonciProgram(args, databaze, okno_hlavni):
    ulozDatabazi(args, databaze)
    
    okno_hlavni.destroy()
