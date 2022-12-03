"""
Based on number from user, output necessary pattern.
e.g. input = 4
output:
*
**
***
****
***
**
*
Use for loops.
"""

input_num = input("Please give me a number")
if input_num.strip().isdigit():
    max_stars = int(input_num)
    for i in range(max_stars):
        print("*" * (i + 1))

    for j in reversed(range(1, max_stars)):
        print("*" * j)
else:
    print("Sorry, I don't think that's a number")
