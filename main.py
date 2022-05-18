# Import

import sys
import alakzatok
import ablakok
from tkinter import * 

# Foablak

foablak = Tk()
foablak.title("Síkidomok területe és kerülete")
foablak.minsize(width = 500, height = 250)

# Menu

    # Menüsor
menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)

    # Első menü

    # Második menü

def ablak_harom():
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

def ablak_harom_masodik():
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

menu_two = Menubutton(menusor, text = "Háromszög", underline = 0)
menu_two.pack(side = LEFT)

haromszog = Menu(menu_two)
haromszog.add_command(label = "Felszín", underline = 0, command = felszin)
haromszog.add_command(label = "Térfogat", underline = 0, command = terfogat)
menu_two.config(menu = haromszog)


    # Harmadik Menü

def ablak_negy():
    abl4 = Toplevel(foablak)
    abl4.title("A trapéz felszíine")
    abl4.minsize(width = 300, height = 100)
    szoveg1 = Label(abl4, text = "a:")
    szoveg2 = Label(abl4, text = "b:")
    szoveg3 = Label(abl4, text = "c:")
    szoveg4 = Label(abl4, text = "Eredmény:")
    gomb1 = Button(abl4, text = "Számítás", command = szamit)
    mezo1 = Entry(abl4)
    mezo2 = Entry(abl4)
    mezo3 = Entry(abl4)
    mezo4 = Entry(abl4)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)

def ablak_negy_masodik():
    abl4 = Toplevel(foablak)
    abl4.title("A trapéz térfogata")
    abl4.minsize(width = 300, height = 100)
    szoveg1 = Label(abl4, text = "a:")
    szoveg2 = Label(abl4, text = "b:")
    szoveg3 = Label(abl4, text = "c:")
    szoveg4 = Label(abl4, text = "Eredmény:")
    gomb1 = Button(abl4, text = "Számítás", command = szamit)
    mezo1 = Entry(abl4)
    mezo2 = Entry(abl4)
    mezo3 = Entry(abl4)
    mezo4 = Entry(abl4)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl4.mainloop()

menu_three = Menubutton(menusor, text = "Trapéz", underline = 0)
menu_three.pack(side = LEFT)

trapez = Menu(menu_three)
trapez.add_command(label = "Felszín", underline = 0, command = felszin)
trapez.add_command(label = "Térfogat", underline = 0, command = terfogat)
menu_three.config(menu = trapez)


    # Negyedik menü

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

    abl5 = Toplevel(foablak)
    abl5.title("A paralelogramma felszíine")
    abl5.minsize(width = 300, height = 100)
    szoveg1 = Label(abl5, text = "a:")
    szoveg2 = Label(abl5, text = "b:")
    szoveg3 = Label(abl5, text = "c:")
    szoveg4 = Label(abl5, text = "Eredmény:")
    gomb1 = Button(abl5, text = "Számítás", command = szamit)
    mezo1 = Entry(abl5)
    mezo2 = Entry(abl5)
    mezo3 = Entry(abl5)
    mezo4 = Entry(abl5)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl5.mainloop()

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

    abl5 = Toplevel(foablak)
    abl5.title("A paralelogramma térfogata")
    abl5.minsize(width = 300, height = 100)
    szoveg1 = Label(abl5, text = "a:")
    szoveg2 = Label(abl5, text = "b:")
    szoveg3 = Label(abl5, text = "c:")
    szoveg4 = Label(abl5, text = "Eredmény:")

    gomb1 = Button(abl5, text = "Számítás", command = szamit)
    mezo1 = Entry(abl5)
    mezo2 = Entry(abl5)
    mezo3 = Entry(abl5)
    mezo4 = Entry(abl5)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl5.mainloop()

menu_four = Menubutton(menusor, text = "Paralelogramma", underline = 0)
menu_four.pack(side = LEFT)

paralelogramma = Menu(menu_four)
paralelogramma.add_command(label = "Felszín", underline = 0)
paralelogramma.add_command(label = "Térfogat", underline = 0)
menu_four.config(menu = paralelogramma)

    # Ötödik menü

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

    abl6 = Toplevel(foablak)
    abl6.title("A téglalap felszíine")
    abl6.minsize(width = 300, height = 100)
    szoveg1 = Label(abl6, text = "a:")
    szoveg2 = Label(abl6, text = "b:")
    szoveg3 = Label(abl6, text = "c:")
    szoveg4 = Label(abl6, text = "Eredmény:")
    gomb1 = Button(abl6, text = "Számítás", command = szamit)
    mezo1 = Entry(abl6)
    mezo2 = Entry(abl6)
    mezo3 = Entry(abl6)
    mezo4 = Entry(abl6)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl6.mainloop()

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

    abl6 = Toplevel(foablak)
    abl6.title("A téglalap térfogata")
    abl6.minsize(width = 300, height = 100)
    szoveg1 = Label(abl6, text = "a:")
    szoveg2 = Label(abl6, text = "b:")
    szoveg3 = Label(abl6, text = "c:")
    szoveg4 = Label(abl6, text = "Eredmény:")

    gomb1 = Button(abl6, text = "Számítás", command = szamit)
    mezo1 = Entry(abl6)
    mezo2 = Entry(abl6)
    mezo3 = Entry(abl6)
    mezo4 = Entry(abl6)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl6.mainloop()

menu_five = Menubutton(menusor, text = "Téglalap", underline = 0)
menu_five.pack(side = LEFT)

teglalap = Menu(menu_five)
teglalap.add_command(label = "Felszín", underline = 0, command = felszin)
teglalap.add_command(label = "Térfogat", underline = 0, command = terfogat)
menu_five.config(menu = teglalap)

    # Hatodik menü

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

    abl6 = Toplevel(foablak)
    abl6.title("A deltoid felszíine")
    abl6.minsize(width = 300, height = 100)
    szoveg1 = Label(abl6, text = "a:")
    szoveg2 = Label(abl6, text = "b:")
    szoveg3 = Label(abl6, text = "c:")
    szoveg4 = Label(abl6, text = "Eredmény:")
    gomb1 = Button(abl6, text = "Számítás", command = szamit)
    mezo1 = Entry(abl6)
    mezo2 = Entry(abl6)
    mezo3 = Entry(abl6)
    mezo4 = Entry(abl6)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl6.mainloop()

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

    abl6 = Toplevel(foablak)
    abl6.title("A deltoid térfogata")
    abl6.minsize(width = 300, height = 100)
    szoveg1 = Label(abl6, text = "a:")
    szoveg2 = Label(abl6, text = "b:")
    szoveg3 = Label(abl6, text = "c:")
    szoveg4 = Label(abl6, text = "Eredmény:")

    gomb1 = Button(abl6, text = "Számítás", command = szamit)
    mezo1 = Entry(abl6)
    mezo2 = Entry(abl6)
    mezo3 = Entry(abl6)
    mezo4 = Entry(abl6)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl6.mainloop()

menu_seven = Menubutton(menusor, text = "Deltoid", underline = 0)
menu_seven.pack(side = LEFT)

deltoid = Menu(menu_six)
deltoid.add_command(label = "Felszín", underline = 0, command = felszin)
deltoid.add_command(label = "Térfogat", underline = 0, command = terfogat)
menu_six.config(menu = deltoid)

    # Hetedik menü

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

    abl7 = Toplevel(foablak)
    abl7.title("A rombusz felszíne")
    abl7.minsize(width = 300, height = 100)
    szoveg1 = Label(abl7, text = "a:")
    szoveg2 = Label(abl7, text = "b:")
    szoveg3 = Label(abl7, text = "c:")
    szoveg4 = Label(abl7, text = "Eredmény:")
    gomb1 = Button(abl7, text = "Számítás", command = szamit)
    mezo1 = Entry(abl7)
    mezo2 = Entry(abl7)
    mezo3 = Entry(abl7)
    mezo4 = Entry(abl7)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl7.mainloop()

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

    abl7 = Toplevel(foablak)
    abl7.title("A rombusz térfogata")
    abl7.minsize(width = 300, height = 100)
    szoveg1 = Label(abl7, text = "a:")
    szoveg2 = Label(abl7, text = "b:")
    szoveg3 = Label(abl7, text = "c:")
    szoveg4 = Label(abl7, text = "Eredmény:")

    gomb1 = Button(abl7, text = "Számítás", command = szamit)
    mezo1 = Entry(abl7)
    mezo2 = Entry(abl7)
    mezo3 = Entry(abl7)
    mezo4 = Entry(abl7)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl7.mainloop()



menu_seven = Menubutton(menusor, text = "Rombusz", underline = 0)
menu_seven.pack(side = LEFT)

rombusz = Menu(menu_seven)
rombusz.add_command(label = "Felszín", underline = 0)
rombusz.add_command(label = "Térfogat", underline = 0)
menu_seven.config(menu = rombusz)

    # Nyolcadik menü

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

    abl8 = Toplevel(foablak)
    abl8.title("A négyzet felszíine")
    abl8.minsize(width = 300, height = 100)
    szoveg1 = Label(abl8, text = "a:")
    szoveg4 = Label(abl8, text = "Eredmény:")
    gomb1 = Button(abl8, text = "Számítás", command = szamit)
    mezo1 = Entry(abl8)
    mezo2 = Entry(abl8)
    mezo3 = Entry(abl8)
    mezo4 = Entry(abl8)
    szoveg1.grid(row = 1)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl8.mainloop()

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

    abl8 = Toplevel(foablak)
    abl8.title("A négyzet térfogata")
    abl8.minsize(width = 300, height = 100)
    szoveg1 = Label(abl8, text = "a:")
    szoveg4 = Label(abl8, text = "Eredmény:")

    gomb1 = Button(abl8, text = "Számítás", command = szamit)
    mezo1 = Entry(abl8)
    mezo2 = Entry(abl8)
    mezo3 = Entry(abl8)
    mezo4 = Entry(abl8)
    szoveg1.grid(row = 1)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl8.mainloop()

menu_eight = Menubutton(menusor, text = "Négyzet", underline = 0)
menu_eight.pack(side = LEFT)

negyzet = Menu(menu_eight)
negyzet.add_command(label = "Felszín", underline = 0, command = felszin)
negyzet.add_command(label = "Térfogat", underline = 0, command = terfogat)
menu_eight.config(menu = negyzet)

    # Kilencedik menü

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

    abl9 = Toplevel(foablak)
    abl9.title("A Kör felszíine")
    abl9.minsize(width = 300, height = 100)
    szoveg1 = Label(abl9, text = "a:")
    szoveg2 = Label(abl9, text = "b:")
    szoveg3 = Label(abl9, text = "c:")
    szoveg4 = Label(abl9, text = "Eredmény:")
    gomb1 = Button(abl9, text = "Számítás", command = szamit)
    mezo1 = Entry(abl9)
    mezo2 = Entry(abl9)
    mezo3 = Entry(abl9)
    mezo4 = Entry(abl9)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl9.mainloop()

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

    abl9 = Toplevel(foablak)
    abl9.title("A Kör térfogata")
    abl9.minsize(width = 300, height = 100)
    szoveg1 = Label(abl9, text = "a:")
    szoveg2 = Label(abl9, text = "b:")
    szoveg3 = Label(abl9, text = "c:")
    szoveg4 = Label(abl9, text = "Eredmény:")

    gomb1 = Button(abl9, text = "Számítás", command = szamit)
    mezo1 = Entry(abl9)
    mezo2 = Entry(abl9)
    mezo3 = Entry(abl9)
    mezo4 = Entry(abl9)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl9.mainloop()

menu_nine = Menubutton(menusor, text = "Kör", underline = 0)
menu_nine.pack(side = LEFT)

kor = Menu(menu_nine)
kor.add_command(label = "Felszín", underline = 0, command = felszin)
kor.add_command(label = "Térfogat", underline = 0, command = terfogat)
menu_nine.config(menu = kor)

# Mainloop 

foablak.mainloop()