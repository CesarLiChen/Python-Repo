# Take 10 inputs from the user, figure out how many of them are equal.
# e.g. Input: 2 4 2 8 9 5 5
# output: 4 numbers repeated (2, 2, 5, 5)
# Numbers can will only be from 1 to 10.
# Without using conditionals, loops.
# FAIL, not possible without conditionals or loops.

numbers = input("Please enter the numbers to count")
num_list = numbers.split(" ")
print(num_list)


# This is hacky but without loops, it might the only way.
one = num_list.count("1")
two = num_list.count("2")
three = num_list.count("3")
four = num_list.count("4")
five = num_list.count("5")
six = num_list.count("6")
seven = num_list.count("7")
eight = num_list.count("8")
nine = num_list.count("9")
ten = num_list.count("10")

count_list = [one, two,  three,  four,  five,  \
              six,  seven,  eight, nine,  ten]
count_list.remove(1)
print(count_list)
total = sum(count_list)
print(count_list)
print("Total repeated number: " + str(total))
