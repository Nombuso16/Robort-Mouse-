from asyncio import futures
import os
from random import randint
from turtle import position
import time
os.system('clear')


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

def get_cheese(grid):
    cheese_list = []
    while len(cheese_list) < 5:
        coor = (randint(1, len(grid)-2), randint(1, len(grid)-2))
        
        for _ in grid:
            if coor not in cheese_list:
                cheese_list.append(coor)
    
    return cheese_list

def get_start_mouse_position():
    mouse = [randint(1, len(grid)-2), randint(1, len(grid)-2)]
    print(f'initial {mouse}')  
    return mouse

def mouse_current_position(x, y) :
    position = [x, y]
    print(f'current {position}')
    return position

def eat_cheese(mouse_start_position):
    cheeses = ''
    if mouse_start_position in cheese:
        grid[mouse_start_position] = '🧱'
        cheeses += '🧀'
        print(f'Cheese : {cheeses}')
    return mouse_start_position


def get_mouse_direction():
    directions = ['U', 'D', 'L', 'R']
    future_position = input('Move (U)-Up or (D)-Down or (R)-Right or (L)-Left?: ').upper()
    while future_position not in directions :
        future_position = input('Move (D)-Up or (D)-Down or (R)-Right or (L)-Left?: ').upper()
        if future_position == 'EXIT' or future_position == 'QUIT':
            quit()
    
    return future_position

def get_mouse_steps():
    num_steps = ''
    while num_steps == '':
        try:
            num_steps = int(input('How many Steps do you want to take: '))
        except:
            pass
    return num_steps
     

def display_mice_grid(grid):
    os.system('clear')
    for rows in grid:
        for columns in rows:
            print(columns, end = '')
        print()

def new_mouse_directions(grid, future_position, mouse_start_position):
    r, c = mouse_start_position
    old_mouse_place = mouse_start_position.copy()
    directions = get_mouse_direction()
    num_steps = get_mouse_steps()
    
    bound_message = 'Illegal Move - Out of Bound!!!'
    if future_position == 'U' :
            if r - num_steps > 0:
                mouse_start_position[0] = r - num_steps
            else:
                 print(bound_message)

    elif future_position == 'D':
            if r + num_steps < len(grid) - 1  :       
                mouse_start_position[0] = r + num_steps
            else:
                 print(bound_message)
            
    elif future_position == 'L':
            if c + num_steps > 0:
                mouse_start_position[1] = c + num_steps   
            else:
                 print(bound_message)
            
    elif future_position == 'R': 
            if c + num_steps < len(grid) - 1:
                mouse_start_position[1] = c + num_steps
            else:
                 print(bound_message)

    
    time.sleep(2)
    mouse_current_position(r, c)
    return old_mouse_place, directions, mouse_start_position, num_steps


def change_mouse_place(grid, old_mouse_place, new_mouse_place):
    grid[old_mouse_place[0]][old_mouse_place[1]] = '🧱'
    grid[new_mouse_place[0]][new_mouse_place[1]] = '🐁'

       

def update_grid(grid, old_mouse_place, num_steps, mouse_start_position, direction):
    r, c = mouse_start_position
    while old_mouse_place != mouse_start_position:
        if direction == 'U':
                mouse_start_position[0] = r - num_steps
        elif direction == 'D':
                mouse_start_position[0] = r + num_steps
        elif direction == 'L':
                mouse_start_position[1] = c + num_steps
        elif direction == 'R':
                mouse_start_position[1] = c + num_steps
    return old_mouse_place, num_steps
    
def grid_coordinates(grid: list):
    coordinates = []
    for h in range(len(grid)):
        for w in range(len(grid)):
            coordinates.append((h, w))
    return coordinates

if __name__ == '__main__':
    grid_size = get_grid_size()
    grid = make_grid(grid_size)
    cheese = get_cheese(grid)

    mouse_position = get_start_mouse_position()
    health = 5
    cheese_score = 0

    initialize_grid(grid, cheese, mouse_position)
    
    display_mice_grid(grid)
    while True:
        old_mouse_position, mouse_position, direction = new_mouse_directions(grid,get_mouse_direction(), mouse_position)
        cheese_score, health, mouse_position = update_grid(
            grid, 
            old_mouse_position, 
            mouse_position, 
            direction, 
            cheese
        )
    
         
         

         
         




