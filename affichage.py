from constante import *
from game_rules import *


def draw_grid(cnv):
    # Dessin plateau
    cnv.create_rectangle(0, 0, WIDTH_TAB,HEIGHT_TAB, fill="light gray")

    for i in range(0, NB_COLUMN + 1):

        x1 = 4 + i * (COTE_CASE + LINE_WIDTH / 2)
        x2 = x1
        y1 = 0
        y2 = HEIGHT_TAB

        cnv.create_line(x1, y1, x2, y2, width=5, fill='black')

    for j in range(0, NB_LINE + 1):

        y1 = 4 + j * (COTE_CASE + LINE_WIDTH / 2)
        y2 = y1
        x1 = 0
        x2 = WIDTH_TAB

        cnv.create_line(x1, y1, x2, y2, width=5, fill='black')


def draw_piece_grid(cnv, grid):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if grid[l][c] != '_':
                draw_piece(cnv, l, c, grid[l][c])


def draw_piece(cnv, l, c, char):

    x = c * (COTE_CASE + LINE_WIDTH / 2) + (COTE_CASE + LINE_WIDTH + 3) / 2
    y = l * (COTE_CASE + LINE_WIDTH / 2) + (COTE_CASE + LINE_WIDTH + 3) / 2
    r = COTE_CASE/2.5

    if char == 'o':
        create_circle(cnv, x, y, r, fill='black')
    else:
        create_circle(cnv, x, y, r, fill='white')


def create_circle(cnv, x, y, r, **kwargs):
    return cnv.create_oval(x - r, y - r, x + r, y + r, **kwargs)


def disp_win(tour, cnv_text):
    if pion_tour(tour[0]) == 'o':
        cnv_text.delete('all')
        cnv_text.create_text(COTE_CASE * 1.5, COTE_CASE / 2, text="Black win !", fill="black",
                             font='Helvetica 18 bold')
    else:
        cnv_text.delete('all')
        cnv_text.create_text(COTE_CASE * 1.5, COTE_CASE / 2, text="White win !", fill="black",
                             font='Helvetica 18 bold')

