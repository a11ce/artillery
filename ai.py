import random
import numpy as np


def randomNormal(pName, facingLeft):
    power = np.random.normal(loc=60, scale=10)
    angle = np.random.normal(loc=45, scale=10)
    if facingLeft:
        angle = 180 - angle
    return (power, angle)


def peaceBot(pName, facingLeft):
    return (100, 90)


def random45(pName, facingLeft):
    power = random.uniform(50, 70)
    angle = 45
    if facingLeft:
        angle = 180 - angle
    return (power, angle)
