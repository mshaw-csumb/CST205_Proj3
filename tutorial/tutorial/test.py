import Tkinter
from Tkinter import *
import tkMessageBox
import os
from search import *


app = Tk()
app.title("Find That Show!")
app.geometry('350x200')


def scrape():

    try:
        os.remove("fox.csv")
        os.remove("cw.csv")
        os.remove("hbo.csv")
        os.remove("hulu.csv")
    except OSError:
        pass

    os.system("scrapy crawl fox -o fox.csv")
    os.system("scrapy crawl cw -o cw.csv")
    os.system("scrapy crawl hbo -o hbo.csv")
    os.system("scrapy crawl hulu -o hulu.csv")


def display():
    tkMessageBox.showinfo( "Results", search())

#def urDadCallBack():
    #print ("Refresh: %s" % (E1.get()))

def search():
    #insert return functions to print out if or if not on the tv
    #replace E1.get() with return function tvs
    showTitle = title.get()
    return searchFox(showTitle) + "\n" +  searchHbo(showTitle) + "\n" +  searchCw(showTitle) + "\n" + searchHulu(showTitle) + "\n"

showTitle = StringVar(None)
L1 = Label (app, text="Welcome to Find That Show!")
L1.pack()
title = Entry(app, textvariable=showTitle)
title.pack()

button1 = Button(app, text="Search", width = 20, command = display)
button1.pack(side='left', padx=15, pady=15)

button2 = Button(app, text="Scrape", width = 20, command = scrape)
button2.pack(side='right', padx=15, pady=15)



app.mainloop()