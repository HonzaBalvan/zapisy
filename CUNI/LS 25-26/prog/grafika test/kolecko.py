from tkinter import *

okno = Tk()

c = Canvas(okno, width = 500, height = 500, background = "gray")
c.pack()

kolecko = c.create_oval(220, 130, 280, 190, fill = "yellow")

def stisk_klavesy(udalost):
    print(udalost.char)
    if udalost.char == "a":
        c.move(kolecko, -10, 0)
    if udalost.char == "d":
        c.move(kolecko, 10, 0)
    if udalost.char == "s":
        c.move(kolecko, 0, 10)
    if udalost.char == "w":
        c.move(kolecko, 0, -10)

okno.bind("<Key>", stisk_klavesy)

okno.mainloop()
