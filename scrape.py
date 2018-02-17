import csv
import sys

openfile = sys.argv[1]
writefile = sys.argv[2]

with open(openfile) as f:
    reader = csv.reader(f)
    your_list = list(reader)

print (your_list)

us_state_abbrev = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
}



new_list = []

print ("\n\n")

for row in your_list:
    string = row[0]
    length = len(string)
    #print (length)
    row[0] = string[0: length - 7]
    party = string[length-5]
    if (party == "D"):
        row.append("Democrat")
    elif (party == "R"):
        row.append("Republican")
    else:
        row.append("")
    state = string[length-3: length-1]
    row.append(us_state_abbrev.get(state, "Unkown"))
    comma_pos = string.find(',')
    if (comma_pos != -1):
        string = string[comma_pos + 2: length - 7] + " " + string[0: comma_pos]
        row[0] = string
    row.pop(1)
    new_list.append(row)



print (new_list)


with open(writefile, 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for row in new_list:
        spamwriter.writerow(row)
