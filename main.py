from tkinter import *
from affichage import *
from game_rules import *
import button


typeGame = NO_GAME







window = Tk()

window.title("Puissance 4")
window.geometry("1080x720")

cnv = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='light gray')

cnv.pack()
cnv.place(x=TAB_GAP, y=TAB_GAP)
draw_grid(cnv)


# txt_1 = Text(window, font='Helvetica 15 bold')
# txt_1.insert(INSERT, "Select a mode :")

# txt_1.place(x=2 * TAB_GAP + WIDTH_TAB, y=TAB_GAP)

button_ami = Button(text="Contre un ami", font='Helvetica 15 bold', background='light gray',
                    command=(lambda:button.toggle_ami(button_ami, button_ordi, typeGame)))

button_ami.place(x=2 * TAB_GAP + WIDTH_TAB, y=2 * TAB_GAP)

button_ordi = Button(text="Contre l'ordi", font='Helvetica 15 bold', background='light gray',
                     command=(lambda:button.toggle_ordi(button_ami, button_ordi, typeGame)))

button_ordi.place(x=2 * TAB_GAP + WIDTH_TAB, y=2.5 * TAB_GAP)

button_reset = Button(window, text="reset", font='Helvetica 15 bold', background='light gray',
                      command=(lambda: button.reset_grid(cnv)))


button_reset.place(x=2 * TAB_GAP + WIDTH_TAB, y=4 * TAB_GAP)




grid = [['_' for x in range(NB_COLUMN)] for y in range(NB_LINE)]
tour = [1]

cnv.bind("<Button-1>", lambda event: click_case(event, grid, tour, cnv))

# cnv.bind("<Button-1>", click_case)

window.mainloop()


"""
grid = [['_' for x in range(NB_COLUMN)] for y in range(NB_LINE)]

affiche_tab(grid)

end = False
tour = 0

while not end :

    colonne = choix_colonne(grid) - 1
    gravity(grid, colonne, tour)
    affiche_tab(grid)

    if victoire(grid, tour):
        print(f'Victoire, {pion_tour(tour)} ')
        end = True

    else:
        tour = tour + 1
        
"""
