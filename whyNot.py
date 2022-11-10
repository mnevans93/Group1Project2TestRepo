for fizzbuzz in range(101):
    if fizzbuzz % 15 == 0:
        print("fizzbuzz")
    elif fizzbuzz % 3 == 0:
        print("fizz")
    elif fizzbuzz % 5 == 0:
        print("buzz")
    print(fizzbuzz)