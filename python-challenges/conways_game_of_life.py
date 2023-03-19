import random
import time

"""
Conway's Game of Life rules:
1. TURNS OFF - If cell is ON and has < 2 ON neighbours.
2. REMAINS ON - If cell is ON and 2 OR 3 ON neighbours.
3. TURNS OFF - If cell is ON and > 3 ON neighbours.
4. TURNS ON - If cell is OFF and == 3 ON neighbours.
"""

ON_STATE = "O"
OFF_STATE = " "

columns = 30
rows = 10

# Creates 2d List, and fills it with random states
game_board_list = [[ON_STATE if random.randint(0, 1) == 0 else OFF_STATE for i in range(columns)] for j in range(rows)]

cycles = 0
while cycles < 100:
    for row in game_board_list:
        for cell in row:
            print(cell, end="")
        print()

    for r_index in range(rows):
        for c_index in range(columns):
            on_neighbours = 0
            ur = r_index - 1  # ur -> up row
            dr = r_index + 1
            lc = c_index - 1  # left column
            rc = c_index + 1

            if 0 <= ur < rows and 0 <= lc < columns:  # make sure UP-LEFT index are inside list range
                on_neighbours += 1 if game_board_list[ur][lc] == ON_STATE else 0
            if 0 <= ur < rows:  # checks UP
                on_neighbours += 1 if game_board_list[ur][c_index] == ON_STATE else 0
            if 0 <= ur < rows and 0 <= rc < columns:  # checks UP-RIGHT
                on_neighbours += 1 if game_board_list[ur][rc] == ON_STATE else 0

            if 0 <= dr < rows and 0 <= lc < columns:  # DOWN-LEFT
                on_neighbours += 1 if game_board_list[dr][lc] == ON_STATE else 0
            if 0 <= dr < rows:  # DOWN
                on_neighbours += 1 if game_board_list[dr][c_index] == ON_STATE else 0
            if 0 <= dr < rows and 0 <= rc < columns:  # DOWN-RIGHT
                on_neighbours += 1 if game_board_list[dr][rc] == ON_STATE else 0

            if 0 <= lc < columns:  # LEFT
                on_neighbours += 1 if game_board_list[r_index][lc] == ON_STATE else 0
            if 0 <= rc < columns:  # RIGHT
                on_neighbours += 1 if game_board_list[r_index][rc] == ON_STATE else 0

            # Uncomment below line for debugging.
            # print(f"[{r_index}][{c_index}] has: {on_neighbours} ON neighbours")

            curr_cell = game_board_list[r_index][c_index]
            if curr_cell == ON_STATE:
                if on_neighbours < 2 or 3 < on_neighbours:
                    game_board_list[r_index][c_index] = OFF_STATE
            elif curr_cell == OFF_STATE:
                if on_neighbours == 3:
                    game_board_list[r_index][c_index] = ON_STATE
    cycles += 1
    time.sleep(1)
    print("====================")
