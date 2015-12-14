import os

os.system("scrapy crawl fox -o fox.csv")
os.system("scrapy crawl cw -o cw.csv")
os.system("scrapy crawl hbo -o hbo.csv")
os.system("scrapy crawl hulu -o hulu.csv")
