import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    fruit_totals = 0
    clothes_totals = 0
    meat_totals = 0
    beverage_totals = 0
    baby_food_totals = 0
    office_supplies_totals = 0
    Cosmetics_totals = 0
    Household_totals = 0
    Cereal_totals = 0
    Personal_Care_totals = 0
    Vegetables_totals = 0
    Snacks_totals = 0
    for row in reader:
        profit = row[13]  # This is a string
        # print(thing)
        item_type = row[2]
        if item_type == 'Fruits':
            fruit_totals += float(profit)
        if item_type == 'Clothes':
            clothes_totals += float(profit)
        if item_type == 'Meat':
            meat_totals += float(profit)
        if item_type == 'Beverage':
            beverage_totals += float(profit)
        if item_type == 'Baby Food':
            baby_food_totals += float(profit)
        if item_type == 'Office Supplies':
            office_supplies_totals += float(profit)
        if item_type == 'Cosmetics':
            Cosmetics_totals += float(profit)
        if item_type == 'HouseHold':
            Household_totals += float(profit)
        if item_type == 'Cereal':
            Cereal_totals += float(profit)
        if item_type == 'Personal Care':
            Personal_Care_totals += float(profit)
        if item_type == 'Vegetables':
            Vegetables_totals += float(profit)
        if item_type == 'Snacks':
            Snacks_totals += float(profit)
    print(clothes_totals)
    print(fruit_totals)
    print(meat_totals)
    print(beverage_totals)
    print(baby_food_totals)
    print(office_supplies_totals)
    print(Cosmetics_totals)
    print(Household_totals)
    print(Cereal_totals)
    print(Personal_Care_totals)
    print(Vegetables_totals)
    print(Snacks_totals)








