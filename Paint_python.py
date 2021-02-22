import pygame
from Block import *
from CBlock import *
from colors import *

WIDTH = 700
WIDTH2 = 1100

WIN1 = pygame.display.set_mode((WIDTH2, WIDTH))

pygame.display.set_caption("Paint - Pygame")

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, gap*i),(width, gap*i))
    for j in range(rows+1):
        pygame.draw.line(win, GREY, (gap*j, 0),(gap*j, width))

def draw_colorgrid(win):
    gap = 20
    for i in range(20):
        pygame.draw.line(win, GREY, (720, 70 + gap*i), (1080, 70 + gap*i))
    for j in range(18+1):
        pygame.draw.line(win, GREY, (720 + gap*j, 70), (720 + gap*j, 450))

def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

def main(win):
    ROWS=50

    grid = make_BGrid(ROWS, WIDTH)
    cgrid = make_CGrid(win)
    color = WHITE

    print(cgrid[3][4].row, cgrid[3][4].col, cgrid[3][4].x, cgrid[3][4].y, cgrid[3][4].width ,cgrid[3][4].color)
    run = True
    while run:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                run = False
            pos = pygame.mouse.get_pos()
            if pos < (700, 700):
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, WIDTH)
                    block = grid[row][col]
                    block.setcolor(BLACK)
                if pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, WIDTH)
                    block = grid[row][col]
                    block.setcolor(WHITE)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for row in grid:
                            for block in row:
                                block.setcolor(WHITE)
            else:
                pass


        WIN1.fill(WHITE)
        draw_BGrid(win, grid)
        draw_CGrid(win, cgrid)
        draw_colorgrid(win)
        draw_grid(win, ROWS, WIDTH)
        
        pygame.display.update()

main(WIN1)