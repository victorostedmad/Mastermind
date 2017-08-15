import pygame
import sys
from random import randint

pygame.init()
buttonPressed = False
turn = 0
#Baggrund
height = 550
width = 1300
screen = pygame.display.set_mode((width, height))
grey = [52, 73, 94]
screen.fill(grey)
colours = ["red","green","blue","yellow","black","white"]
drawnPins = ["blank", "blank", "blank", "blank", "blank", "blank"]
emptyPins = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

isPinEmpty = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

pointPins = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

coloursPicked = [0,0,0,0]
pins = [pygame.image.load('redPin.png').convert(),
            pygame.image.load('greenPin.png').convert(),
            pygame.image.load('bluePin.png').convert(),
            pygame.image.load('yellowPin.png').convert(),
            pygame.image.load('blackPin.png').convert(),
            pygame.image.load('whitePin.png').convert(),
            pygame.image.load('emptyPin.png').convert(),
            pygame.image.load('nextPin.png').convert()]
    
emptyPin = pygame.image.load('emptyPin.png').convert()
dis = 105

nextRoundIA = pygame.image.load('emptyPin.png').convert()
nextRoundA = 0
blackPoint = pygame.image.load('blackPoint.png').convert()
whitePoint = pygame.image.load('whitePoint.png').convert()
#Tegning af brættet

def Graphics():
    for x in range (0,6):
        drawnPins[x]=screen.blit(pins[x], (150+x*dis,450))
    for x in range (0,4):
        for y in range (0,10):
            emptyPins[y][x] = screen.blit(emptyPin, (150+y*100,100*x))
    pygame.display.update()
    readyToProceedA = screen.blit(pins[6], (780,450))


def WhichRow(turn):
    newTurn = 0
    for x in range (0,4):
        if isPinEmpty[turn][x] == 0:
            newTurn = -1
            
    if newTurn == -1:
        newTurn = 0
    else:
        newTurn = 1
    return newTurn






def colourPickerAI():
    pickedColoursInFunction = ["blank","blank","blank","blank"] 

    for x in range (0,4): #Each value in pickedColoursInFun gets changed for a color 
        colourIndex = randint(0,5)
        alreadyPicked = False
        
        while True: #Making sure that the color isnt picked
            for i in range (0,4):
               if pickedColoursInFunction[i] == colours[colourIndex]: #Making a new number in case its already picked
                    alreadyPicked = True
                    colourIndex = randint(0,5)
               
            if alreadyPicked == False: #If it wasnt picked, we stop the infinte loop 
                break
            
            alreadyPicked = False
        pickedColoursInFunction[x] = colours[colourIndex]
    return pickedColoursInFunction ;






def whitePointCounter(a,b):
    points = 0;
    for y in range (0,4): 
        for x in range (0,4):
            if a[x] == b[y]:
                points = points + 1
    return points ;


def blackPointCounter(a,b):
    points = 0;
    for x in range (0,4):
        if a[x] == b[x]:
            points = points + 1
    return points ; 








def DrawPoints(b,w,x,y):
    point1 = 0
    point2 = 0
    print (str(b) + str(w))
    for a in range(b):
        if point1 == 2:
            point2 = point2 + 1
            point1 = 1
        else:
            point1 = point1 + 1
        pointPins[0][0]= screen.blit(blackPoint, (11*point1-11+x,11*point2+y))
    for a in range(w):
        if point1 == 2:
            point2 = point2 + 1
            point1 = 1
        else:
            point1 = point1 + 1
        print ("white point")
        pointPins[0][0]= screen.blit(whitePoint, (11*point1-11+x,11*point2+y))
    





ranOnce = False

def MainGame(turn):
    
    clock = pygame.time.Clock()
    fps = 30
    readyToProceed = 0
    buttonPressed = False
    while True: #Here, I check for mouseclicks over the different pins
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() 

                for x in range (0,6):  
                    if drawnPins[x].collidepoint(mouse_pos):
                        buttonPressed = True
                        ranOnce = True    
                        whichButton = x
                        
                if buttonPressed == True:
                    if turn == 0:
                        whichRow = 0
                        turn = turn + 1
                    for x in range (0,4):
                        if emptyPins[whichRow][x].collidepoint(mouse_pos):
                            ranOnce = False
                            print (ranOnce)
                            emptyPins[whichRow][x] = screen.blit(pins[whichButton], (150+whichRow*100,100*x))
                            coloursPicked[x] = colours[whichButton]
                            isPinEmpty [whichRow][x] = 1
                            readyToProceedA = screen.blit(pins[6], (780,450))
                            readyToProceed = WhichRow(whichRow)
                            
                    if readyToProceed == 1:
                        if ranOnce == False:
                            readyToProceedA = screen.blit(pins[7], (780,450))
                        
                        if readyToProceedA.collidepoint(mouse_pos):
                            readyToProceedA = screen.blit(pins[6], (780,450))
                            ranOnce = True
                            blackPoints = blackPointCounter(coloursToGuess,coloursPicked)
                            whitePoints = whitePointCounter(coloursToGuess,coloursPicked) - blackPoints
                            if blackPoints < 4:
                                whichRow = WhichRow(whichRow)+whichRow
                                buttonPressed = False
                                print (whichRow)
                                print (blackPoints)
                                print (whitePoints)
                                print (coloursPicked)
                                print (coloursToGuess)
                                DrawPoints(blackPoints, whitePoints,89+100*whichRow,410)
                                break
                            else:
                                myfont = pygame.font.SysFont("monospace", 42)
                                label = myfont.render("YOU WON!", 1, (10,10,10))
                                
                                tdH = label.get_rect().height
                                tdW = label.get_rect().width
                                pygame.draw.rect(screen, (100, 100, 100), (width/2-200,height/2-200,400,250))
                                screen.blit(label, (width/2-tdW/2, height/2-100))
                                pygame.display.update()
                                DrawPoints(blackPoints, whitePoints,89+100*(whichRow+1),410)
                
                    
                        
   
            
        
        
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    sys.exit


def MainMenu() :
    clock = pygame.time.Clock()
    fps = 30
    Graphics()
    MainGame(turn)

coloursToGuess = colourPickerAI()        
MainMenu()
