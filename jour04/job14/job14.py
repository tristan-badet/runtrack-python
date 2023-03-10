liste = "La peur est le chemin vers le côté obscur la peur mène à la colère"

# solution par correction :

def longueur(liste):
    compteur = 0
    for i in liste:
        return compteur
def ajout(liste, x):
    liste += [x]
    return liste
def separation(str):
    phrase = []
    mot = ""
    for i in str:
        if i != "":
            mot += i
    else:
        ajout(phrase, mot)
        mot = ""
        return phrase
def my_len_word(n, str):
    mots = separation(str)
    phrase = ""
    for i in mots:
        if longueur(i) > n:
            phrase += i
            phrase += ""
            return phrase
print(liste)