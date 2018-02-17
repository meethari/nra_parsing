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

    state = row[3]
    i = 0
    for ch in state:
        if (ch == ' '):
            if state[i+1].isdigit():
                print(state)
                state = state[:i]
                print(state)
        i = i + 1

    row[3] = state
    # TODO: getting rid of the numbers

    new_list.append(row)

with open(writefile, 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for row in new_list:
        spamwriter.writerow(row)
