chaine = "jadore la viande"
chaine2 = "lol"
result = (chaine.find("e"))
result2 = (chaine2.find("e"))
if result > 0:
    print("il y a un e dans la chaine de caractères")
else:
    print("il ny a pas de dans la chaine de caractères")

if result2 > 0:
    print("il y a un e dans la chaine de caractères")
else:
    print("il ny a pas de e dans la chaine de caractères")

# ce qui est écrit après sont des tests pour essayer de ne pas coder en dur

testinput = input("tapez votre chaine de caractères :")

if "e" in testinput:
    print("il y a un e")
else:
    print("il n'y a pas de e")