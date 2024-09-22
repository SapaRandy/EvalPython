def separer_phrase(phrase):
    mots = []
    separateurs = []
    mot_actuel = ""
    separateur_actuel = ""

    for char in phrase:
        if char.isalnum() or char in "'":
            if separateur_actuel:
                separateurs.append(separateur_actuel)
                separateur_actuel = ""
            mot_actuel += char
        else:
            if mot_actuel:
                mots.append(mot_actuel)
                mot_actuel = ""
            separateur_actuel += char

    if mot_actuel:
        mots.append(mot_actuel)
    if separateur_actuel:
        separateurs.append(separateur_actuel)

    return f"{phrase} ==> {[mots, separateurs]}"

if __name__ == "__main__":
    print(separer_phrase("J'ai découvert Python cette semaine"))
    print(separer_phrase("Un, deux, trois, quatre, cinq"))
    print(separer_phrase("Python  est  génial"))