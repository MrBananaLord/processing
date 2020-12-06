from random import seed
from random import uniform
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
R_RATIO = 50
ALPHA = 50
ALPHA_STEP = 3

class Item:
    def __init__(self, time, strength, bpm):
        self.time = time
        self.strength = strength
        self.bpm = bpm
        self.alpha = ALPHA
   
    def draw(self):
        fill(255, 255 - self.strength * R_RATIO /2, 0, self.alpha)
        stroke(0,0,0,0)
        circle(0, 0, self.strength * R_RATIO)
        
        noise = uniform(1,1.1)
        stroke(255,255,255,255)
        fill(0,0,0,0)
        ellipse(0, 0, self.bpm * R_RATIO, noise * self.bpm * R_RATIO / 2)
        
        self.alpha -= ALPHA_STEP
        
        if self.alpha < 0:
            self.alpha = 0
      
    def get_alpha(self):
        return self.alpha
      
def setup():
    global index
    global items
    global visible_items
    
    seconds = []
    table = loadTable("../data/20000.csv", "header")
    items = []
    visible_items = []
    
    bpm = 0
    for row in table.rows():
        if row.getString("bpm"):
            bpm = float(row.getString("bpm").replace(",", "."))
            
        if bpm != 0:
            items.append(
                Item(
                    float(row.getString("czas").replace(",", ".")),
                    float(row.getString("sila").replace(",", ".")),
                    bpm
                )
            )
            
    stroke(0,0,0,0)
    size(1440, 810)
    frameRate(60)
    background(0, 0, 0)
    
    index = 0

def draw():
#     return 1

# def mousePressed():
    global index
    global items
    global visible_items
    visible_items.append(items[index])
    
    translate(width/2, height/2)
    rotate(radians(index))
    background(0,0,0)
    for visible_item in visible_items:
        visible_item.draw()
    
    visible_items = filter(lambda e: e.get_alpha() > 0, visible_items)
    
    index += 1
    
    if index >= len(items):
        noLoop()
