from constante import *
import affichage


def affiche_tab(grid):

    for x in range(0, NB_LINE):
        print()
        print('| ', end='')
        for y in range(0, NB_COLUMN):
            print(grid[x][y], end=' | ')


def click_case(event, grid, tour, cnv):

    print("clicked at", event.x, event.y)

    colonne = int(event.x / (WIDTH_TAB / NB_COLUMN))

    if 0 <= colonne < 7 and grid[0][colonne] == '_':
        print(colonne)
        gravity(grid, colonne, tour, cnv)

        if victoire(grid, tour):
            print(f'Victoire, {pion_tour(tour)} ')

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

    if tour[0] % 2 == 0:
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
