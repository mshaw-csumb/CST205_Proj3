import os
import csv

def searchFox(showTitle):

    with open('fox.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        if showTitle in show:
            print showTitle + " is on Fox"
            break
        else:
            print showTitle + " is not on Fox"
            break


def searchHbo(showTitle):

    with open('hbo.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        for index in show:
            if showTitle in index:
                print showTitle + " is on HBO"
                break
    print showTitle + " is not on HBO"


def searchCw(showTitle):

    with open('cw.csv','rb') as f:
        reader = csv.reader(f)
        showList = map(tuple, reader)

    for show in showList:
        if showTitle in show:
            print showTitle + " is on CW"
            break
        else:
            print showTitle + " is not on CW"
            break


showTitle = raw_input("Enter Show or Movie: ")

#os.system("scrapy crawl fox -o fox.csv")#one of the system calls that will exist for each website we crawl.
#os.system("scrapy crawl cw -o cw.csv")
os.system("scrapy crawl hbo -o hbo.csv")

#searchFox(showTitle)
searchHbo(showTitle)
#searchCw(showTitle)



