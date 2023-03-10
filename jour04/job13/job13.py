L = [10,20,30,20,10,50,60,40,80,50,40]
L2 = [ ]

for x in L:
    if x not in L2:
        L2 += [x]
L = L2
print(L)




