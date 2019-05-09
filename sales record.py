import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        thing = row[13]  # This is a string
        print(thing)
    item_type = row[2]
    if item_type == "Fruits":
        print(item_type)
