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
        if item_type == 'Beverages':
            beverage_totals += float(profit)
        if item_type == 'Baby Food':
            baby_food_totals += float(profit)
        if item_type == 'Office Supplies':
            office_supplies_totals += float(profit)
        if item_type == 'Cosmetics':
            Cosmetics_totals += float(profit)
        if item_type == 'Household':
            Household_totals += float(profit)
        if item_type == 'Cereal':
            Cereal_totals += float(profit)
        if item_type == 'Personal Care':
            Personal_Care_totals += float(profit)
        if item_type == 'Vegetables':
            Vegetables_totals += float(profit)
        if item_type == 'Snacks':
            Snacks_totals += float(profit)
    print("clothes profit:", clothes_totals)
    print("fruit profit:", fruit_totals)
    print("meat profit:", meat_totals)
    print("beverage profit:", beverage_totals)
    print("baby food profit:", baby_food_totals)
    print("office supplies profit:", office_supplies_totals)
    print("cosmetics profit:", Cosmetics_totals)
    print("household profit:", Household_totals)
    print("cereal profit:", Cereal_totals)
    print("personal care profit:", Personal_Care_totals)
    print("vegetable:", Vegetables_totals)
    print("snacks profit:", Snacks_totals)


list_of_profits = [clothes_totals, fruit_totals, meat_totals, beverage_totals, baby_food_totals, office_supplies_totals
                   , Cosmetics_totals, Household_totals, Cereal_totals, Personal_Care_totals, Vegetables_totals,
                   Snacks_totals]
list_of_items = ["Clothes", "Fruit", "Meat", "Beverages", "baby food", "office supplies", "cosmetics", "household",
                 "cereal", "personal care", "vegetable", "snacks"]
index_of_item = list_of_profits.index(max(list_of_profits))
print(list_of_items[index_of_item], max(list_of_profits))
