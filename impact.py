import math

def applyImpact(shellLoc, field, tankPosJ, tankHealthJ):
    for x in range(len(field)):
        for y in range(len(field[0])):
            if toBeRemoved(shellLoc, (x,y)):
                field[x][y] = 0

    fixTankPos(field, tankPosJ, tankHealthJ)
    
    for i in range(2):
        impactDistance = distance(shellLoc, tankPosJ[i])
        if impactDistance <= 5:
            damage = int((2/impactDistance) * 50)
        else:
            damage = 0
            
        tankHealthJ[i] -= damage
        
    return field, tankPosJ, tankHealthJ

def fixTankPos(field, tankPosJ, tankHealthJ):
    for i in range(2):

        tank = tankPosJ[i]
       
        try:
            while field[tank[0]][tank[1]-1] == 0:
                #print(field[tank[0]][tank[1]])
                #print(tank)
                tank = (tank[0], tank[1]-1)
            tankPosJ[i] = tank
        except:
            tankHealthJ[i] = 0
            tankPosJ[i] = (-1,-1)
    
    return tankPosJ, tankHealthJ

def toBeRemoved(shellLoc, groundLoc):
    if distance(shellLoc, groundLoc) < 4.5:
        return True
    return False

def distance(p1, p2):
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2    )
    