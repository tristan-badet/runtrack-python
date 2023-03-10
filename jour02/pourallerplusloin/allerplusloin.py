def postriangle(a,b,c):
    if a == b == c:
        print("ce triangle est équilatéral")
    elif (a*a) + (b*b) == (c*c) and a != b:
        print("le triangle est rectangle en C")
    elif a == b or a == c or c == b and (a*a) + (b*b) != (c*c):
        print("ce triangle est isocèle")
    else:
        print("ce triangle est quelconque")


        # correction, triangle rectangle on aurait du faire pour tous les angles avec or 
        # or a*a = (b*b) + (c*c) par exemple ça aurait couvert les différents angles du triangle 