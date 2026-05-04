import tkinter
from tkinter import messagebox

okno = tkinter.Tk()
okno.title('Ahoj')

def t1_klik(): 
    messagebox.showinfo("pomoc", "zakliknuto")
    t1.config(text = "kliknuto")

t1 = tkinter.Button(
        okno, text = "ahoj", 
        font = ("Helvetica", 16), 
        command = t1_klik
)

t1.pack()

okno.mainloop()
