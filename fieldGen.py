from random import randint

def generateField(width, height):

    field = [  
            [ 0 for _ in range(height)]
            for _ in range (width)]

    elevation = randint(int(height/10), int(height/2))
    
    tankPosJ = [[0,0],[0,0]]


    for x in range(width):
        
        for y in range(elevation):
            field[x][y] = 1

        if(x == int(width/10)):
            tankPosJ[0] = (x, elevation)
            field[x-1][elevation] = 0
        elif(x == int(width - (width/10))):
            tankPosJ[1] = (x, elevation)
            field[x-1][elevation] = 0
        elif(elevation < height/20):
            elevation += 1
        else:
           elevation += randint(-1, 1)
                    
        
    return tankPosJ, field 