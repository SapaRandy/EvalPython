def trouver_triplets_somme_zero(liste):
    n = len(liste)
    resultat = []
    liste.sort()

    for i in range(n - 2):
        if i > 0 and liste[i] == liste[i - 1]:
            continue

        gauche = i + 1
        droite = n - 1

        while gauche < droite:
            somme = liste[i] + liste[gauche] + liste[droite]

            if somme == 0:
                resultat.append([liste[i], liste[gauche], liste[droite]])

                while gauche < droite and liste[gauche] == liste[gauche + 1]:
                    gauche += 1
                while gauche < droite and liste[droite] == liste[droite - 1]:
                    droite -= 1

                gauche += 1
                droite -= 1
            elif somme < 0:
                gauche += 1
            else:
                droite -= 1

    return resultat

if __name__ == "__main__":
    print(trouver_triplets_somme_zero([2, 7, 9, -9]))
    print(trouver_triplets_somme_zero([-33, -10, -8, -2, 1, 4, 1, 9, 10]))