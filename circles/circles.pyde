from random import seed
from random import randint

def setup():
    global old_position
    global new_position
    global table
    global index
        
    size(1440, 810)
    frameRate(60)
    background(255, 204, 0)

    index = 0
    direction = "E"
    table = loadTable("../data-20000-rekordow.csv", "header")
    
    old_position = {}
    old_position["y"] = 20
    old_position["x"] = 0
    
    new_position = {}
    new_position["y"] = 20
    new_position["x"] = 0

def draw():
    global old_position
    global new_position
    global table
    global index
    
    row = table.getRow(index)
    strength = float(row.getString("sila").replace(",", "."))
    step = 20

    new_position["x"] = old_position["x"] + step
    new_position["y"] = old_position["y"]
    if new_position["x"] >= width:
        new_position["x"] = step
        new_position["y"] = new_position["y"] + step
        
        if new_position["y"] > height:
            noLoop()
        
    noStroke()
    fill(randint(0,255), randint(0,255), randint(0,255))
    circle(new_position["x"], new_position["y"], strength)
                    
    index += 1
    if index >= table.getRowCount():
        noLoop()
    
    old_position["x"] = new_position["x"]
    old_position["y"] = new_position["y"]

def random_direction():
    return DIRECTIONS[randint(0,3)]
