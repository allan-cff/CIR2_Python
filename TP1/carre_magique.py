#carre = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

def est_magique(carre):
    length = -1
    n = -1
    for ligne in carre:
        if length != len(ligne):
            if length == -1:
                length = len(ligne)
            else:
                return False
        if n != sum(ligne):
            if n == -1:
                n = sum(ligne)
            else:
                return False
    for i in range(length):
        colonne = [x[i] for x in carre]
        if length != len(colonne):
            return False
        if n != sum(colonne):
            return False
    return True


def generer_carre_magique(n):
    val = 1
    pos_x = n//2
    pos_y = 0
    new_carre = [[-1 for i in range(n)]for i in range(n)]
    while val <= n**2:
        if new_carre[pos_y][pos_x] != -1:
            pos_y += 1
            if pos_y == n:
                pos_y = 0
        print("x ", pos_x)
        print("y ", pos_y)
        new_carre[pos_y][pos_x] = val
        val += 1
        pos_x = pos_x - 1
        pos_y = pos_y - 1
        if pos_x == -1:
            pos_x = n-1
        if pos_y == -1:
            pos_y = n-1
        for l in new_carre:
            print(l)
    return new_carre

carre = generer_carre_magique(3)
print(est_magique(carre))