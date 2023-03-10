texte = ""

width = int(input("largeur: "))
height = int(input("hauteur: "))





for x in range(0, height):
    for y in range(0, width):
        if (y == 0 or y == width - 1):
            texte += "|"
        elif x == 0 or x == height - 1:
            texte += "-"
        else:
            texte += " "
    texte += "\n"
print(texte)
         



            


