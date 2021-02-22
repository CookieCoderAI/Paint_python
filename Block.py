import pygame
from colors import *

class Block:
    def __init__(self, row, col, width, color):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.color = color

    def setcolor(self, color):
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

def make_BGrid(rows, width):
    BGrid = []
    gap = width // rows
    
    for i in range(rows):
        BGrid.append([])
        for j in range(rows):
            block = Block(i, j, gap, WHITE)
            BGrid[i].append(block)
    return BGrid

def draw_BGrid(win, grid):
    for row in grid:
        for block in row:
            block.draw(win)