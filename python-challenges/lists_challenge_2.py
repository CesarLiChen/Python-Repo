# Take 10 inputs from the user, figure out how many of them are equal.
# e.g. Input: 2 4 2 8 9 5 5
# output: 4 numbers repeated (2, 2, 5, 5)
# Numbers WILL only be from 1 to 10.
# Without using conditionals, loops.
# FAIL, not possible without conditionals or loops.

print("Please enter 10 numbers from 1 to 10")

in1 = int(input("1st number"))
in2 = int(input("2nd number"))
in3 = int(input("3rd number"))
in4 = int(input("4th number"))
in5 = int(input("5th number"))
in6 = int(input("6th number"))
in7 = int(input("7th number"))
in8 = int(input("8th number"))
in9 = int(input("9th number"))
in10 = int(input("10th number"))

num_list = [in1, in2, in3, in4, in5, in6, in7, in8, in9, in10]
print(num_list)


# This is hacky but without loops, it might the only way.
one = num_list.count(1)
two = num_list.count(2)
three = num_list.count(3)
four = num_list.count(4)
five = num_list.count(5)
six = num_list.count(6)
seven = num_list.count(7)
eight = num_list.count(8)
nine = num_list.count(9)
ten = num_list.count(10)

count_list = [one, two,  three,  four,  five,  \
              six,  seven,  eight, nine,  ten]
print(count_list)
count_list.remove(1)
print(count_list)

total = sum(count_list)
print("Total repeated number: " + str(total))
