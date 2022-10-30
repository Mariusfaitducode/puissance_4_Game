
from constante import *
import affichage
import game_rules as game


def choix_colonne_ordi(grid, tour, cnv):

    max = -1000
    final_l = None
    final_c = None

    filled = filled_colonne(grid)
    print(filled)

    for c in range(NB_COLUMN):

        l = coup_colonne(grid, c)

        if l > -1:

            grid[l][c] = game.pion_tour(tour)

            score = minimax(grid, tour + 1, 5 + filled, (l, c))

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
def minimax(grid, tour, profondeur, last_case):

    max = None
    (l, c) = last_case

    if victoire_with_case(l, c, grid):
    # if game.victoire(grid, tour):
        # print("vic detected")

        if game.pion_tour(tour - 1) == 'x':  # defaite

            return -100 - profondeur * 10

        else:
            return 100 + profondeur * 10

    elif game.egalite(grid, tour):
        print("end game")
        print(tour)
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

                    score = minimax(grid, tour + 1, profondeur-1, (l, c))

                    grid[l][c] = '_'

                    if score > max:
                        max = score

        elif game.pion_tour(tour) == 'x':

            max = 1000

            for c in range(NB_COLUMN):

                l = coup_colonne(grid, c)

                if l > -1:

                    grid[l][c] = game.pion_tour(tour)

                    score = minimax(grid, tour + 1, profondeur - 1, (l, c))

                    grid[l][c] = '_'

                    if score < max:
                        max = score

    return max


def coup_colonne(grid, colonne):

    l = 0
    while l < NB_LINE and grid[l][colonne] == '_':
        l += 1

    return l-1


def filled_colonne(grid):

    count = 0
    for c in range(NB_COLUMN):

        if grid[0][c] != '_':
            count += 1

    return count


def victoire_with_case(ligne, colonne, grid):

    pion = grid[ligne][colonne]

    for l in range(ligne-1, ligne+2):
        for c in range(colonne-1, colonne+2):

            if 0 <= l < NB_LINE and 0 <= c < NB_COLUMN:

                if grid[l][c] == pion and (l != ligne or c != colonne):
                    count = 2
                    count += search_next_case((ligne, colonne), (l, c), grid, pion)
                    count += search_next_case((l, c), (ligne, colonne),  grid, pion)
                    # print(count)
                    if count >= 4:
                        return True
    return False


def search_next_case(case1, case2, grid, pion):

    (l1, c1) = case1
    (l2, c2) = case2

    l3, c3 = 2 * l2 - l1, 2 * c2 - c1

    if 0 <= l3 < NB_LINE and 0 <= c3 < NB_COLUMN and grid[l3][c3] == pion:

        l4, c4 = 2 * l3 - l2, 2 * c3 - c2

        if 0 <= l4 < NB_LINE and 0 <= c4 < NB_COLUMN and grid[l4][c4] == pion:
            return 2

        return 1

    else:
        return 0
    