L = [8, 24, 48, 2, 16]
compteur = 0
for x in L:
    if x%3 == 0:
        compteur += 1
    else:
        compteur = compteur
print(compteur)

    
