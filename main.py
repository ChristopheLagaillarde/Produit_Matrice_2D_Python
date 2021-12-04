try:
    nb_ligne_colonne_M1_M2 = int(input("saisir le nombre de ligne de la matrice M1"
                                       "/ le nombre de colonne de la matrice M2"))
    nb_colonne_M1 = int(input("saisir le nombre de colonne de la matrice M1"))
    nb_ligne_M2 = int(input("saisir le nombre de ligne de la matrice M2"))

    M1 = []
    M2 = []

    for i in range(nb_ligne_colonne_M1_M2):
        ligne_actuel = []
        for j in range(nb_colonne_M1):
            ligne_actuel.append(int(input("M1 =")))
        M1.append(ligne_actuel)

    for i in range(nb_ligne_M2):
        ligne_actuel = []
        for j in range(nb_ligne_colonne_M1_M2):
            ligne_actuel.append(int(input("M2 =")))
        M2.append(ligne_actuel)

    M3 = [[0 for k in range(nb_ligne_colonne_M1_M2)] for t in range(nb_ligne_colonne_M1_M2)]

    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                M3[i][j] += (M1[i][k] * M2[k][j])

    print(M1)
    print(M2)
    print(M3)

except ValueError:
    print("Saisie non valide")