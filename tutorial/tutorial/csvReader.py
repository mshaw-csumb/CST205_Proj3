import csv

with open('filename.csv','rb') as f:
    reader = csv.reader(f)
    your_list = map(tuple, reader)

for i in your_list:
    for j in i:
        if "Sniper" in j:
            print "true"
print "false"


print your_list


