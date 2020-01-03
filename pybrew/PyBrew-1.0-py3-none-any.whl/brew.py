from pybrew.timers import chemex_brew
import time


class Brew():
    def __init__(self, brew_type, grams):
        self.grams = grams
        self.type = brew_type

    def __str__(self):
        return str.title(self.type) + ' at ' + str(self.grams) + ' grams.'

    def start(self):
        if str.lower(self.type) == "chemex":
            chemex_brew(self.grams, chemex_brew_int)


app_condition = True
chemex_brew_int = 45
usr_brew_type = ""
usr_grams = 0
start_input = "n"

while app_condition:
    print("Hello,")
    while str.lower(start_input) != "y":
        usr_brew_type = input(
            "\nHow would you like to make your coffee? \n(Chemex or Keurig?) \n> "
        )
        while str.lower(usr_brew_type) == "keurig":
            print("Your coffee sucks.")
            usr_brew_type = input(
                "How would you ACTUALLY like to make your coffee? \n(Chemex?) \n> "
            )
        while str.lower(usr_brew_type) != "chemex":
            print("You can't make coffee like THAT!")
            usr_brew_type = input(
                "How would you ACTUALLY like to make your coffee? \n(Chemex) \n> "
            )
        while True:
            usr_grams = int(input(
                "How many grams of coffee would you like to use? \n> "))
            try:
                value = int(usr_grams)
                if value > 0:
                    break
                else:
                    print("You have to have coffee beans to brew coffee...")
            except ValueError:
                print("Please enter a number...")
        start_input = input("Ready to start? \n(y or n)> ")

    brew = Brew(usr_brew_type, usr_grams)
    brew.start()
    time.sleep(2)
    end_input = input(
        "Would you like to brew some more coffee? \n(y or n)\n> ")
    if str.lower(end_input) == "y":
        start_input = "n"
        app_condition = True
    else:
        app_condition = False
        print("Good Bye!")
