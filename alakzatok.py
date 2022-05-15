# Import

import main

# Formák 

    # Háromszög
from tkinter import *

def felszin():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        if felszin < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title("A Háromszög felszíne")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        if terfogat < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title("A háromszög térfogata")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")

    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

foablak = Tk()
foablak.title("A háromszög adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)



menu2 = Menubutton(menusor, text = "háromszög", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
teglatest.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu2.config(menu = teglatest)

foablak.mainloop()

    # Trapéz-------------------------------------------------------------------------
    
def felszin():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        if felszin < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title("A trapéz felszíine")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        if terfogat < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title("A trapéz térfogata")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")

    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

foablak = Tk()
foablak.title("A trapéz adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)



menu2 = Menubutton(menusor, text = "Trapéz", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
teglatest.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu2.config(menu = teglatest)

foablak.mainloop()


    # Paralelogramma-------------------------------------------------------------------------

def felszin():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        if felszin < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title("A paralelogramma felszíine")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        if terfogat < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title("A paralelogramma térfogata")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")

    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

foablak = Tk()
foablak.title("A paralelogramma adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)



menu2 = Menubutton(menusor, text = "Paralelogramma", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
teglatest.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu2.config(menu = teglatest)

foablak.mainloop()

    # Téglalap-------------------------------------------------------------------------

def felszin():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        if felszin < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title("A téglalap felszíine")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        if terfogat < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title("A téglalap térfogata")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")

    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

foablak = Tk()
foablak.title("A téglalap adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)



menu2 = Menubutton(menusor, text = "Téglalap", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
teglatest.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu2.config(menu = teglatest)

foablak.mainloop()

    # Deltoid-------------------------------------------------------------------------

def felszin():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        if felszin < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title("A deltoid felszíine")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        if terfogat < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title("A deltoid térfogata")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")

    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

foablak = Tk()
foablak.title("A deltoid adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)



menu2 = Menubutton(menusor, text = "Deltoid", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
teglatest.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu2.config(menu = teglatest)

foablak.mainloop()

    # Rombusz-------------------------------------------------------------------------

def felszin():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        if felszin < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title("A rombusz felszíne")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        if terfogat < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title("A rombusz térfogata")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")

    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

foablak = Tk()
foablak.title("A rombusz adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)



menu2 = Menubutton(menusor, text = "Rombusz", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
teglatest.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu2.config(menu = teglatest)

foablak.mainloop()

    # Négyzet-------------------------------------------------------------------------

def felszin():
    def szamit():
        a = eval(mezo1.get())
        felszin = a*a
        if felszin < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title("A négyzet felszíine")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        terfogat = 2*(a*a)
        if terfogat < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title("A négyzet térfogata")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg4 = Label(abl3, text = "Eredmény:")

    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

foablak = Tk()
foablak.title("A négyzet adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)



menu2 = Menubutton(menusor, text = "Négyzet", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
teglatest.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu2.config(menu = teglatest)

foablak.mainloop()

    # Kör-------------------------------------------------------------------------

def felszin():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        if felszin < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title("A Kör felszíine")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        if terfogat < 0:
            mezo4.delete(0, END)
            mezo4.insert(0, str("Nincs eredmény"))
        else:
            mezo4.delete(0, END)
            mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title("A Kör térfogata")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")

    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

foablak = Tk()
foablak.title("A Kör adatai")
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)



menu2 = Menubutton(menusor, text = "kör", underline = 0)
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = "Felszín", command = felszin, underline = 0)
teglatest.add_command(label = "Térfogat", command = terfogat, underline = 0)
teglatest.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu2.config(menu = teglatest)

foablak.mainloop()