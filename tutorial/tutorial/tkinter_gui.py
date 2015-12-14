__author__ = 'Bjon'

#!/usr/bin/python

import Tkinter
import tkMessageBox
from Tkinter import *
from PIL import ImageTk, Image
import os

def urMumCallBack():
    tkMessageBox.showinfo( "yo wassup", test())

def urDadCallBack():
    print ("Refresh: %s" % (E1.get()))

def test():
    #insert return functions to print out if or if not on the tv
    #replace E1.get() with return function tvs
    return E1.get() + "\n" + E1.get() + "\n" + E1.get() + "\n" + E1.get() + "\n"

master = Tk()
master.geometry("400x300")



L1 = Label(master, text="Enter name of movie or tv show:")
L1.pack()

E1 = Entry(master, bd =5)
E1.pack()


L2 = Tkinter.Button(master,text = "Submit", command = urMumCallBack)
L2.pack()

L3 = Tkinter.Button(master,text = "Scrape me!", command = urDadCallBack)
L3.pack()

image = Image.open("logo3.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo # keep a reference!
label.pack()

master.mainloop()

