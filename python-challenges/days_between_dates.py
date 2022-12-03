# Two dates in following format: mm-dd-yy.
# Determine how many days between the dates.
# No loops, conditionals.
# There are absolutely better and more ACCURATE ways to do this.

date1 = "04-20-2009"
date2 = "02-08-2012"

# Split each date into a list.
# list = [mm, dd, yy]
# Using index to add the days.

date1_list = date1.split("-")
date2_list = date2.split("-")

# Subtracting the days from dates.
days = abs(int(date2_list[1]) - int(date1_list[1]))
# Getting how many days between months
# That's why '* 30'
days_in_month = abs(int(date2_list[0]) - int(date1_list[0])) * 30
# Getting how many days between years
days_in_year = abs(int(date2_list[2]) - int(date1_list[2])) * 365

total_days = days + days_in_month + days_in_year
print("Total days in between the dates is " + str(total_days) + " days.")
