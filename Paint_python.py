import pygame

WIDTH = 700
WIDTH2 = 800

WIN1 = pygame.display.set_mode((WIDTH2, WIDTH))
#WIN2 = pygame.display.set_mode((WIDTH2, WIDTH2))

pygame.display.set_caption("Paint - Pygame")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Block:
    def __init__(self, row, col, width, color):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, gap*i),(width, gap*i))
    for j in range(rows+1):
        pygame.draw.line(win, GREY, (gap*j, 0),(gap*j, width))


def make_BGrid(rows, width, color):
    BGrid = []
    gap = width // rows
    
    for i in range(rows):
        BGrid.append([])
        for j in range(rows):
            block = Block(i, j, gap, color)
            BGrid[i].append(block)
    return BGrid

def draw_BGrid(win, grid):
    for row in grid:
        for block in row:
            block.draw(win)

def main(win):
    ROWS=50
    
    color = WHITE

    run = True
    while run:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                run = False

        WIN1.fill(WHITE)
        grid = make_BGrid(ROWS, WIDTH, color)
        draw_BGrid(win, grid)
        draw_grid(win, ROWS, WIDTH)
        
        pygame.display.update()

main(WIN1)