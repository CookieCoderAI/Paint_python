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

def make_CGrid(win, colorval):
    CGrid = []
    gap = 20
    
    for i in range(20):
        CGrid.append([])
        for j in range(20):
            block = CBlock(i, j,720+gap*i,70+gap*j, gap, (int(13.47*i),int(13.47*j), colorval))
            CGrid[i].append(block)
            print(block.col, block.row, block.x, block.y, block.width)
    return CGrid

def draw_CGrid(win, grid):
    for i in range(20):
        for j in range(20):
            grid[i][j].draw(win)
