# Import

import sys
from alakzatok import * 
from tkinter import * 

# Foablak

foablak = Tk()
foablak.title("Síkidomok területe és kerülete")
foablak.minsize(width = 500, height = 250)

# Def

# Widgetek

# Menu

    # Menüsor
menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)

    # Első menü

menu_one = Menubutton(menusor, text = "File", underline = 0)
menu_one.pack(side = LEFT)

file = Menu(menu_one)
file.add_command(label = "Névjegy", underline = 0)
file.add_command(label = "Kilépés", command = foablak.destroy, underline = 0)
menu_one.config(menu = file)

    # Második menü

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

menu_two = Menubutton(menusor, text = "Háromszög", underline = 0)
menu_two.pack(side = LEFT)

haromszog = Menu(menu_two)
haromszog.add_command(label = "Felszín", underline = 0)
haromszog.add_command(label = "Térfogat", underline = 0)
menu_two.config(menu = haromszog)


    # Harmadik Menü

menu_three = Menubutton(menusor, text = "Trapéz", underline = 0)
menu_three.pack(side = LEFT)

trapez = Menu(menu_three)
trapez.add_command(label = "Felszín", underline = 0)
trapez.add_command(label = "Térfogat", underline = 0)
menu_three.config(menu = trapez)


    # Negyedik menü

menu_four = Menubutton(menusor, text = "Paralelogramma", underline = 0)
menu_four.pack(side = LEFT)

paralelogramma = Menu(menu_four)
paralelogramma.add_command(label = "Felszín", underline = 0)
paralelogramma.add_command(label = "Térfogat", underline = 0)
menu_four.config(menu = paralelogramma)

    # Ötödik menü

menu_five = Menubutton(menusor, text = "Téglalap", underline = 0)
menu_five.pack(side = LEFT)

teglalap = Menu(menu_five)
teglalap.add_command(label = "Felszín", underline = 0)
teglalap.add_command(label = "Térfogat", underline = 0)
menu_five.config(menu = teglalap)

    # Hatodik menü

menu_six = Menubutton(menusor, text = "Deltoid", underline = 0)
menu_six.pack(side = LEFT)

deltoid = Menu(menu_six)
deltoid.add_command(label = "Felszín", underline = 0)
deltoid.add_command(label = "Térfogat", underline = 0)
menu_six.config(menu = deltoid)

    # Hetedik menü

menu_seven = Menubutton(menusor, text = "Rombusz", underline = 0)
menu_seven.pack(side = LEFT)

rombusz = Menu(menu_seven)
rombusz.add_command(label = "Felszín", underline = 0)
rombusz.add_command(label = "Térfogat", underline = 0)
menu_seven.config(menu = rombusz)

    # Nyolcadik menü

menu_eight = Menubutton(menusor, text = "Négyzet", underline = 0)
menu_eight.pack(side = LEFT)

negyzet = Menu(menu_eight)
negyzet.add_command(label = "Felszín", underline = 0)
negyzet.add_command(label = "Térfogat", underline = 0)
menu_eight.config(menu = negyzet)

    # Kilencedik menü

menu_nine = Menubutton(menusor, text = "Kör", underline = 0)
menu_nine.pack(side = LEFT)

kor = Menu(menu_nine)
kor.add_command(label = "Felszín", underline = 0)
kor.add_command(label = "Térfogat", underline = 0)
menu_nine.config(menu = kor)

# Mainloop 

foablak.mainloop()