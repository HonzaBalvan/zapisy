import tkinter as tk
from tkinter import ttk

from prace_s_databazi import *

def udelejOknoHlavni(args, databaze):
    global okno_cele

    okno_cele = tk.Tk()
    okno_cele.geometry("800x600")
    okno_cele.title("Evidence – Hlavní okno")
    okno_cele.configure(bg="grey80")

    ramcovy_frame = tk.Frame(okno_cele)

    okno_tabulky = tk.Frame(ramcovy_frame)

    lista_tlacitek = tk.Frame(ramcovy_frame, width = 100, height = 300)

    tlacitko_pridat = tk.Button(lista_tlacitek, text = "Přidat", command = lambda:udelejOknoPridat(args, databaze))

    tlacitko_odstranit = tk.Button(lista_tlacitek, text = "Odstranit", command = lambda:udelejOknoOdstranit(args, databaze))

    tlacitko_ukoncit = tk.Button(lista_tlacitek, text = "Uložit a ukončit", command = lambda:ukonciProgram(args, databaze))

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

    ramcovy_frame.pack(side = "top")

    lista_tlacitek.pack(side = "left")

    tlacitko_pridat.pack(expand=True, fill=tk.BOTH, side = "top")
    tlacitko_odstranit.pack(expand=True, fill=tk.BOTH, side = "top")
    tlacitko_ukoncit.pack(expand=True, fill=tk.BOTH, side = "bottom")

    okno_tabulky.pack(side = "right", anchor = tk.NE)

    tabulka.pack(expand=True, fill=tk.BOTH)

    okno_cele.mainloop()

def udelejOknoPridat(args, databaze):
    global okno_cele

    okno_cele.destroy()
    okno_cele = tk.Tk()
    okno_cele.geometry("800x600")
    okno_cele.title = ("Evidence – Přidat položku")
    okno_cele.configure(bg="grey80")

    frame_input = tk.Frame(okno_cele)
    frame_input.pack()

    jmeno_label = tk.Label(frame_input, text = "Jméno")
    jmeno_label.grid(row = 0, column = 0)

    datum_label = tk.Label(frame_input, text="Datum (YYYY/MM/DD)")
    datum_label.grid(row = 0, column = 1)

    pocet_label = tk.Label(frame_input, text = "Počet")
    pocet_label.grid(row = 0, column = 2)

    kategorie_label = tk.Label(frame_input,text="Kategorie")
    kategorie_label.grid(row=0,column=3)

    jmeno_entry = tk.Entry(frame_input)
    jmeno_entry.grid(row = 1, column = 0)

    datum_entry = tk.Entry(frame_input)
    datum_entry.grid(row = 1, column = 1)

    pocet_entry = tk.Entry(frame_input)
    pocet_entry.grid(row = 1, column = 2)

    kategorie_entry = tk.Entry(frame_input)
    kategorie_entry.grid(row = 1, column = 3)

    def udelejInput(args, databaze):
        if dataValidacePridat(jmeno_entry.get(), datum_entry.get(), pocet_entry.get(), kategorie_entry.get()):
            databaze.append([len(databaze) + 1, jmeno_entry.get(), datum_entry.get(), pocet_entry.get(), kategorie_entry.get()])
            jmeno_entry.delete(0, tk.END)
            datum_entry.delete(0, tk.END)
            pocet_entry.delete(0, tk.END)
            kategorie_entry.delete(0, tk.END)
    
            zrusitOkno(args, databaze)
        else:
            udelejOknoUpozorneni()

    tlacitko_input = tk.Button(frame_input, text = "Potvrdit", command = lambda:udelejInput(args, databaze))
    tlacitko_input.grid(row = 2, column = 1)

    tlacitko_zrusit = tk.Button(frame_input, text = "Zrušit", command = lambda:zrusitOkno(args, databaze))
    tlacitko_zrusit.grid(row = 2, column = 2)

def udelejOknoOdstranit(args, databaze):
    global okno_cele

    okno_cele.destroy()
    okno_cele = tk.Tk()
    okno_cele.geometry("800x600")
    okno_cele.title = ("Evidence – Odstranit položku")
    okno_cele.configure(bg="grey80")

    frame_odstranit = tk.Frame(okno_cele)
    frame_odstranit.pack()

    cislo_label = tk.Label(frame_odstranit, text = "Číslo položky, kterou chcete odstranit:")
    cislo_label.grid(row = 0, column = 0)

    cislo_entry = tk.Entry(frame_odstranit)
    cislo_entry.grid(row = 0, column = 1)

    def udelejOdstranit(args, databaze):
        if dataValidaceOdstranit(databaze, cislo_entry.get()):
            databaze.pop(int(cislo_entry.get()) - 1)
            cislo_entry.delete(0, tk.END)

            for i in range(len(databaze)):
                databaze[i][0] = i + 1
                for j in range(1, len(databaze[i])):
                    databaze[i][j] = databaze[i][j].strip()

            zrusitOkno(args, databaze)
        else:
            udelejOknoUpozorneni()

    tlacitko_input = tk.Button(frame_odstranit, text = "Potvrdit", command = lambda:udelejOdstranit(args, databaze))
    tlacitko_input.grid(row = 2, column = 0)

    tlacitko_zrusit = tk.Button(frame_odstranit, text = "Zrušit", command = lambda:zrusitOkno(args, databaze))
    tlacitko_zrusit.grid(row = 2, column = 1)

def zrusitOkno(args, databaze):
    okno_cele.destroy()
    udelejOknoHlavni(args, databaze)

def udelejOknoUpozorneni():
    okno_upozorneni = tk.Tk()
    okno_upozorneni.title("Evidence – Upozornění")

    upozorneni_label = tk.Label(okno_upozorneni, text = "Špatný formát vstupu.")
    upozorneni_label.grid(row = 0, column = 0)

    upozorneni_button = tk.Button(okno_upozorneni, text = "Zavřít", command = lambda:okno_upozorneni.destroy())
    upozorneni_button.grid(row = 1, column = 0)

def ukonciProgram(args, databaze):
    ulozDatabazi(args, databaze)
    
    okno_cele.destroy()
