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