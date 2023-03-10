def suite():
    for x in range(2, 1000):
        for n in range(2, x):
            if x % n == 0:
              break
        else:
            print(x)

suite()