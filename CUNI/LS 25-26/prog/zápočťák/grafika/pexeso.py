from tkinter import *

okno = Tk()

def klik(x):
    print(f"klik na tlacitko {x}")

POCET_DVOJIC = 5

for i in range(POCET_DVOJIC*2):
    b = Button(okno, text=i%POCET_DVOJIC, command = lambda x=i: klik(x))
    b.pack()

okno.mainloop()
