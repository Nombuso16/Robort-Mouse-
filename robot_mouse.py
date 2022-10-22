import os
from random import randint

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
    future_position = input('Move (D)-Up or (D)-Down or (R)-Right or (L)-Left?: ').upper()
    while future_position not in directions:
        future_position = input('Move (D)-Up or (D)-Down or (R)-Right or (L)-Left?: ').upper()

    while True:
        try:
            num_steps = int(input('How many Steps do you want to take: '))
            break
        except Exception as e:
            print('Incorrect input')

def display(grid):
    che = ''
    for c in cheese:
        if tuple(mouse) == c:
            che += '🧀'
    print(f'Cheese: {che}')
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


def updated_grid(grid, mouse, cheese):    
    os.system('clear')
    
    error = 'Illegal Move !!!'
    r, c = mouse
    # che = ''
    # print('cheese :'+che) 
    # for cs in cheese:
    #     if tuple(mouse) == cs:
    #         che += '🧀'   
    for row in grid:
        
        
        if future_position == 'U':                    
            if r - num_steps > 0:
                mouse[0] = r - num_steps
                grid[r ][c] = '🧱'
                grid[r - num_steps][c ] = '🐁'
                print(''.join(row))

   

        elif future_position == 'D':                    
            if r  + num_steps < len(grid) - 1:
                mouse[0] = r + num_steps
                grid[r ][c] = '🧱'
                grid[r + num_steps][c] = '🐁'
                print(''.join(row))
               
        elif future_position == 'L': 
            if c - num_steps > 0: 
                mouse[1] = c - num_steps   
                grid[r ][c] = '🧱' 
                grid[r ][c - num_steps ] = '🐁'
                print(''.join(row))
            
       
        elif future_position == 'R':  
            if c + num_steps < len(grid) - 1:  
                mouse[1] = c + num_steps
                grid[r ][c] = '🧱'     
                grid[r ][c + num_steps ] = '🐁'
                print(''.join(row))

           

        elif future_position == 'EXIT' or future_position == 'QUIT':
            os.system('clear')   
         
    return cheese

def get_cheese(grid):
    cheese_list = []
    while len(cheese_list) < 5:
        coor = (randint(1, len(grid)-2), randint(1, len(grid)-2))
        
        for _ in grid:
            if coor not in cheese_list:
                cheese_list.append(coor)
    
    return cheese_list

if __name__ == '__main__':
    grid_size = get_grid_size() # no bugs
    grid = make_grid(grid_size) # no bugs
    cheese = get_cheese(grid) # no bugs
    mouse = get_mouse() # minor bug
    initialize_grid(grid, cheese, mouse) # seems okay 
    
    
    display(grid)
    while True:
        promt_user = get_mouse_move() #ok
    
        updated_grid(grid, mouse, cheese)

