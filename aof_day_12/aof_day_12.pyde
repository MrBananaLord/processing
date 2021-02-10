from random import seed
from random import randint

DIRECTIONS = ["N", "W", "S", "E"]
ROTATIONS = ["L", "R"]
BOAT_LENGTH = 10
DELAY_FACTOR = 2
DAY = 2

def next_position(position, direction, distance):
    if direction == "N":
        return [position[0], position[1] + distance]
    elif direction == "S":
        return [position[0], position[1] - distance]
    elif direction == "E":
        return [position[0] + distance, position[1]]
    elif direction == "W":
        return [position[0] - distance, position[1]]

def next_direction(direction, rotation_direction, rotation):
    if rotation_direction == "R":
        return DIRECTIONS[DIRECTIONS.index(direction) - int((rotation / 90) % 4)]
    elif rotation_direction == "L":
        return DIRECTIONS[DIRECTIONS.index(direction) - len(DIRECTIONS) + int((rotation / 90) % 4)]

def draw_ship(ship_position, ship_direction):
    bow_x = ship_position[0]
    bow_y = ship_position[1]
    
    if ship_direction == "N":
        stern_port_x = bow_x - BOAT_LENGTH // 2 
        stern_port_y = bow_y - BOAT_LENGTH
        stern_star_x = bow_x + BOAT_LENGTH // 2
        stern_star_y = bow_y -BOAT_LENGTH
    elif ship_direction == "E":
        stern_port_x = bow_x - BOAT_LENGTH 
        stern_port_y = bow_y + BOAT_LENGTH // 2
        stern_star_x = bow_x - BOAT_LENGTH
        stern_star_y = bow_y - BOAT_LENGTH // 2
    elif ship_direction == "S":
        stern_port_x = bow_x + BOAT_LENGTH // 2 
        stern_port_y = bow_y + BOAT_LENGTH
        stern_star_x = bow_x - BOAT_LENGTH // 2
        stern_star_y = bow_y + BOAT_LENGTH
    elif ship_direction == "W":
        stern_port_x = bow_x + BOAT_LENGTH 
        stern_port_y = bow_y - BOAT_LENGTH // 2
        stern_star_x = bow_x + BOAT_LENGTH
        stern_star_y = bow_y + BOAT_LENGTH // 2
         
    triangle(bow_x, bow_y, stern_port_x, stern_port_y, stern_star_x, stern_star_y)

def setup():
    global ship_direction
    global ship_position
    global instructions
    global index
    
    file = open("day_12_input.txt", "r")
    
    index = 0
    
    ship_direction = "E"
    ship_position = [width // 2, height // 2]
    instructions = []

    for instruction in file.readlines():
        instructions.append(instruction.strip("\n"))
        
    size(4000, 3000)
    frameRate(60)
    stroke(0,0,0,0)
    background(100, 125, 255)
    
def draw():
    global instructions
    global ship_direction
    global ship_position
    global index
    
    if len(instructions) == 0:
        noLoop()
    elif index % DELAY_FACTOR == 0:
        instruction = instructions.pop()
        command, value = instruction[0], int(instruction[1:])
            
        if command in DIRECTIONS:
            ship_position = next_position(ship_position, command, value)
        elif command in ROTATIONS:
            ship_direction = next_direction(ship_direction, command, value)
        elif command == "F":
            ship_position = next_position(ship_position, ship_direction, value)
           
    # background(100, 125, 255) 
    draw_ship(ship_position, ship_direction)
    index += 1
