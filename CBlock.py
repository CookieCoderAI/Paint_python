import pygame
from colors import *

class CBlock:
    def __init__(self, row, col, x, y,  width, color):
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def setcolor(self, color):
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

def make_CGrid(win):
    CGrid = []
    gap = 20
    
    for i in range(18):
        CGrid.append([])
        for j in range(19):
            block = CBlock(i, j,720+gap*i,70+gap*j, gap, (80+8*i,30+3*j, 125))
            CGrid[i].append(block)
            print(block.col, block.row, block.x, block.y, block.width)
    return CGrid

def draw_CGrid(win, grid):
    for i in range(18):
        for j in range(19):
            grid[i][j].draw(win)
