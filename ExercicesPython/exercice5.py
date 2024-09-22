def jeu_plus_petit_plus_grand():
    print("Mémorisez un nombre entier entre 1 et 100, script va essayer de le retrouver, ne trichez pas :")

    min_val, max_val = 1, 100
    propositions = []
    reponses = []
    coups = 0

    while True:
        coups += 1
        proposition = (min_val + max_val) // 2
        propositions.append(proposition)

        reponse = input(f"script propose {proposition}... +, - ou G ? ").lower()
        reponses.append(reponse)

        if reponse == 'g':
            print(f"script a trouvé {proposition} en {coups} coups !!!")
            break
        elif reponse == '+':
            min_val = proposition + 1
        elif reponse == '-':
            max_val = proposition - 1
        else:
            print("Réponse invalide. Utilisez +, - ou G.")
            continue

        if min_val > max_val:
            print("Tricheur !!! Vos réponses sont incohérentes.")
            print(f"J'ai gagné par forfait en {coups} coups !!!")
            break

        if min_val == max_val:
            print(f"Le nombre que vous avez choisi est {min_val}.")
            print(f"J'ai trouvé en {coups} coups !!!")
            break

if __name__ == "__main__":
    jeu_plus_petit_plus_grand()