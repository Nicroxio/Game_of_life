import pygame
import random 

size = 1000,1000
WINDOW_HEIGHT = 100
WINDOW_WIDTH = 100

BLACK = 0,0,0
WHITE = 255,255,255
X = 100
Y = 100
MouseX = 0
MouseY = 0
click = False
mouseButtons = ()

def cell_checker(grid):
    check_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    new_grid = gen_grid(len(grid), len(grid[0]))
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):

            for coord in check_cells:
                one, two = coord
                new_row = row + one
                new_col = col + two

                try:
                    if grid[new_row][new_col] == '█':
                        count = count + 1
                        pass
                    if grid[new_row][new_col] == ' ':
                        pass
                except:
                    # count=count+1
                    pass

            if count == 2 and grid[row][col] == '█':
                new_grid[row][col] = '█'
            elif count == 3:
                new_grid[row][col] = '█'
            else:
                new_grid[row][col] = ' '
            count = 0

    return new_grid
def random_placer(grid, Random_num):
    for i in range(Random_num):
        x = random.randint(0, len(grid) - 1)
        y = random.randint(0, len(grid) - 1)
        grid[x][y] = '█'

def gen_grid(xlen, ylen):
    grid = []
    for num in range(0, xlen):
        grid.append([])
    for row in grid:
        for num in range(0, ylen):
            row.append(' ')
    return grid

def drawGrid(grid):
    thickness = 1
    for x in range(len(grid[0])):
        for y in range(len(grid[1])):
            rect = pygame.Rect(x*10,y*10,WINDOW_WIDTH/10,WINDOW_HEIGHT/10)
            if grid[x][y] == '█':
                thickness = 1000
            else:
                thickness = 1
            pygame.draw.rect(display,BLACK,rect,thickness)


pygame.display.set_caption("Game Of Life")
grid = gen_grid(X,Y)
random_placer(grid, 1000)
display = pygame.display.set_mode(size)

click = False
pause = False

running = True     
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                if pause:
                    pause=False
                else:
                    pause=True
        if event.type == pygame.MOUSEMOTION:
            MouseX, MouseY = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtons = pygame.mouse.get_pressed(num_buttons=3)
            if mouseButtons[0]:
                click=True
            else:  
                click=False

    mouseOnGridX=MouseX//10
    mouseOnGridY=MouseY//10

    print(mouseOnGridX, mouseOnGridY)
    print(click)
    if click:
        grid[mouseOnGridX][mouseOnGridY]="█"
    else:
        pass
    display.fill(WHITE)
    drawGrid(grid)
    # drawGrid(10)
    pygame.display.update()

    if pause != True:
        grid = cell_checker(grid)
    else:
        pass
    