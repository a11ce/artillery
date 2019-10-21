GROUND = "\033[41m "
SKY    = "\033[100m "
RESET  = "\033[m"
TANK1  = "\033[45m "
TANK2  = "\033[46m "

def renderAll(tankPosJ, field, tankHealthJ):
    clearScreen()
    drawField(tankPosJ, field)
    #rawHud(tankHealthJ)
    
def clearScreen():
    print('\033c') 

def drawField(tankPosJ, field, shellLoc = ((0,0),(0,0)) ):
    fieldWidth = len(field)
    fieldHeight = len(field[0])

    printString = ""

    curCol = None
    
    for y in reversed(range(fieldHeight)):
        for x in range(fieldWidth):
            
            if( (x,y) == tankPosJ[0] ):
                if curCol != TANK1:
                    printString += TANK1
                else:
                    printString += " "
                curCol = TANK1
                
            elif( (x,y) == tankPosJ[1]):
                if curCol != TANK2:
                    printString += TANK2
                else:
                    printString += " "
                curCol = TANK2               
            else:
                if(field[x][y] == 1):
                    if curCol != GROUND:
                        printString += GROUND
                    else:
                        printString += " "
                    curCol = GROUND
                elif((x,y) == shellLoc[0] or (x,y) == shellLoc[1] ):
                    curCol = None
                    printString += RESET + "X"
                else:
                    if curCol != SKY:
                        printString+= SKY
                    else:
                        printString += " "
                    curCol = SKY
        printString += "\n"
    printString += RESET
    print(printString, end = "")