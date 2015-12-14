import os
import csv

def searchFox(showTitle,services):

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

    services[0] = False
    return services


showTitle = raw_input("Enter Show or Movie: ")

os.system("scrapy crawl fox -o fox.csv")#one of the system calls that will exist for each website we crawl.
#os.system("scrapy crawl cw -o cw.csv")
#os.system("scrapy crawl hbo -o hbo.csv")

services = [False,False,False]#index 0 = Fox, index 1 = CW, index 2 = hbo

services = searchFox(showTitle,services)



