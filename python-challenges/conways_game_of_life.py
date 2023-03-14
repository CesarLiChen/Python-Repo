import random
# Conway's Game of Life rules:
# 1. TURNS OFF - If cell is ON and has < 2 ON neighbours.
# 2. REMAINS ON - If cell is ON and 2 OR 3 ON neighbours.
# 3. TURNS OFF - If cell is ON and > 3 ON neighbours.
# 4. TURNS ON - If cell is OFF and == 3 ON neighbours.

ON_STATE = "o"
OFF_STATE = " "

columns = 5
rows = 3

# Creates 2d List populated with "hi"s
game_board_list = [[ON_STATE if random.randint(0, 1) == 0 else OFF_STATE for i in range(columns)] for j in range(rows)]

for row in game_board_list:
    for cell in row:
        print(cell, end=" ")
    print()

for r_index in range(rows):
    for c_index in range(columns):
        on_neighbours = 0
        ur = r_index - 1 # ur -> up row
        dr = r_index + 1
        lc = c_index - 1 # left column
        rc = c_index + 1

        if 0 <= ur < rows and 0 <= lc <columns: # make sure up left is not out of bounce
            on_neighbours += 1 if game_board_list[ur][lc] == ON_STATE else 0

        print(f"[{r_index}][{c_index}] U-L neighbor's state is: {on_neighbours}")
