import random
# Create 2d list based on user input
# Fill the list with alternating 0s and 1s

columns = int(input("How many columns for the list"))
rows = int(input("How many rows for the list"))
# Below is a bad way of creating 2d lists
# l = [[7]*columns]*rows

# Better ways:
# First, list comprehension
l = [[4 for i in range(columns)] for j in range(rows)]

#Second,
# l = []
# for i in range(rows):
#     col = []
#     for j in range(columns):
#         col.append(0)
#     l.append(col)

print(l)
for i in range(columns):
    for j in range(rows):
        if i % 2 == 0:
            l[j][i] = 1
        else:
            l[j][i] = 0
print(l)

# ======================================================
# One line solution
one_line_list = [[1 if i % 2 == 0 else 0 for i in range(columns)] for j in range(rows)]
print(f"{one_line_list} one line")

