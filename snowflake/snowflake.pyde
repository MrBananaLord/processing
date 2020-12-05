from random import seed
from random import randint
from collections import defaultdict

def setup():
    global table
    global seconds
    global i
    global j
    
    size(1440, 810)
    frameRate(10)
    background(255, 204, 0)
    
    table = loadTable("../data/200.csv", "header")
    seconds = defaultdict(list)
    i = 0
    j = 0

    for row in table.rows():
        current_second = int(row.getString("czas").split(",")[0])
        seconds[current_second].append(float(row.getString("sila").replace(",", ".")))

def draw():
    global i
    global j
    global seconds
    
    if i < len(seconds):
        x = width / 2.0
        y = height / 2.0
         
        for strength in seconds[i]:
            length = int(strength * 4)
            angle = randint(1,360)
            new_x = x + cos(angle) * length
            new_y = y + sin(angle) * length
            # print(length, angle, x, y, new_x, new_y)
            line(x, y, new_x, new_y)
            x = new_x
            y = new_x
    i += 1
    
    if i == len(seconds):
        noLoop()
# def setup():
#   size(200, 200)  

# def draw():
#   background(0)
#   stroke(255)
#   lineAngle(100, 100, (millis()/1000.0), 50)
