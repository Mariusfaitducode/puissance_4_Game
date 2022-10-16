
from constante import *
import affichage
import game_rules as game


def choix_colonne_ordi(grid, tour, cnv):

    max = -1000
    final_l = None
    final_c = None

    for c in range(NB_COLUMN):

        l = coup_colonne(grid, c)

        if l > -1:

            grid[l][c] = game.pion_tour(tour)
            score = minimax(grid, tour + 1, 3)
            grid[l][c] = '_'

            print(score)

            if score > max:
                max = score
                final_l = l
                final_c = c

            if score == max and c == 3:
                final_l = l
                final_c = c

    grid[final_l][final_c] = game.pion_tour(tour)
    affichage.draw_piece(cnv, final_l, final_c, game.pion_tour(tour))


# 'x' == ordi
def minimax(grid, tour, profondeur):

    max = None

    if game.victoire(grid, tour):
        # print("vic detected")

        if game.pion_tour(tour) == 'x':  # defaite

            return -100 - profondeur * 10

        else:
            return 100

    elif game.egalite(grid, tour):
        # print("end game")
        return 0

    elif profondeur < 0:
        # print("prof")
        return 0

    else:
        if game.pion_tour(tour) == 'o':

            max = -1000

            for c in range(NB_COLUMN):

                l = coup_colonne(grid, c)

                if l > -1:

                    grid[l][c] = game.pion_tour(tour)

                    score = minimax(grid, tour + 1, profondeur-1)

                    grid[l][c] = '_'

                    if score > max:
                        max = score

        elif game.pion_tour(tour) == 'x':

            max = 1000

            for c in range(NB_COLUMN):

                l = coup_colonne(grid, c)

                if l > -1:

                    grid[l][c] = game.pion_tour(tour)

                    score = minimax(grid, tour + 1, profondeur - 1)

                    grid[l][c] = '_'

                    if score < max:
                        max = score

    return max


def coup_colonne(grid, colonne):

    l = 0
    while l < NB_LINE and grid[l][colonne] == '_':
        l += 1

    return l-1







