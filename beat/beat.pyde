from random import seed
from random import randint
from math import pi

def snowflake(entries, x, y):
    for i, entry in enumerate(entries):
        angle = i * 2 * pi / len(entries)
        new_x = x + cos(angle) * entry * 50
        new_y = y + sin(angle) * entry * 50
        line(x, y, new_x, new_y)
        
        if entry / 5 > 0.2:
            snowflake(len(entries) * [entry / 5], new_x, new_y)

def blob(entry, x, y):
    circle(x, y, entry["strength"] * 10)
      
def setup():
    global index
    global table
    global items
    global step
    global rows
    global row_index
    global items_per_row
    global offset
    
    seconds = []
    table = loadTable("../data/20000.csv", "header")
    items = []
    
    bpm = 0
    for row in table.rows():
        if row.getString("bpm"):
            bpm = float(row.getString("bpm").replace(",", "."))
            
        if bpm != 0:
            item = {
                "strength": float(row.getString("sila").replace(",", ".")),
                "bpm": bpm,
                "time": float(row.getString("czas").replace(",", "."))
            }
        
            items.append(item)
               
    size(1440, 810)
    frameRate(144)
    background(0, 0, 0)
    
    index = 1
    step  = 3
    rows = 20
    row_index = 0
    offset = height / 10
    
    items_per_row = width / step
    fill(255,255,255,10)

def draw():
    global index
    global items
    global step
    global rows
    global row_index
    global items_per_row
    global offset
    
    # background(255, 255, 255)
    stroke(0,0,0,0)
    
    if (step * (index - row_index * items_per_row) - step / 2) >= width:
        row_index += 1 
    
    # if (offset + (row_index * height / rows)) >= height:
    #     fill(200,100,100,100)
        
    x = step * (index - row_index * items_per_row) - step / 2
    y = offset + (row_index % rows * height / rows)
    
    # print(step, index, row_index, items_per_row, x,y)
    
    blob(items[index - 1], x, y)
    
    index += 1
    
    if index >= len(items):
        noLoop()
        # index = 0
