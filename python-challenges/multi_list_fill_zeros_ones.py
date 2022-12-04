import random
# Create 2d list based on user input
# Fill the list with alternating 0s and 1s

columns = int(input("How many columns for the list"))
rows = int(input("How many rows for the list"))

l = [[7]*columns]*rows

print(l)
for i in range(columns):
    for j in range(rows):
        print(i % 2)
        if i % 2 == 0:
            l[j][i] = 1
        else:
            l[j][i] = 0
print(l)
