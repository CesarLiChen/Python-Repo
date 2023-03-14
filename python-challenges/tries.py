# Python file for trying assorted code
column = 4
rows = 8

multi_list = [["0" for i in range(column)] for j in range(rows)]

print_row = ""
for r in multi_list:
    for c in r:
        print(c, end=" ")
    print("")

on_neighbours = 5
on_neighbours += 1 if False else 5
print(on_neighbours)



