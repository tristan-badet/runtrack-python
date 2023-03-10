texte = ""

width = int(input("largeur: "))
height = int(input("hauteur: "))
compteur = 1




for x in range(0, height):
    for y in range(0, width):
        if ((y == 0 or y == width - 1) and (x == 0 or x == height - 1)):
            texte += "+"
        elif (y == 0 or y == width - 1):
            texte += "|"
        elif x == 0 or x == height - 1:
            texte += "-"
        elif ((y == width - compteur)):
            texte += " "
        else:
            texte += "#"
    texte += "\n"
    compteur += 1
print(texte)
         