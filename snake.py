import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube():
    pass


class snake(object):
    body=[]
    turns={}
    def __init__(self,color,pos):
        self.color=color
        #self.head=cube(pos) #to know the head position at all times
        #self.body.append(self.head)
        self.dirnx=0 #direction x for the snake, when x=1 y=0 and vice versa
        self.dirny=1
    
    def move(self):
        #when left is clicked the rest of the snake moves until it reaches the point where the head turned left
        for event in pygame.event.get() :
            if event.type==pygame.QUIT :
                pygame.quit()


def drawGrid(w, rows ,surface):
    sizeBtwn= w // rows
    x=0
    y=0
    for l in range(rows):
        x=x+sizeBtwn
        y=y+sizeBtwn
        #vertical line of the grid
        pygame.draw.line(surface,(255,255,255), (x,0),(x,w))
        #horizontal line of the grid
        pygame.draw.line(surface,(255,255,255), (0,y),(w,y))

def redrawWindow(surface):
    global rows,width
    surface.fill((0,0,0))
    drawGrid(width,rows,surface)
    pygame.display.update()




def main() :
    global width,rows
    width=500
    rows=20
    pygame.init()

    win = pygame.display.set_mode ((width ,width) )
    s= snake((255,0,0),(10,10))
    clock= pygame.time.Clock()
    #Chang the title of the game window win.dis
    flag= True
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
        s.move()
    
    



main()
