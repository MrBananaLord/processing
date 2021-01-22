from random import seed
from random import randint
from math import pi

# screen saver
# R_RATIO = 100
# ALPHA = 50
# ROW_COUNT = 6
# STEP = 30
# OFFSET_Y = 30
# ENDLESS = True

# space
# R_RATIO = 1
# ALPHA = 50
# ROW_COUNT = 20
# STEP = 3
# OFFSET_Y = 30
# ENDLESS = False

# zebra
R_RATIO = 10
ALPHA = 255
ROW_COUNT = 20
STEP = 3
OFFSET_Y = 30
ENDLESS = False

def snowflake(entries, x, y):
    for i, entry in enumerate(entries):
        angle = i * 2 * pi / len(entries)
        new_x = x + cos(angle) * entry * 50
        new_y = y + sin(angle) * entry * 50
        line(x, y, new_x, new_y)
        
        if entry / 5 > 0.2:
            snowflake(len(entries) * [entry / 5], new_x, new_y)

def blob(entry, x, y):
    fill(255 - entry["strength"] * R_RATIO, 255 - entry["strength"] * R_RATIO,255 - entry["strength"] * R_RATIO,ALPHA)
    stroke(0,0,0,0)
    circle(x, y, entry["strength"] * R_RATIO)
    # fill(0,0,0,0)
    # stroke(0,255,0,10)
    # line(width / 2, height / 2, x, y)
      
def setup():
    global index
    global table
    global items
    global row_index
    
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
            
    stroke(0,0,0,0)
    size(1440, 810)
    frameRate(144)
    background(0, 0, 0)
    
    index = 1
    row_index = 0

def draw():
    global index
    global items
    global row_index
    
    items_per_row = width / STEP
    
    if (STEP * (index - row_index * items_per_row)) >= width:
        row_index += 1 
    
    x = (STEP * (index - row_index * items_per_row))
    y = (row_index % ROW_COUNT * height / ROW_COUNT) + OFFSET_Y
        
    blob(items[index - 1], x, y)
    
    index += 1
    
    print(row_index, ROW_COUNT)
    if not ENDLESS and row_index > ROW_COUNT:
        noLoop()
    
    if index >= len(items):
        noLoop()
        # index = 0
