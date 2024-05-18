import random

# Définition des combinaisons possibles et leur score associé
combinaisons = {
    "paire": 2,
    "brelan": 3,
    "suite": 4,
    "full": 5,
    "carré": 6,
}

# Définition des cartes spéciales et leur effet associé
cartes_speciales = {
    "vol_de_dés": "Lancez à nouveau les dés de votre adversaire.",
    "point_bonus": "Gagnez 5 points bonus.",
}

# Définition des variables du jeu
joueurs = ["Vous", "Dharmavir"]
scores = {joueur: 0 for joueur in joueurs}

# Fonction pour lancer les dés
def lancer_des(n):
    return [random.randint(1, 6) for _ in range(n)]

# Fonction pour obtenir le score d'une combinaison
def obtenir_score(combinaison, des):
    if combinaison == "paire":
        for i in range(1, 7):
            if des.count(i) == 2:
                return combinaisons[combinaison]
    elif combinaison == "brelan":
        for i in range(1, 7):
            if des.count(i) == 3:
                return combinaisons[combinaison]
    elif combinaison == "suite":
        if sorted(des) in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]):
            return combinaisons[combinaison]
    elif combinaison == "full":
        if sorted(des) in ([1, 1, 1, 2, 2], [2, 2, 2, 3, 3], [3, 3, 3, 4, 4], [4, 4, 4, 5, 5], [5, 5, 5, 6, 6]):
            return combinaisons[combinaison]
    elif combinaison == "carré":
        for i in range(1, 7):
            if des.count(i) == 4:
                return combinaisons[combinaison]
    return 0

# Fonction pour piocher une carte spéciale
def piocher_carte():
    return random.choice(list(cartes_speciales.keys()))

# Boucle principale du jeu
while True:
    # Tour de chaque joueur
    for joueur in joueurs:
        # Lancer les dés
        des = lancer_des(5)
        print(f"{joueur}, voici les dés que vous avez lancés : {des}")

        # Obtenir les scores pour chaque combinaison
        scores_combinaisons = {combinaison: obtenir_score(combinaison, des) for combinaison in combinaisons}

        # Afficher les scores
        print(f"Voici les scores pour chaque combinaison : {scores_combinaisons}")

        # Demander au joueur de choisir une combinaison
        combinaison_choisie = input("Choisissez une combinaison : ")
        score_obtenu = scores_combinaisons.get(combinaison_choisie, 0)

        # Ajouter le score obtenu au score total du joueur
        scores[joueur] += score_obtenu
        print
