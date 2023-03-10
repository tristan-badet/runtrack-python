alphabet = "abcdefghijklmnopqrstuvwxyz" * 10
etages = 10
lettre = 1
value = 0


for x in range(1, etages+1):
    for n in range(1, x+1):
        print(alphabet[value], end ="")
        value += 1
    print()




