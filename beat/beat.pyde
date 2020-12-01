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
    circle(x, y, entry["strength"] * randint(10, 100))
      
def setup():
    global index
    global table
    global alpha
    global items
    global fade_out
    
    seconds = []
    table = loadTable("../data/200.csv", "header")
    items = []
    fade_out = []
    
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
    frameRate(60)
    background(255, 255, 255)
    
    index = 0
    alpha = 0

def draw():
    global index
    global alpha
    global items
    global fade_out
    
    # background(255, 255, 255)
    fill(255,255,255,0)
    
    y = height / 2
    
    for i, item in enumerate(fade_out):
        stroke((255 / 5) * (5 - i), (255 / 5) * (5 - i), (255 / 5) * (5 - i))
        
        # stroke(255, 255, 255)
        x = (index - (4 - i)) * width / len(items) 
        blob(item, x, y)
        
    if len(fade_out) == 5:
        fade_out.pop()
    
    stroke(0, 0, 0)
    x = index * width / len(items)     
    blob(items[index], x, y)
    fade_out.append(items[index])
    
    index += 1
    
    if index >= len(items):
        index = 0
