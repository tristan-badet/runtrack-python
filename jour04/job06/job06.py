liste = ["brimstone", "thackeray", "brisk", "caithe"]
a = liste.index("brimstone")
b = liste.index("caithe")

liste[a], liste[b] = liste[b], liste [a]

print(liste)
