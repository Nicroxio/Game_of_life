import os
from time import sleep
import random

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def screen(grid):
    for row in grid:
        print(row)

def gen_grid(xlen,ylen):
    grid =[]
    for num in range(0,ylen):
        grid.append([])
    for row in grid:
        for num in range(0,xlen):
            row.append('□')
    return grid


def random_placer(grid,Random_num):
    for i in range(Random_num):
        x = random.randint(0,len(grid)-1)
        y = random.randint(0,len(grid)-1)
        grid[x][y] = '■'

def cell_checker(grid):
    check_cells =[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    count = 0
    new_grid = gen_grid(len(grid),len(grid[0]))
    for row in range(0,len(grid)):
        for col in range(0,len(grid[0])):

            for coord in check_cells:
                one,two = coord
                new_row = row + one
                new_col = col + two
                # print(grid[new_row][new_col])
                # print(count)
                try:

                    if grid[new_row][new_col] == '■':
                        count=count+1
                        pass

                    if grid[new_row][new_col] == '□':
                        pass
                except:
                    pass

            if count == 2 and grid[row][col] == '■':
                new_grid[row][col] = '■'
            elif count == 3:
                new_grid[row][col] = '■'
            else:
                new_grid[row][col] = '□'
            count = 0


    return new_grid



if __name__ == '__main__':
    #init
    grid = gen_grid(int(20), int(20))
    random_placer(grid,40)
    # screen(grid)
    # grid = cell_checker(grid)
    # screen(grid)

    #main loop
    while True:
        screen(grid)
        grid = cell_checker(grid)
        sleep(1)
        clear()
        # exit()
        pass
