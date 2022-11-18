
def afficherMorpion(tab):
    #Afficher le premier tableau
    print(tab[0])
    #Afficher le deuxieme tableau
    print(tab[1])
    #Afficher le troisieme tableau
    print(tab[2])

def verifAlign(tablo):
    #on fait une boucle pour verifier chaque ligne horizontale puis verticale
    for x in range(3):
        #Verification horizontale pour les X
        if tablo[x][0] == 'X' and tablo[x][1] == 'X' and tablo[x][2] == 'X' :
            #Renvoi X
            return 'X'
        #Verification horizontale pour les O
        elif tablo[x][0] == 'O' and tablo[x][1] == 'O' and tablo[x][2] == 'O' :
            #Renvoi O
            return 'O'
        #Verification veticale pour les X
        elif tablo[0][x] == 'X' and tablo[1][x] == 'X' and tablo[2][x] == 'X' :
            #Renvoi X
            return 'X'
        #Verification veticale pour les O
        elif tablo[0][x] == 'O' and tablo[1][x] == 'O' and tablo[2][x] == 'O' :
            #Renvoi O
            return 'O'
    #Verification de la premiere diagonale pour X
    if tablo[0][0] == 'X' and tablo[1][1] == 'X' and tablo[2][2] == 'X' :
         #Renvoi X
        return 'X'
    #Verification de la premiere diagonale pour O
    elif tablo[0][0] == 'O' and tablo[1][1] == 'O' and tablo[2][2] == 'O' :
        #Renvoi O
        return 'O'
    #Verification de la deuxieme diagonale pour X
    elif tablo[0][2] == 'X' and tablo[1][1] == 'X' and tablo[2][0] == 'X' :
         #Renvoi X
        return 'X'
    #Verification de la deuxieme diagonale pour O
    elif tablo[0][2] == 'O' and tablo[1][1] == 'O' and tablo[2][0] == 'O' :
        #Renvoi O
        return 'O'

def morpion() : 
    #on initialise les tableaux du morpion
    tab0 = ['7','8','9']
    tab1 = ['4','5','6']
    tab2 = ['1','2','3']
    #on stock tout les tableaux dans un tableau
    tableau = [tab0,tab1,tab2]
    #on initialise un compteur a 0
    compteur = 0
    #on affiche le morpion
    afficherMorpion(tableau)
    #Tant que le compteur est inférieur a 9 ()
    while compteur < 9 :
        #Récupérer la donné du joueur1
        playerOne = input()
        #Si le joueur 1 a choisi 1
        if playerOne == '1' :
            #Si dans la table 3 la première valeur est 1
            if tab2[0] == '1':
                #Alors la changer en X
                tab2[0] = 'X'
                #Afficher le nouveau tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si le joueur 1 choisi 2
        elif playerOne == '2' :
            #Si dans la table 3 la deuxième valeur est 2
            if tab2[1] == '2':
                #Alors changer la valeur par X
                tab2[1] = 'X'
                #Afficher le nouveau tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déja utilisé
                print("emplacement deja utilisé")
        #Si le joueur 1 choisis 3
        elif playerOne == '3' :
            #Si dans la table 3 la 3eme valeur est 3
            if tab2[2] == '3':
                #Alors la remplacer par X
                tab2[2] = 'X'
                #Mettre a jour le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utiliser
                print("emplacement deja utilisé")
        #Si le joueur 1 choisi 4
        elif playerOne == '4' :
            #Si dans la table 2 la première valeur est 4
            if tab1[0] == '4':
                #Alors la remplacer par X
                tab1[0] = 'X'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si le joueur 1 choisi 5
        elif playerOne == '5' :
            #Si dans la table 2 la 2ème valeur est 5
            if tab1[1] == '5':
                #Alors changer la valeur pour X
                tab1[1] = 'X'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si le joueur 1 choisi 6
        elif playerOne == '6' :
            #Si dans la table 2 la 3ème valeur est 6
            if tab1[2] == '6':
                #Alors changer la valeur pour X
                tab1[2] = 'X'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si le joueur 1 choisi 7
        elif playerOne == '7' :
            #Si dans la table 1 la première valeur est 7
            if tab0[0] == '7':
                #Alors changer cette valeur pour X
                tab0[0] = 'X'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si le joueur 1 choisi 8
        elif playerOne == '8' :
            #Si dans la table 1 la 2ème valeur est 8 
            if tab0[1] == '8':
                #Alors cahnger cette valeur pour X
                tab0[1] = 'X'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si le joueur 1 choisi 9
        elif playerOne == '9' :
            #Si dans la table 1 la 3ème valeur est 9
            if tab0[2] == '9':
                #Alors changer la valeur pour X
                tab0[2] = 'X'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si la fonction verifAlign() renvoi 'X' alors
        if verifAlign(tableau) == 'X' :
            #Print que le joueur 1 gagne
            print("Le player One a gagné")
            return
        ##Si la fonction verifAlign() renvoie 'O' alors
        elif verifAlign(tableau) == 'O':
            #Afficher que le joueur 2 a gagné
            print("Le player Two a gagné")
            return

        #Récupérer la donnée du joueur 2
        playerTwo = input()
        #Si le joueur 2 choisi 1
        if playerTwo == '1' :
            #Si dans la table 3 la première valeur est 1
            if tab2[0] == '1':
                #Alors la changer en O
                tab2[0] = 'O'
                #Afficher le nouveau tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si le joueur 2 choisi 2
        elif playerTwo == '2' :
            #Si dans la table 3 la deuxième valeur est 2
            if tab2[1] == '2':
                #Alors changer la valeur par O
                tab2[1] = 'O'
                #Afficher le nouveau tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utiliser
                print("emplacement deja utilisé")
        #Si le joueur 2 choisis 3
        elif playerTwo == '3' :
            #Si dans la table 3 la 3eme valeur est 3
            if tab2[2] == '3':
                #Alors la remplacer par O
                tab2[2] = 'O'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
                #Sinon
            else:
                #Écrire que l'emplacement est déjà utiliser
                print("emplacement deja utilisé")
        #Si le joueur 2 choisi 4
        elif playerTwo == '4' :
            #Si dans la table 2 la première valeur est 4
            if tab1[0] == '4':
                #Alors la remplacer par O
                tab1[0] = 'O'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utiliser
                print("emplacement deja utilisé")
        #Si le joueur 2 choisi 5
        elif playerTwo == '5' :
            #Si dans la table 2 la 2ème valeur est 5
            if tab1[1] == '5':
                #Alors la remplacer par O
                tab1[1] = 'O'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utiliser
                print("emplacement deja utilisé")
        #Si le joueur 2 choisi 6
        elif playerTwo == '6' :
            #Si dans la table 2 la 3ème valeur est 6
            if tab1[2] == '6':
                #Alors remplacer la valeur par O
                tab1[2] = 'O'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utiliser
                print("emplacement deja utilisé")
        #Si le joueur 2 choisi 7
        elif playerTwo == '7' :
            #Si dans la table 1 la première valeur est 7
            if tab0[0] == '7':
                #Alors remplacer la valeur par O
                tab0[0] = 'O'
                #Afficher le tabeau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si le joueur 2 choisi 8
        elif playerTwo == '8' :
            #Si dans la table 1 la 2ème valeur est 8 
            if tab0[1] == '8':
                #Alors remplacer la valeur par O
                tab0[1] = 'O'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")
        #Si le joueur 2 choisi 9
        elif playerTwo == '9' :
            #Si dans la table 1 la 3ème valeur est 9
            if tab0[2] == '9':
                #Alors remplacer la valeur par O
                tab0[2] = 'O'
                #Afficher le tableau
                afficherMorpion(tableau)
                #Ajouter 1 au compteur
                compteur = compteur + 1
            #Sinon
            else:
                #Écrire que l'emplacement est déjà utilisé
                print("emplacement deja utilisé")

        #Si varifAligh renvoie X
        if verifAlign(tableau) =='X' :
            #Écrire que le joueur 1 a gagné
            print("Le player One a gagné")
            return
            #Si verifAlign revoie O
        elif verifAlign(tableau) == 'O':
            #Écrire que le joueur 2 a gagné
            print("Le player Two a gagné")
            return
morpion()