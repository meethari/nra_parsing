import sys
import csv
import json

csvFileName = sys.argv[1]
jsonFileName = sys.argv[2]

csvfile = open(csvFileName, 'r')
jsonfile = open(jsonFileName, 'w')

fieldnames = ("name","money","party","state")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
