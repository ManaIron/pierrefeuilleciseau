from random import randint
def choixOrdi():
    randomChoix = randint(0,2)
    if randomChoix == 0:
        randomChoix = "pierre"
    elif randomChoix == 1:
        randomChoix = "feuille"
    elif randomChoix == 2:
        randomChoix = "ciseaux"
    return randomChoix
def playRPS(nombreRounds):
    roundLost = 0
    roundWon = 0
    while roundLost != nombreRounds and roundWon != nombreRounds:
        randomChoix = choixOrdi()
        choixJoueur = input("pierre, feuille, ou ciseaux?")
        while choixJoueur not in ["pierre", "feuille", "ciseaux"]:
            choixJoueur = input("La saisie est invalide, rééssaye")
        if (choixJoueur == "pierre" and randomChoix == "feuille") or (choixJoueur == "ciseaux" and randomChoix == "pierre") or (choixJoueur == "feuille" and randomChoix == "ciseaux"):
            
            roundLost = roundLost + 1
            print("Tu as perdu", roundLost, "rounds")
            
        if (choixJoueur == "ciseaux" and randomChoix == "feuille") or (choixJoueur == "pierre" and randomChoix == "ciseaux") or (choixJoueur == "feuille" and randomChoix == "pierre"):
            
            roundWon = roundWon + 1
            print("Tu as gagné", roundWon,"rounds")
            
        if choixJoueur == randomChoix:
            print("Egalité, rejoue")
        if nombreRounds == roundLost:
            print("T'as perdu, mais tu as quand même gagné", roundWon, "rounds!")
        if nombreRounds == roundWon:
            print("Bien joué, tu as gagné! Tu as perdu", roundLost, "rounds, mais tu t'en sort bien")

playRPS(5)
