from random import seed
from random import randint
from math import pi
from collections import defaultdict

def setup():
    global index
    global alpha
    global seconds
    global ordered_keys
    
    seconds = defaultdict(list)
    table = loadTable("../data/200.csv", "header")
    
    for row in table.rows():
        second = int(row.getString("czas").replace(",", ".")[0])
        seconds[second].append(float(row.getString("sila").replace(",", ".")))
                
    size(1440, 810)
    frameRate(60)
    background(255, 255, 255)
    
    # noStroke()

    ordered_keys = seconds.keys()
    ordered_keys.sort()
    index = 0
    alpha = 0

def draw():
    global index
    global table
    global alpha
    global seconds
    global ordered_keys
    
    background(255, 255, 255)
    stroke(0, 0, 0, alpha)
    
    x = width / 2
    y = height / 2
    
    snowflake(seconds[ordered_keys[index]], x, y)
    
    alpha += 8 
    if alpha > 255:
        index += 1
        
        if index >= len(ordered_keys):
            index = 0
        alpha = 0

def snowflake(entries, x, y):
    for i, entry in enumerate(entries):
        angle = i * 2 * pi / len(entries)
        new_x = x + cos(angle) * entry * 50
        new_y = y + sin(angle) * entry * 50
        line(x, y, new_x, new_y)
         
        if entry / 5 > 0.2:
            snowflake(len(entries) * [entry / 5], new_x, new_y)
