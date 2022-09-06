import os
from time import sleep
import random

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def screen(grid):
    for x in grid:
        print(x)

def grid(xlen,ylen):
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




if __name__ == '__main__':
    #init
    grid = grid(int(input('How many Rows: ')), int(input('How many Columns: ')))
    random_placer(grid,10)

    #main loop
    while True:
        screen(grid)
        clear()