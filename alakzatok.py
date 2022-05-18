# Import


# Formák 

    # Háromszög

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
