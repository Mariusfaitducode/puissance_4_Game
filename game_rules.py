from constante import *
import affichage
import intelligence as ordi


def affiche_tab(grid):

    for x in range(0, NB_LINE):
        print()
        print('| ', end='')
        for y in range(0, NB_COLUMN):
            print(grid[x][y], end=' | ')


def click_case(event, grid, tour, cnv, typeGame, cnv_text):

    if typeGame[0] != NO_GAME:
        colonne = int(event.x / (WIDTH_TAB / NB_COLUMN))

        if 0 <= colonne < 7 and grid[0][colonne] == '_':
            print(colonne)
            ligne = gravity(grid, colonne, tour[0], cnv)
            cnv.update()

            if ordi.victoire_with_case(ligne, colonne, grid):
                print(f'Victoire, {pion_tour(tour[0])} ')
                disp_win(tour, cnv_text)
                typeGame[0] = NO_GAME

            else:
                tour[0] += 1

                if typeGame[0] == ORDI:
                    ordi.choix_colonne_ordi(grid, tour[0], cnv)
                    cnv.update()

                    if victoire(grid, tour[0]):
                        print(f'Victoire, {pion_tour(tour[0])} ')
                        disp_win(tour, cnv_text)
                        typeGame[0] = NO_GAME
                    else:
                        tour[0] += 1


def choix_colonne(grid):

    condition = True

    while condition:
        print('Colonne =', end='')
        rep = input()
        colonne = int(rep)

        if 0 < colonne < 8 and grid[0][colonne-1] == '_':
            print('Ok')
            return colonne


def pion_tour(tour):

    if tour % 2 == 0:
        return 'x'
    else:
        return 'o'


def gravity(grid, colonne, tour, cnv):
    x = 1
    condition = True

    while condition:

        if x == NB_LINE or grid[x][colonne] != '_':
            grid[x - 1][colonne] = pion_tour(tour)
            affichage.draw_piece(cnv, x-1, colonne, pion_tour(tour))

            condition = False

        else:
            x = x + 1
    return x - 1


def disp_win(tour, cnv_text):
    if pion_tour(tour[0]) == 'o':
        cnv_text.delete('all')
        cnv_text.create_text(COTE_CASE * 1.5, COTE_CASE / 2, text="Black win !", fill="black",
                             font='Helvetica 18 bold')
    else:
        cnv_text.delete('all')
        cnv_text.create_text(COTE_CASE * 1.5, COTE_CASE / 2, text="White win !", fill="black",
                             font='Helvetica 18 bold')


def victoire(grid, tour):

    for i in range(0, NB_LINE):
        for z in range(0, 4):
            compte = 0
            for j in range(z, z+4):

                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True

    for j in range(0, NB_COLUMN):
        for z in range(0, 3):
            compte = 0
            for i in range(z, z+4):
                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True

    for z in range(0, 4):
        for y in range(0, 3):
            compte = 0
            for j in range(z, z+4):
                i = j + y - z
                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True

    for y in range(5, 2, -1):
        for z in range(0, 4):
            compte = 0
            for i in range(y, y-4, -1):
                j = y - i + z
                if grid[i][j] == pion_tour(tour):
                    compte = compte + 1
                    if compte == 4:
                        return True


def egalite(grid, tour):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            if grid[l][c] == '_':
                return False
    if victoire(grid, tour):
        return False

    return True
