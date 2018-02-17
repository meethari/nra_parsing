import csv
import sys

openfile = sys.argv[1]
writefile = sys.argv[2]

with open(openfile) as f:
    reader = csv.reader(f)
    your_list = list(reader)

# stuff

new_list = []

for row in your_list:

    if (row[1] == "D"):
        row[1] = "Democrat"
    elif (row[1] == "R"):
        row[1] = "Republican"
    else:
        row[1] = "Independent"

    # TODO: getting rid of the numbers

    new_list.append(row)

with open(writefile, 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for row in new_list:
        spamwriter.writerow(row)
