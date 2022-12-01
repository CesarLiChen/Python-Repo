# Program to find the armstrong numbers:
# 371 is an armstrong number
# 3 ^ 3 = 27
# 7 ^ 3 = 343
# 1 ^ 3 =  1
# 27+343+1 = 371

upper_range = int(input("Please enter the upper range to find the armstrong numbers within:"))

for num in range(upper_range):
    digit_amount = len(str(num))  # e.g. 1252 has 4 digits.
    total = 0
    num_to_check = num
    for i in range(digit_amount):
        digit = num_to_check % 10
        total += (digit ** digit_amount)
        num_to_check = num_to_check // 10

    if total == num:
        print(num)
        #print(str(total) + " | " + str(digit) + " | " + str(num_to_check))

