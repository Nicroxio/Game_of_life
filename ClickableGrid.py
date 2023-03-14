import pygame
import random 
from json import dumps, loads

size = 1000,1000
X = int(size[0]/10)
Y = int(size[1]/10)



#Colours
BLACK = 0,0,0
WHITE = 255,255,255

def save(grid):
    file = open("Save","w+")
    file.write(dumps(grid))
    file.close()

def load(path):
    file = open(str(path),"r")
    grid = loads(file.read())
    file.close()
    return grid

def cell_checker(grid,X,Y):
    check_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    new_grid = gen_grid(X, Y)
    for row in range(X):
        for col in range(Y):

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

def drawGrid(grid,WINDOW_WIDTH,WINDOW_HEIGHT,display):
    thickness = 1
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*10,y*10,WINDOW_WIDTH/10,WINDOW_HEIGHT/10)
            if grid[x][y] == '█':
                thickness = 1000
            else:
                thickness = 1
            pygame.draw.rect(display,BLACK,rect,thickness)




def init(X,Y,Load,Path):
    if Load:
        grid = load(Path)
    else:
        grid = gen_grid(X,Y)
    # random_placer(grid, 1000)
    return grid




def mainLoop(size,X,Y,grid): 
    pygame.display.set_caption("Game Of Life")
    display = pygame.display.set_mode(size) 
    click = False
    pause = True  
    mode = False
    running = True
    MouseX = 0
    MouseY = 0
    mouseButtons = ()
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
                elif event.key == pygame.K_1:
                    if mode:
                        mode = False
                    else:
                        mode = True

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
        drawGrid(grid,X,Y,display)
        # drawGrid(10)
        pygame.display.update()

        if pause != True:
            grid = cell_checker(grid,X,Y)
        if mode != True:
            click=False
        if running == False:
            save(grid)
        
def main():
    grid = init(X,Y,True,"./Save")
    mainLoop(size,X,Y,grid)

if __name__ == "__main__":
    main()