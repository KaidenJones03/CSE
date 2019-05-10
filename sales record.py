import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    fruit_totals = 0
    for row in reader:
        thing = row[13]  # This is a string
        # print(thing)
        item_type = row[2]
        if item_type == 'Fruits':
            print(thing)
            fruit_totals += float(thing)
    print(fruit_totals)

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    clothes_totals = 0
    for row in reader:
        clothes_profit = row[13]  # This is a string
        # print(thing)
        item_type = row[2]
        if item_type == 'Clothes':
            print(clothes_profit)
            clothes_totals += float(clothes_profit)
    print(clothes_totals)

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    meat_totals = 0
    for row in reader:
        meat_profit = row[13]  # This is a string
        # print(thing)
        item_type = row[2]
        if item_type == 'Meat':
            print(meat_profit)
            meat_totals += float(meat_profit)
    print(meat_totals)

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    meat_totals = 0
    for row in reader:
        meat_profit = row[13]  # This is a string
        # print(thing)
        item_type = row[2]
        if item_type == 'Meat':
            print(meat_profit)
            meat_totals += float(meat_profit)
    print(meat_totals)

