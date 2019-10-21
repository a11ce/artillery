import math, time
import graphics 
import impact

GRAVITY = 100 
POWER_MULTIPLIER = 1.4

TIME_STEP = 0.01
DISPLAY_EVERY = 1


def moves(tankPosJ, tankHealthJ, movesJ, field):

    POWER_MULTIPLIER = 1.4 * ( (len(field)/181.0))
    #GRAVITY = 100 * math.sqrt(math.sqrt((len(field[0])))/math.sqrt(math.sqrt(43)))
    GRAVITY = 100 * (43.0/(len(field[0])))
    #GRAVITY = 100 * ((len(field[0]))/43.0)
    #print(POWER_MULTIPLIER)
    movesImpacted = [False, False]
    cTime = 0
    simCount = 0
    vectorMovesJ = (vectorize(movesJ[0]), vectorize(movesJ[1])) 
    
    while not (movesImpacted[0] and movesImpacted[1]):
        simCount += 1
        
        cTime += TIME_STEP
        
        shellLocJ = (
                    (dX(cTime, vectorMovesJ[0][0]) + tankPosJ[0][0], dY(cTime, vectorMovesJ[0][1]) + tankPosJ[0][1]),
                    (dX(cTime, vectorMovesJ[1][0]) + tankPosJ[1][0], dY(cTime, vectorMovesJ[1][1]) + tankPosJ[1][1])
                    )

        for i in range(2):
            if not movesImpacted[i]:
                if impacted(shellLocJ[i], field):
                    field, tankPosJ, tankHealthJ = impact.applyImpact(shellLocJ[i], field, tankPosJ, tankHealthJ)
                    #print(tankPosJ)
                    movesImpacted[i] = True
                    
        shellLocJint = ( tuple((  tuple((int(x) for  x in  shellLoc )) for shellLoc in shellLocJ  )))
        if( simCount % DISPLAY_EVERY == 0):
            #print("DISP")
            #print(movesImpacted)
            graphics.drawField(tankPosJ, field, shellLocJint)
            graphics.clearScreen()
        time.sleep(TIME_STEP)

    return tankPosJ, tankHealthJ, field
        
def vectorize(move):
    return (POWER_MULTIPLIER* move[0] * math.cos(math.radians(move[1])), POWER_MULTIPLIER * move[0] * math.sin(math.radians(move[1])))

def dY(time, Vyi):
    return ( (Vyi * time) - ( 0.5 * GRAVITY * time * time ))

def dX(time, Vxi):
    return ((Vxi * time) )

def impacted(shellLoc, field):
    if(shellLoc[1] > len(field[0])):
        return False
    try:
        if(field[int(shellLoc[0])][int(shellLoc[1])] == 1):
            #print("Impact at " + str(shellLoc))
            return True
    except:
        print("Shell out of bounds")
        return True
        
    return False