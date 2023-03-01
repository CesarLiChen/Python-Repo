bill_total = 36.23
only_bills_of_5 = 5

# if b = bill of $5,
# t = total

# Rounds to 'nearest' multiple of the bill
# b * (t / b)
# e.g. 12.24 --> 10 | 13.68 --> 15

# Rounds to next multiple of the bill
# t + (b - t) % b
# e.g. 41.23 --> 45 | 44.99 --> 45

round_to_multiple_of_bill = bill_total + (only_bills_of_5 - bill_total) % only_bills_of_5

change = round_to_multiple_of_bill - bill_total
change_rounded = round(change, 2)

print("If only paying with bills of $5, the change will be: " + str(change_rounded))
