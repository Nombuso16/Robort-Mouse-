import os
from random import randint
import time

future_position = None
num_steps = None

def get_grid_size() -> int:
    grid_size = input('Grid size?: ')
    
    while not grid_size.isdigit():
        grid_size = input('Grid size?: ')
    return int(grid_size)                       #prompting the user for an input


def make_grid(grid_size: int):
    grid = []
    for _ in range(grid_size):
        grid.append(["🧱" for _ in range(grid_size)])
    return grid                                         #returns a 2D list of walls "🧱"

def get_mouse():
    mouse = [randint(1, len(grid)-2), randint(1, len(grid)-2)]
    print(f'initial {mouse}')  
    return mouse

# ok
def get_mouse_move():
    global future_position
    global num_steps
    directions = ['U', 'D', 'L', 'R']
    future_position = ''
    while future_position not in directions:
        future_position = input('Move (D)-Up or (D)-Down or (R)-Right or (L)-Left?: ').upper()
        if future_position == 'EXIT' or future_position == 'QUIT':
            os.system('clear') 
            exit()


    while True:
        try:
            num_steps = int(input('How many Steps do you want to take: '))
            break
        except Exception as e:
            print('Incorrect input')

def display(grid, lives, no_cheese):
    print("life: "+"💗" *lives)
    print("cheese: "+"🧀" * no_cheese, '\n')
    for row in grid:
        print(''.join(row))  
    return grid, cheese

# seems okay  
def initialize_grid(grid: list, cheese_list, mouse):
    for h in range(len(grid)):
        for w in range(len(grid)):
            if (h < 1) or (h >= len(grid) - 1):
                grid[h][w] = '🟥'
            if (w < 1) or (w >= len(grid) - 1):
                grid[h][w] = '🟥'
            if (h, w) in cheese_list:
                grid[h][w] = '🧀'
            if [h, w] == mouse and mouse != '🧀':
                grid[h][w] = '🐁'


def updated_grid(grid, mouse, cheese, no_cheese, mines, lives):    
    os.system('clear')
    
    r, c = mouse
    if future_position == 'U':                    
        #if r - num_steps > 0:
        for steps in range(num_steps):
            #mouse[0] = r - num_steps
            grid[r ][c] = '🧱'
            r= r-1
            time.sleep(0.3)
            grid[r][c ] = '🐁'
            r, c = r, c
            display(grid, lives, no_cheese)
            



    elif future_position == 'D':                    
        if r  + num_steps < len(grid) - 1:
            mouse[0] = r + num_steps
            grid[r ][c] = '🧱'
            grid[r + num_steps][c] = '🐁'
            
    elif future_position == 'L': 
        if c - num_steps > 0: 
            mouse[1] = c - num_steps   
            grid[r ][c] = '🧱' 
            grid[r ][c - num_steps ] = '🐁'
        
    
    elif future_position == 'R':  
        if c + num_steps < len(grid) - 1:  
            mouse[1] = c + num_steps
            grid[r ][c] = '🧱'     
            grid[r ][c + num_steps ] = '🐁'

    # if tuple(mouse) in cheese:
    #     no_cheese += 1
    #     cheese.remove(tuple(mouse))
    
    # if tuple(mouse) in mines:
    #     lives -= 1
    #     mouse_position = [mouse.copy()]
    #     mines.remove(tuple(mouse))
    #     modifying_mines_position((grid, mouse))
    #     display(grid, lives, no_cheese)
        
    #     modifying_mines_position(grid, mouse, place = False)
    #     display(grid, lives, no_cheese)
        #break
    # os.system('clear')   
        
    return cheese, no_cheese, lives

def get_cheese(grid):
    cheese_list = []
    while len(cheese_list) < 5:
        coor = (randint(1, len(grid)-2), randint(1, len(grid)-2))
        
        for _ in grid:
            if coor not in cheese_list:
                cheese_list.append(coor)
    
    return cheese_list


def get_mines(grid, cheese):
    list_mines = []
    while len(list_mines) < 5:
        coordinates = (randint(1, len(grid)-2), randint(1, len(grid)-2))
        
        for _ in grid:
            if coordinates not in list_mines and coordinates not in cheese:
                list_mines.append(coordinates)
    
    return list_mines

def modifying_mines_position(grid, mines_position, position = True):
    if position:
        grid[mines_position[0]][mines_position[1]] = '💣'
    else:
        grid[mines_position[0]][mines_position[1]] = '🧱'


def win_game(cheese):
    winner = True
    if len(cheese) < 1:
        print('Congratulations :)\n You are a winner!!!')
        winner = True
        return winner
    winner = False
    return winner


def lose_game(mines):
    lost = True
    if len(mines) < 1:
        print('GAME OVER!!!\nYou have lost :(')
        lost = True
        return lost
    lost = False
    return lost


if __name__ == '__main__':
    grid_size = get_grid_size() # no bugs
    grid = make_grid(grid_size) # no bugs
    cheese = get_cheese(grid) # no bugs
    mouse = get_mouse() # minor bug
    mines = get_mines(grid, cheese)
    lives = 5
    no_cheese = 0

    initialize_grid(grid, cheese, mouse) # seems okay

    display(grid, lives, no_cheese)
    time.sleep(0.3)
    while True:
        promt_user = get_mouse_move() #ok

        updated_grid(grid, mouse, cheese, no_cheese, mines, lives)
        display(grid, lives, no_cheese)
        time.sleep(0.3)

