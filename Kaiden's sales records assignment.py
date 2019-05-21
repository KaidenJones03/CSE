import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    fruit_totals = 0
    clothes_totals = 0
    meat_totals = 0
    beverage_totals = 0
    office_supplies_totals = 0
    Cosmetics_totals = 0
    baby_food_totals = 0
    Household_totals = 0
    Cereal_totals = 0
    Personal_Care_totals = 0
    Vegetables_totals = 0
    Snacks_totals = 0
    sub_saharan_africa_total = 0
    middle_east_and_north_africa_total = 0
    australia_and_oceania_total = 0
    europe_total = 0
    asia_total = 0
    central_america_and_the_caribbean_total = 0
    north_america_total = 0
    for row in reader:
        profit = row[13]
        region = row[0]
        # This is a string
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
        if region == 'Sub-Saharan Africa':
            sub_saharan_africa_total += float(profit)
        if region == 'Middle East and North Africa ':
            middle_east_and_north_africa_total += float(profit)
        if region == 'Australia and Oceania':
            australia_and_oceania_total += float(profit)
        if region == 'Europe':
            europe_total += float(profit)
        if region == 'Asia':
            asia_total += float(profit)
        if region == 'Central America and the Caribbean':
            central_america_and_the_caribbean_total += float(profit)
        if region == 'North America':
            north_america_total += float(profit)

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
    print("Sub-Saharan Africa profit:", sub_saharan_africa_total)
    print("Middle East and North Africa profit:", middle_east_and_north_africa_total)
    print("Australia and Oceania profit:", australia_and_oceania_total)
    print("Europe profit:", europe_total)
    print("Asia profit:", asia_total)
    print("Central America and the Caribbean profit:", central_america_and_the_caribbean_total)
    print("North America profit:", north_america_total)


list_of_profits = [clothes_totals, fruit_totals, meat_totals, beverage_totals, baby_food_totals, office_supplies_totals,
                   Cosmetics_totals, Household_totals, Cereal_totals, Personal_Care_totals, Vegetables_totals,
                   Snacks_totals]
list_of_items = ["Clothes", "Fruit", "Meat", "Beverages", "baby food", "office supplies", "cosmetics", "household",
                 "cereal", "personal care", "vegetable", "snacks"]
index_of_item = list_of_profits.index(max(list_of_profits))
print("The most profitable item is", list_of_items[index_of_item], max(list_of_profits))

list_of_regions = ['Sub-Saharan Africa', 'Middle East and North Africa', 'Australia and Oceania', 'Europe', 'Asia',
                   'Central America and the Caribbean', 'North America']
list_of_region_profits = [sub_saharan_africa_total, middle_east_and_north_africa_total, australia_and_oceania_total,
                          europe_total, asia_total, central_america_and_the_caribbean_total, asia_total]
index_of_region = list_of_region_profits.index(max(list_of_region_profits))
print("The most profitable region is", list_of_regions[index_of_region], max(list_of_region_profits))
