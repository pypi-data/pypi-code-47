import time


def chemex_brew(grams, brew_int):
    print("Make sure your water is heated up and your Chemex is ready to go.")
    time.sleep(2)
    while True:
        value = input("Ready to start pouring? \n(y or n)\n> ")
        if str.lower(value) == "y":
            break
        else:
            print("Well just press 'y' when you are...")
            time.sleep(3)
    for x in range(5, -1, -1):
        print("*" * x)
        time.sleep(0.2)
    print("Here we go!")
    time.sleep(1)

    print(f"Pour to {grams * 3.0} grams and then wait...")
    time.sleep(brew_int)
    print(f"Now pour to {grams * 6.8} grams and then wait...")
    time.sleep(brew_int)
    print(f"Now pour to {grams * 9.6} grams and then wait...")
    time.sleep(brew_int)
    print(f"Now pour to {grams * 12.8} grams and then wait...")
    time.sleep(brew_int)
    print(f"Now pour to {grams * 16.0} grams and then wait...")
    time.sleep(10)
    print(
        "You're done! \nEnjoy!"
    )
