Contributors: Arash Aria, Peter Moung, Bryant Ng, Markus Shaw

This project requires that Scrapy be installed for Python 2.7.10

Github page: https://github.com/mshaw-csumb/CST205_Proj3

The github language breakdown of our project says that it is 99% html, but
that is because the scrapy code we ran early on generated html files of the
web pages that we scraped data from.

The File test.py in "CST205_Proj3\tutorial\tutorial\"  (or  CST205_Proj3/tutorial/tutorial/)
is the main file to this program. 

test.py must be run in order to start the Find That Show! program.

The program was made after running the Scrapy tutorial so the python code is 
in the tutorial folder, and the subsequent tutorial folders.

The program will prompt the user to enter a show title, and present two buttons.

The first button "Search" will search the data that is scraped for the show or movie title that
the user enters.

The second button will be the "Scrape" button, which will run the scrape operation
from the streaming/network television websites and refresh the data into csv files.

Once the user presses Search, a popup will tell them where the show or movie can be found.
For now, the program only checks Fox, The CW, HBO, and Hulu.