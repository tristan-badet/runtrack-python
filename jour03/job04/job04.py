for x in range(101):
    if x% 5 == 0 and x% 3 == 0 and x != 0:
        print("FizzBuzz")
    elif x% 5 == 0 and x != 0:
        print("Buzz")
    elif x% 3 == 0 and x != 0:
        print("Fizz")
    else:
        print(x)
       
