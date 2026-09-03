import tkinter as tk
from tkinter import ttk

from prace_s_databazi import *

def udelejOknoHlavni(args, databaze):
    """OKNA"""
    okno_hlavni = tk.Tk()
    okno_hlavni.title("Evidence – Hlavní okno")
    okno_hlavni.configure(bg = "grey80")

    ramcovy_frame = tk.Frame(okno_hlavni)

    okno_tabulky = tk.Frame(ramcovy_frame)

    lista_tlacitek = tk.Frame(ramcovy_frame, width = 100, height = 300)
    
    """TLAČÍTKA"""
    tlacitko_pridat = tk.Button(lista_tlacitek, text = "Přidat", command = lambda:udelejOknoPridat(args, databaze, okno_hlavni))

    tlacitko_odstranit = tk.Button(lista_tlacitek, text = "Odstranit", command = lambda:udelejOknoOdstranit(args, databaze, okno_hlavni))

    tlacitko_ukoncit = tk.Button(lista_tlacitek, text = "Uložit a ukončit", command = lambda:ukonciProgram(args, databaze, okno_hlavni))

    """TABULKA"""
    tabulka = ttk.Treeview(okno_tabulky)

    tabulka["columns"] = ("#", "Jméno", "Datum", "Počet", "Kategorie")

    tabulka.column("#0", width = 0, stretch = tk.NO)
    tabulka.column("#", width = 30, anchor = tk.W)
    tabulka.column("Jméno", anchor = tk.W)
    tabulka.column("Datum", width = 100, anchor = tk.W)
    tabulka.column("Počet", width = 50, anchor = tk.W)
    tabulka.column("Kategorie", anchor = tk.W)

    tabulka.heading("#", text = "#", anchor = tk.W)
    tabulka.heading("Jméno", text = "Jméno", anchor = tk.W)
    tabulka.heading("Datum", text = "Datum", anchor = tk.W)
    tabulka.heading("Počet", text = "Počet", anchor = tk.W)
    tabulka.heading("Kategorie", text = "Kategorie", anchor = tk.W)

    tabulka.tag_configure("liché", background="#E8E8E8")
    tabulka.tag_configure("sudé", background="#FFFFFF")

    for i in range(len(databaze)):
        if i % 2 == 0:
            tabulka.insert(parent = "", index = i, values = databaze[i], tags = ("sudé",))
        else:
            tabulka.insert(parent = "", index = i, values = databaze[i], tags = ("liché",))

    """ZOBRAZENÍ"""
    ramcovy_frame.pack(side = "top", padx = 10, pady = 10)

    lista_tlacitek.pack(side = "left", padx = (10, 0), pady = 10)

    tlacitko_pridat.pack(expand=True, fill=tk.BOTH, side = "top")
    tlacitko_odstranit.pack(expand=True, fill=tk.BOTH, side = "top")
    tlacitko_ukoncit.pack(expand=True, fill=tk.BOTH, side = "bottom")

    okno_tabulky.pack(side = "right", anchor = tk.NE, padx = 10, pady = 10)

    tabulka.pack(expand=True, fill=tk.BOTH)

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

        print(udalost.char, udalost.keysym, udalost.keycode)
        if udalost.keycode == 36: #klávesa Enter
            udelejPridat(args, databaze)
        if udalost.keycode == 9: #klávesa Escape
            zrusitOknoPridat(args, databaze, okno_pridat)

    okno_pridat.bind("<Key>", stiskKlavesyPridat)

def udelejOknoOdstranit(args, databaze, okno_hlavni):
    okno_hlavni.destroy()

    okno_odstranit = tk.Tk()
    okno_odstranit.title("Evidence – Odstranit položku")
    okno_odstranit.configure(bg="grey80")

    frame_odstranit = tk.Frame(okno_odstranit)
    frame_odstranit.pack(padx = 10, pady = 10)

    cislo_label = tk.Label(frame_odstranit, text = "Číslo položky, kterou chcete odstranit:")
    cislo_label.grid(row = 0, column = 0, padx = 10, pady = (10, 0))

    cislo_entry = tk.Entry(frame_odstranit)
    cislo_entry.grid(row = 0, column = 1, padx = (0, 10), pady = (10, 0))

    def udelejOdstranit(args, databaze):
        if dataValidaceOdstranit(databaze, cislo_entry.get()):
            databaze.pop(int(cislo_entry.get()) - 1)
            cislo_entry.delete(0, tk.END)

            for i in range(len(databaze)):
                databaze[i][0] = i + 1
                for j in range(1, len(databaze[i])):
                    databaze[i][j] = databaze[i][j].strip()

            zrusitOknoOdstranit(args, databaze, okno_odstranit)
        else:
            udelejOknoUpozorneni()

    tlacitko_pridat = tk.Button(frame_odstranit, text = "Potvrdit", command = lambda:udelejOdstranit(args, databaze))
    tlacitko_pridat.grid(row = 2, column = 0, pady = 10)

    tlacitko_zrusit = tk.Button(frame_odstranit, text = "Zrušit", command = lambda:zrusitOknoOdstranit(args, databaze, okno_odstranit))
    tlacitko_zrusit.grid(row = 2, column = 1, pady = 10)

    def stiskKlavesyOdstranit(udalost):
        nonlocal args, databaze, okno_odstranit

        if udalost.keycode == 36: #klávesa Enter
            udelejOdstranit(args, databaze)
        if udalost.keycode == 9: #klávesa Escape
            zrusitOknoOdstranit(args, databaze, okno_odstranit)

    okno_odstranit.bind("<Key>", stiskKlavesyOdstranit)

def zrusitOknoPridat(args, databaze, okno_pridat):
    okno_pridat.destroy()
    udelejOknoHlavni(args, databaze)

def zrusitOknoOdstranit(args, databaze, okno_odstranit):
    okno_odstranit.destroy()
    udelejOknoHlavni(args, databaze)

def udelejOknoUpozorneni():
    okno_upozorneni = tk.Tk()
    okno_upozorneni.title("Evidence – Upozornění")

    upozorneni_label = tk.Label(okno_upozorneni, text = "Špatný formát vstupu.")
    upozorneni_label.grid(row = 0, column = 0)

    upozorneni_button = tk.Button(okno_upozorneni, text = "Zavřít", command = lambda:okno_upozorneni.destroy())
    upozorneni_button.grid(row = 1, column = 0)

def ukonciProgram(args, databaze, okno_hlavni):
    ulozDatabazi(args, databaze)
    
    okno_hlavni.destroy()
