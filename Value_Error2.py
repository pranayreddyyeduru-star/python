try:
    num=int(input("Give me a number: "))
    print("The number entered is:", num)
except ValueError as ex:
    print("Exception: ", ex)