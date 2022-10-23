from constante import *
from affichage import *


def toggle_ami(button_ami, button_ordi, typeGame, cnv_text):

    if button_ami.config('relief')[-1] == 'sunken':
        button_ami.config(relief="raised")
    else:
        button_ami.config(relief="sunken")
        typeGame[0] = AMI
        if button_ordi.config('relief')[-1] == 'sunken':
            button_ordi.config(relief="raised")

    cnv_text.delete('all')
    cnv_text.create_text(COTE_CASE * 1.5, COTE_CASE / 2, text="Let's play !", fill="black",
                         font='Helvetica 18 bold')


def toggle_ordi(button_ami, button_ordi, typeGame, cnv_text):

    if button_ordi.config('relief')[-1] == 'sunken':
        button_ordi.config(relief="raised")
    else:
        button_ordi.config(relief="sunken")
        typeGame[0] = ORDI

        if button_ami.config('relief')[-1] == 'sunken':
            button_ami.config(relief="raised")
    cnv_text.delete('all')
    cnv_text.create_text(COTE_CASE * 1.5, COTE_CASE / 2, text="Let's play !", fill="black",
                         font='Helvetica 18 bold')


def reset_grid(cnv, grid, tour, typeGame, button_ami, button_ordi, cnv_text):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):
            grid[l][c] = '_'

    tour[0] = 0
    print("okk")
    draw_grid(cnv)

    if button_ordi.config('relief')[-1] == 'sunken':
        typeGame[0] = ORDI
        cnv_text.delete('all')
        cnv_text.create_text(COTE_CASE * 1.5, COTE_CASE / 2, text="Let's play !", fill="black",
                             font='Helvetica 18 bold')

    elif button_ami.config('relief')[-1] == 'sunken':
        typeGame[0] = AMI
        cnv_text.delete('all')
        cnv_text.create_text(COTE_CASE * 1.5, COTE_CASE / 2, text="Let's play !", fill="black",
                             font='Helvetica 18 bold')



