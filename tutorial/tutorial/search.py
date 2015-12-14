import os
import csv

def searchFox(showTitle):

    checker = False
    with open('fox.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        if showTitle in show:
            checker = True
            
        
    if checker == True:
        print showTitle + " is on FOX"
    else:
        print showTitle + " is Not on FOX"


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
        print showTitle + " is on HBO"
    else:
        print showTitle + " is Not on HBO"
    

def searchCw(showTitle):

    checker = False
    with open('cw.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        if showTitle in show:
            checker = True
            
        
    if checker == True:
        print showTitle + " is on CW"
    else:
        print showTitle + " is Not on CW"
        

def searchHulu(showTitle):

    checker = False
    with open('hulu.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        if showTitle in show:
            checker = True
            
        
    if checker == True:
        print showTitle + " is on HULU"
    else:
        print showTitle + " is Not on HULU"

showTitle = raw_input("Enter Show or Movie: ")

searchFox(showTitle)
searchHbo(showTitle)
searchCw(showTitle)
searchHulu(showTitle)



