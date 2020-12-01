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
            
class Second:
    def __init__(self, id):
        self.id = id
        self.entries = {}
        
    def add_entry(self, time, strength):
        self.entries[time] = strength
            
    def draw(self, x, y):
        snowflake(self.entries.values(), x, y)
      
def setup():
    global index
    global alpha
    global seconds
    
    seconds = []
    table = loadTable("../data/200.csv", "header")
    
    for row in table.rows():
        time = float(row.getString("czas").replace(",", "."))
        second = next((x for x in seconds if x.id == int(time)), None)
        if second:
            second.add_entry(time, float(row.getString("sila").replace(",", ".")))
        else:
            second = Second(int(time))
            second.add_entry(time, float(row.getString("sila").replace(",", ".")))
            seconds.append(second)
                
    size(1440, 810)
    frameRate(60)
    background(255, 255, 255)
    
    index = 0
    alpha = 0

def draw():
    global index
    global table
    global alpha
    global seconds
    
    background(255, 255, 255)
    stroke(0, 0, 0, alpha)
    
    x = width / 2
    y = height / 2
    
    seconds[index].draw(x, y)
    
    alpha += 8 
    if alpha > 255:
        index += 1
        
        if index >= len(seconds):
            index = 0
        alpha = 0
