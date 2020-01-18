class SimpleTextInteraction:
    def __init__(self):
        pass

    ## Text menu in Python
    def get_selection(self, options: list, title = 'Please select', default = 1):  ## Your menu design here

        padding = 20
        while True:  ## While loop which will keep going until loop = False
            print(padding * "-", title, padding * "-")
            for i in range(len(options)):
                print("{}. {}".format(i + 1, options[i]))
            print('0. Exit')
            print((padding*2 + 2 + len(title)) * "-")
            choice = input("Enter your choice [0-{}]: ".format(len(options)))
            try:
                if choice == '':
                    return default
                elif int(choice) <= len(options):
                    return int(choice)
                else:
                    pass
            except:
                pass
            print("Wrong input. please try again...")

    def get_numeric(self, text, low=None, high=None):
        while True:
            try:
                val = input(text)
                val = int(val)
                if low is not None and val<low:
                    print('{} is smaller than {}, please enter again'.format(val,low))
                    continue
                if high is not None and val > high:
                    print('{} is bigger than {}, please enter again'.format(val, high))
                    continue
                return val
            except:
                print('"{}" is not numeric, please try again'.format(val))

if __name__ == '__main__':
    menu = SimpleTextInteraction()
    selection=1
    while selection != 0:
        selection = menu.get_selection(['Option 1', 'Option 2', 'Option 3'], default=2)
        print ('Selected:', selection)
        menu.get_numeric('Please enter a number between 3 and 8: ', 3, 8)

