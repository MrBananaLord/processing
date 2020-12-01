from random import seed
from random import randint

def setup():
    global index
        
    size(1440, 810)
    frameRate(60)
    background(255, 255, 255)
    
    noStroke()

    index = 0
    

def draw():
    global index
    
    background(255, 255, 255)
    fill(0, 0, 0, index)
    circle(width / 2, height / 2, 100)
    index += 8
    if index > 255:
        index = 0
        
