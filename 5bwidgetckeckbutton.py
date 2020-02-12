from tkinter import *
root = Tk()


def var_states():
    print
    ("Singing 1 : % d, \nDancing 2 : % d, \nRiding 3 : % d" % (
        var1.get(), var2.get(), var3.get()))

var1 = IntVar()
c1 = Checkbutton(root, text="Singing", variable=var1)

var2 = IntVar()
c2 = Checkbutton(root, text="Dancing", variable=var1)

var3 = IntVar()
c3 = Checkbutton(root, text="Riding", variable=var2)
b = Button(root, text="SHOW", command=var_states)

c1.pack(side=LEFT)
c2.pack(side=LEFT)
c3.pack(side=LEFT)
b.pack(side=LEFT)
