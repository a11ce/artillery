import random

def random45(pName, facingLeft):
    power = 45
    angle = random.randint(50,100)
    if facingLeft:
        angle = 180 - angle
    return (power,angle)