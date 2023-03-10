message = "Attaquons La Gaule"
decalage = 5
messagelower = message.lower()
liste = messagelower.split()
listeletttre = list(map(list, liste))
messagechiffre = ""
alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabetliste = alphabet.split


for x in range(len(listeletttre)):
    for y in range(len(alphabetliste)):
        if x == y:
            [x] = [y + 5]
            messagechiffre += [x]
print(messagechiffre)



