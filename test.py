import pygame
from pygame.locals import *
import re
import time
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height+100))

O = pygame.image.load("images/O.png")
X = pygame.image.load("images/cross.png")
gameover = pygame.image.load("images/gameover.png")
X = pygame.transform.scale(X,(80,80))
O = pygame.transform.scale(O,(80,80))
gameover = pygame.transform.scale(gameover,(width,height+100))

line_color = (10, 10, 10)
Exitcode = 0
X_blocks = []
O_blocks = []
res = [0]*9
winner = "Noone"
turn = 'x'
def checkwinner(block):
    global turn
    global Exitcode
    global winner
    row = int(block/3)*3
    column = block%3
    print(row,column)
    if res[row] == res[row+1] == res[row+2]:
        Exitcode = 1
        winner = turn
    elif res[column] == res[column+3] == res[column+6]:
        Exitcode = 1
        winner = turn


    elif block%2 == 0 and ((res[0] == res[4] == res[8] and res[0]!=0) or (res[2] == res[4] == res[6] and  res[2]!=0)):
        Exitcode = 1
        winner = turn
    elif res[0] != 0 and res[1] != 0 and res[2] != 0 and res[3] != 0 and res[4] != 0 and res[5] != 0 and res[6] != 0 and res[7] != 0 and res[8] != 0:
        Exitcode = 2
    find_turn()

def find_turn():
    if Exitcode == 0:
        message = turn.upper() + "'s turn"
        screen.fill((0,0,0),(0,600,700,100))
        font = pygame.font.Font(None, 30)
        text = font.render(message, 1, (255, 255, 255))
        text_rect = text.get_rect(center=(width/2, 700-50))
        screen.blit(text, text_rect)
    elif Exitcode == 1:
        pygame.font.init()
        font1 = pygame.font.Font(None, 40)
        # message = winner + "lost"
        message = font1.render(winner +" Lost", True, (255,0,0))      
        textRect = message.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.fill(0)                                            
        screen.blit(gameover,(0,0))
        screen.blit(message, textRect)
        message = winner + " lost"
    else:
        pygame.font.init()
        font1 = pygame.font.Font(None, 40)
        message = font1.render("draw", True, (255,0,0))      
        textRect = message.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.fill(0)                                            
        screen.blit(gameover,(0,0))
        screen.blit(message, textRect)
    
    pygame.display.update()
def drawimage(p1):
    global turn 
    block = int(p1[0]/200)+int(int(p1[1]/200))*3
    if res[block] != 0:
        return
    else:
        if turn == 'x':
            screen.blit(X,(p1[0]+50,p1[1]+50))
            X_blocks.append(block)
            turn = 'o'
            res[block] = 1
        else:
            screen.blit(O,(p1[0]+50,p1[1]+50))
            O_blocks.append(block)
            turn = 'x'
            res[block] = 2

        checkwinner(block)

    pygame.display.update()
def reset():
    time.sleep(3)
    global Exitcode
    Exitcode = 0
    global res
    res = [0]*9
    global turn 
    turn = 'x'
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
    pygame.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 7)
    pygame.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pygame.draw.line(screen, line_color, (0, height/3*2), (width, height/3*2), 7)
    find_turn()

screen.fill((255, 255, 255))
pygame.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
pygame.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 7)
pygame.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
pygame.draw.line(screen, line_color, (0, height/3*2), (width, height/3*2), 7)
screen.fill((0,0,0),(0,600,700,100))
find_turn()
while(True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        position = pygame.mouse.get_pos()
        p1 = list(position)
        p1[0] = int(int(p1[0]/200)*200)
        p1[1] = int(int(p1[1]/200)*200)
        drawimage(p1)
        if Exitcode != 0:
            reset()
    pygame.display.update()
    