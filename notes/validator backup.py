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