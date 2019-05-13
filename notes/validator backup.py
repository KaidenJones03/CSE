def validate(num: str):
    if len(num) != 16:
        return False
    last_digit = num[15]


valid_card_number = "7174233103126850"

print(validate(valid_card_number))

# def reverse_it(string):
#     print(string[0:0:-1])
#     reverse_it(valid_card_number)
#
#
# list_num = list(valid_card_number)
# for index in range(len(list_num)):
#     list_num[index] = int(list_num[index])
with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    baby_food_totals = 0
    for row in reader:
        baby_food_profit = row[13]  # This is a string
        # print(thing)
        item_type = row[2]
        if item_type == 'Baby Food':
            print(baby_food_profit)
            baby_food_totals += float(baby_food_profit)
    print(baby_food_totals)

    with open("Sales Records.csv", 'r') as old_csv:
        reader = csv.reader(old_csv)
        office_supplies_totals = 0
        for row in reader:
            office_supplies_profit = row[13]  # This is a string
            # print(thing)
            item_type = row[2]
            if item_type == 'Office Supplies':
                print(office_supplies_profit)
                office_supplies_totals += float(office_supplies_profit)
        print(office_supplies_totals)