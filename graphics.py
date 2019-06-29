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
    
    for y in reversed(range(fieldHeight)):
        for x in range(fieldWidth):
            
            if( (x,y) == tankPosJ[0] ):
                printString += TANK1 + RESET
            elif( (x,y) == tankPosJ[1]):
                printString += TANK2 + RESET
            else:
                if(field[x][y] == 1):
                    printString += GROUND + RESET
                elif((x,y) == shellLoc[0] or (x,y) == shellLoc[1] ):
                    printString += "X" 
                else:
                    printString += SKY + RESET
        printString += "\n"
    print(printString, end = "")