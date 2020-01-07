class ExitException(BaseException):
    def __init__(self):
        return


class UI:

    def __init__(self):
        self.step_index = 0
        self.overwrite = False

    def back(self):
        if self.step_index > 0:
            self.step_index -= 1
            self.overwrite = True
            self.to_do.pop(-1)
            raise ExitException

    def get_index(self, list, message=None, free_response=True):
        """ Recursively call until valid index chosen from specified array
        """
        if message is not None:
            print('\n' + message)

        for i in range(len(list)):
            print("\t" + str(i+1) + " - " + str(list[i]))
        if free_response:
            print("\t" + str(len(list)+1) + " - Other")
        i_str = input(">> ")
        if i_str in [str(i) for i in range(1, len(list) + 1, 1)]:
            to_return = list[int(i_str) - 1]
        elif i_str == str(len(list) + 1):
            if free_response:
                to_return = self.no_commas(message)
            else:
                to_return = "Other"
        elif "!" in i_str:
            self.back()
            raise ExitException
        else:
            print("Please enter valid option")
            to_return = self.get_index(list, message, free_response)
        return to_return


    def no_commas(self, message):
        """ Ensure no commas input
        """
        print(message)
        x = input(">> ")
        while "," in x:
            print("Please enter valid name with no commas")
            x = self.no_commas(message)
        if "!" in x:
            self.back()
            raise ExitException()
        if "remarks" not in message and "Remarks" not in message:
            while x in "":
                print("This field is non-optional")
                x = self.no_commas(message)
        return x
