import random
# Conway's Game of Life rules:
# 1. TURNS OFF - If cell is ON and has < 2 ON neighbours.
# 2. REMAINS ON - If cell is ON and 2 OR 3 ON neighbours.
# 3. TURNS OFF - If cell is ON and > 3 ON neighbours.
# 4. TURNS ON - If cell is OFF and == 3 ON neighbours.

ON_STATE = "o"
OFF_STATE = " "

columns = 20
rows = 10

game_board_list = [["hi" for i in range(columns)] for j in range(rows)]

for row in game_board_list:
    for cell in row:
        cell = ON_STATE if random.randint(0, 1) == 0 else OFF_STATE
        print(cell, end=" ")
    print()


