import os
import csv


__authors__ = "Arash Aria, Peter Moung, Bryant Ng, Markus Shaw"
def searchFox(showTitle):

    checker = False
    with open('fox.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        if showTitle in show:
            checker = True
            
        
    if checker == True:
         showTitle = str(showTitle) + (" is on FOX")

    else:
         showTitle = str(showTitle) + (" is Not on FOX")
    return showTitle

def searchHbo(showTitle):

    checker = False
    with open('hbo.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        for index in show:
            if showTitle in index:
                checker = True
            

    if checker == True:
         showTitle = str(showTitle) + (" is on HBO")

    else:
         showTitle = str(showTitle) + (" is Not on HBO")
    return showTitle
    

def searchCw(showTitle):

    checker = False
    with open('cw.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        if showTitle in show:
            checker = True
            
    if checker == True:
        showTitle = str(showTitle) + (" is on CW")

    else:
         showTitle = str(showTitle) + (" is Not on CW")
    return showTitle
        

def searchHulu(showTitle):

    checker = False
    with open('hulu.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        if showTitle in show:
            checker = True
            
        
    if checker == True:
         showTitle = str(showTitle) + (" is on HULU")

    else:
         showTitle = str(showTitle) + (" is Not on HULU")
    return showTitle

#showTitle = raw_input("Enter Show or Movie: ")

#searchFox(showTitle)
#searchHbo(showTitle)
#searchCw(showTitle)
#searchHulu(showTitle)



