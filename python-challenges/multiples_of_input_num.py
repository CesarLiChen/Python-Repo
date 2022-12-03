# Loop from 0 to 100 and
# print out all multiples of
# a number given as input.

in_num = int(input("Please enter a number"))

n = 1
while n < 100:
    print(in_num * n)
    n += 1
