keepgoing = True
while keepgoing == True:

    # show a menu
    print("1: C to F")
    print("2: F to C")
    print("Anything else - exit")

    choice = int(input("What way to convert?"))

    # ask for user input
    if choice == 1 or choice == 2:
        n = int(input("Enter a value to convert: "))

    # convert the value
    if choice == 1:
        res = (n * 9/5) + 32
        # show the converted value
        print(f"The converted value is {res}")
    elif choice == 2:
        res = (n-32) * (5/9)
        # show the converted value
        print(f"The converted value is {res}")
    else:
        keepgoing == False

# CHALLENGE look at brief and make better