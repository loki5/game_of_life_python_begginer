import random 
import time

dead = 0
live = 1

def dead_state(width, height):
    return [[dead for _ in range(0, width)] for _ in range(0, height)] 

def random_state(width, height):
    state = dead_state(width, height)
    for x in range(0, state_width(state)):
        for y in range(0, state_height(state)):
            random_number = random.random()
            if random_number > 0.5:
                 state[x][y] = live
            else:
                state[x][y] = dead           
            
    return state
            
def state_width(state):
    return len(state)

def state_height(state):
    return len(state[0])

def render(state):
    signs = { dead: ' ', live: '$'}
    list = []
    
    for x in range(0,state_width(state)):
        lists = ' '
        for y in range(0,state_height(state)):
            if state[x][y] == dead:
                lists += signs[dead]
            else:
                lists += signs[live]
        list.append(lists)
   
    print('\n'.join(list))
    

def next_cell_state(cell_coordinates, state):
    
    width = state_width(state)
    height = state_height(state)
    n_neighbours = 0
    x = cell_coordinates[0]
    y = cell_coordinates[1]
    
    for x1 in range(x - 1, x + 2):
        
        if x1 < 0 or x1 >= width:
            continue
        for y1 in range(y - 1, y + 2):
            if y1 < 0 or y1 >= height:
                continue
            if x1 == x and y1 == 1:
                continue
            if state[x1][y1] == live:
                n_neighbours += 1
        
    if state[x][y] == live:
        if n_neighbours < 2:
            return dead
        elif n_neighbours < 4:
            return live
        else:
            return dead
        
    else:
        if n_neighbours == 3:
            return live
        else:
            return dead

def next_board_state(initial_state):
    
    width = state_width(initial_state)
    height = state_height(initial_state)
    next_state = dead_state(width, height)
    
    for x in range(0, width):
        for y in range(0, height):
            next_state[x][y] = next_cell_state([x, y], initial_state)
    
    return next_state
            
                       
            
def run_forever(init_state):
    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.3)
        
run_forever(random_state(100, 100))