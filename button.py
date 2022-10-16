from constante import *
from affichage import *


def toggle_ami(button_ami, button_ordi, typeGame):

    if button_ami.config('relief')[-1] == 'sunken':
        button_ami.config(relief="raised")
    else:
        button_ami.config(relief="sunken")
        typeGame = AMI
        if button_ordi.config('relief')[-1] == 'sunken':
            button_ordi.config(relief="raised")


def toggle_ordi(button_ami, button_ordi, typeGame):

    if button_ordi.config('relief')[-1] == 'sunken':
        button_ordi.config(relief="raised")
    else:
        button_ordi.config(relief="sunken")
        typeGame = ORDI

        if button_ami.config('relief')[-1] == 'sunken':
            button_ami.config(relief="raised")

def reset_grid(cnv):

    grid = [['_' for x in range(NB_COLUMN)] for y in range(NB_LINE)]
    print("okk")
    draw_grid(cnv)