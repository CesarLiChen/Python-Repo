bill_total = 43.22
only_bills_of_5 = 5

change = (only_bills_of_5 * round(bill_total / only_bills_of_5)) - bill_total

change_rounded = round(change, 2)

print("If only paying with bills of $5, the change will be: " + str(change_rounded))
