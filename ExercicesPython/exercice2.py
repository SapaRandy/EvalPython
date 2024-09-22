def addition_listes(n1, n2):
    if len(n2) > len(n1):
        n1, n2 = n2, n1

    resultat = []
    retenue = 0

    for i in range(1, len(n1) + 1):
        chiffre1 = n1[-i]
        chiffre2 = n2[-i] if i <= len(n2) else 0
        somme = chiffre1 + chiffre2 + retenue
        nouveau_chiffre = somme % 10
        retenue = somme // 10
        resultat.insert(0, nouveau_chiffre)

    if retenue > 0:
        resultat.insert(0, retenue)

    return  f"résultat {resultat}"

if __name__ == "__main__":
    print(addition_listes( [1,2,3],[7]))