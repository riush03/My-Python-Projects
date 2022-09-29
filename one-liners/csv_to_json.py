import csv,json
print(json.dump(list(csv.reader(open('your.csv')))))