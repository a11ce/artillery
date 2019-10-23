import shutil, sys 
import fieldGen, graphics, physics, ai
from getch import getch

termSize = shutil.get_terminal_size((80,40)) #defaults
SCREEN_WIDTH = termSize[0]
SCREEN_HEIGHT = termSize[1] - 4

def main():
    playAgain = True

    possiblePlayers = [("Human",askMove),
                       ("randomNormal (AI)", ai.randomNormal),
                       ("random45 (AI)", ai.randomNormal),
                       ("peaceBot (AI)", ai.peaceBot)
                      ]

    print("Select two players:\n")
    for idx, posPlayer in enumerate(possiblePlayers):
        print(str(idx+1) + ": " + posPlayer[0])
    players = [ possiblePlayers[int(input("\n> "))-1][1] for _ in range(2)]
    
    while playAgain:
        
        playAgain = playGame(players)

def playGame(moveTypeJ):

    tankPosJ, field = fieldGen.generateField(SCREEN_WIDTH,SCREEN_HEIGHT)

    tankHealthJ = [100, 100]
    dead = False
   
    while not (dead):

        graphics.renderAll(tankPosJ, field, tankHealthJ)

        dead, winner = checkDead(tankHealthJ)

        if dead:
            print(str(winner) + " wins!")
            
            return askToPlayAgain(getch)
        #print("\n\n\nEEEE\n\n\n")
        tankPosJ, tankHealthJ, field = playerMoves(moveTypeJ,tankPosJ, tankHealthJ, field)

def askToPlayAgain(getch):
    while(True):
        print("play again? y/n")
        inp = getch()

        if inp == 'y':
            return True
        elif inp == 'n':
            print("bye!")
            return False

def checkDead(tankHealthJ):
    if(tankHealthJ[0] <=  0 and tankHealthJ[1] <= 0):
        return True, "Nobody"
    if(tankHealthJ[0] <= 0):
        return True, "Player 2"
    if(tankHealthJ[1] <= 0):
        return True, "Player 1"
    return False, "A ghost"

def playerMoves(getJ, tankPosJ, tankHealthJ, field):
    print("Player 1 health is " + str(tankHealthJ[0]))
    print("Player 2 health is " + str(tankHealthJ[1]))
    print()
    movesJ = [getJ[0]("Player 1", False), getJ[1]("Player 2", True)]
    tankPosJ, tankHealthJ, field = physics.moves(tankPosJ, tankHealthJ, movesJ, field)

    return tankPosJ, tankHealthJ, field

def askMove(pName, facingLeft):

    print(pName + ", enter elevation angle: ", end="")
    angle = float(input())
    print(pName + ", enter shot power: ", end = "")
    power = float(input())
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    if facingLeft:
        angle = 180 - angle
    return (power, angle)

if __name__ == "__main__":
    main()