# Take input for 5 numbers and sort them.
# Done without:
# .sort function, conditionals, loops

numbers = input("Please enter 5 numbers separated by spaces")

num_list = numbers.split(" ")
print("Full list " + str(num_list))
# Find max, and min of the list
#then delete them from the list
last = max(num_list)
first = min(num_list)
num_list.remove(last)
num_list.remove(first)
print("Removed first and last " + str(num_list))

# Do it again for the 3 numbers left
fourth = max(num_list)
second = min(num_list)
num_list.remove(fourth)
num_list.remove(second)
print("Removed second and fourth " + str(num_list))

# With only one item left in list
third = num_list[0]

print(first, second, third, fourth, last)
