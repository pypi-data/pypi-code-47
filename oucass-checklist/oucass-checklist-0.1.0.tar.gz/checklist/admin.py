from utils import UI, ExitException
from contextlib import suppress
import pickle


class Admin(UI):
    def __init__(self):
        self.step_index = 0
        self.to_do = ['choose_list']
        print("Welcome to the Admin menu! To return to the flight checklist, \n"
              "restart the program. If you make a mistake, just enter \"!\" \n"
              "to go back a step.")
        while self.step_index < len(self.to_do):
            with suppress(ExitException):
                self.step()

    def step(self):
        self.__getattribute__(self.to_do[self.step_index])()
        self.step_index += 1

    def choose_list(self):
        options = {'Platforms (i.e. N###UA_Colloqiual_Name)': "platforms",
                   'General Locations (i.e. Colorado)': "groups",
                   'Specific Locations (i.e. ABC City Park)': "locations",
                   'Objectives (i.e. Photogrametry)': "objectives"}
        message = "What would you like to edit?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def platforms(self):
        options = {'Add': "platforms_add",
                   'Remove': "platforms_remove",
                   'Reorder': "platforms_reorder"}
        message = "What would you like to do?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def platforms_add(self):
        old_dict = pickle.load(open("ndict.pkl", "rb"))
        print(list(old_dict.keys()))
        add = self.no_commas("Is your platform in this list? (y/n)")
        while add.lower() not in ["y", "n"]:
            add = self.no_commas("Enter y or n")
        if add in "Yesyes":
            self.back()

        name = self.no_commas("Enter the name of your platform in the format "
                              "N###UA_Colloqiual_Name")
        scoop = self.no_commas("Does this platform have an interchangeable "
                               "scoop?")
        while scoop.lower() not in ["y", "n"]:
            scoop = self.no_commas("Enter y or n")

        if scoop in "Yesyes":
            scoop = True
        else:
            scoop = False

        old_dict[name] = scoop
        pickle.dump(old_dict, open("ndict.pkl", "wb"))
        print("Platform " + name + " has been added.")
        self.back()

    def platforms_remove(self):
        old_dict = pickle.load(open("ndict.pkl", "rb"))
        to_remove = self.get_index(list(old_dict.keys()),
                                   message="Which platform would you like to "
                                           "remove?", free_response=False)
        old_dict.pop(to_remove)
        pickle.dump(old_dict, open("ndict.pkl", "wb"))
        print("Platform " + to_remove + " has been removed.")
        self.back()

    def platforms_reorder(self):
        old_dict = pickle.load(open("ndict.pkl", "rb"))
        keys = list(old_dict.keys())
        print("Here is the current order of the platforms: ")
        for i in range(len(keys)):
            print(str(i+1), keys[i])
        print("\nEnter the numbers shown on the left one at a time, starting "
              "with the platform you want listed first and ending with the "
              "one you want listed last.")
        new_dict = {}
        while len(old_dict.keys()) > 0:
            print("\tRemaining: " + str(list(old_dict.keys())))
            next_elem = self.no_commas("")
            while not next_elem.isnumeric():
                next_elem = self.no_commas("Enter an integer.")
            next_elem = int(next_elem)

            new_dict[keys[next_elem-1]] = old_dict.pop(keys[next_elem-1])

        pickle.dump(new_dict, open('ndict.pkl', 'wb'))
        self.back()

    def groups(self):
        options = {'Remove': "groups_remove",
                   'Reorder': "groups_reorder"}
        message = "What would you like to do?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def groups_remove(self):
        old_dict = pickle.load(open("known_locations.pkl", "rb"))
        message = "Which set of locations would you like to remove?\n" \
                  "WARNING: ALL DATA STORED WITHIN THIS AREA WILL BE " \
                  "PERMANENTLY DELETED!"
        option = self.get_index(list(old_dict.keys()), message=message,
                                free_response=False)
        old_dict.pop(option)
        pickle.dump(old_dict, open("known_locations.pkl", "wb"))
        print("All locations in " + option + " have been deleted.")
        self.back()

    def groups_reorder(self):
        old_dict = pickle.load(open("known_locations.pkl", "rb"))
        keys = list(old_dict.keys())
        print("Here is the current order of the location groups: ")
        for i in range(len(keys)):
            print(str(i + 1), keys[i])
        print("\nEnter the numbers shown on the left one at a time, starting "
              "with the group you want listed first and ending with the "
              "one you want listed last.")
        new_dict = {}
        while len(old_dict.keys()) > 0:
            print("\tRemaining: " + str(list(old_dict.keys())))
            next_elem = self.no_commas("")
            while not next_elem.isnumeric():
                next_elem = self.no_commas("Enter an integer.")
            next_elem = int(next_elem)

            new_dict[keys[next_elem - 1]] = old_dict.pop(keys[next_elem - 1])

        pickle.dump(new_dict, open('known_locations.pkl', 'wb'))
        self.back()

    def locations(self):
        options = {'Add': "locations_add",
                   'Remove': "locations_remove",
                   'Reorder': "locations_reorder"}
        message = "What would you like to do?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def locations_add(self):
        old_dict = pickle.load(open("known_locations.pkl", "rb"))
        group = self.get_index(list(old_dict.keys()), message="What country or"
                                                              " US state are "
                                                              "you in?")
        if group in old_dict.keys():
            region = old_dict[group] \
                [list(old_dict[group].keys())[0]]["region"]
        else:
            choice = self.no_commas("Are you in North America? [y/n]")
            if choice in "yesYESYes":
                region = "north_america"
            else:
                region = self.no_commas("What region from this list are you"
                                        " in?\n"
                                        "http://cfconventions.org/"
                                        "Data/standardized-region-list/"
                                        "standardized-region-list.html")

        long_name = self.no_commas("What is the full name of your location?")
        location_id = self.no_commas("What 4-5 character ID would you like "
                                     "to assign to " + long_name + "?")

        lat = self.no_commas("What your latitude?")
        lon = self.no_commas("What is your longitude?")
        alt = self.no_commas("What is your altitude in meters?")
        choice = self.no_commas("Is there a Mesonet station nearby? [y/n]")
        if choice in "yesYesYES":
            mesonet_id = self.no_commas("Enter the station's 4-letter "
                                        "identifier.")
        else:
            mesonet_id = None

        if group not in old_dict.keys():
            old_dict[group] = {}

        old_dict[group][location_id] = \
            {"location_name": long_name, "lat": lat,
             "lon": lon, "surface_altitude": alt,
             "region": region, "mesonet_id": mesonet_id}

        pickle.dump(old_dict, open("known_locations.pkl", "wb"))
        print(long_name + " has been added to the list of known locations.")
        self.back()

    def locations_remove(self):
        old_dict = pickle.load(open("known_locations.pkl", "rb"))
        group = self.get_index(list(old_dict.keys()),
                               message="Where is the location you want to "
                                       "delete?", free_response=False)
        loc = self.get_index(list(old_dict[group].keys()),
                             message="Which location would you like to delete?",
                             free_response=False)
        old_dict[group].pop(loc)
        if len(old_dict[group].keys()) < 1:
            del_group = self.no_commas("There are now no saved locations "
                                       "within " + group + ". Would you like "
                                                           "to delete " + group
                                       + "? [y/n]")
            while del_group.lower() not in ["y", "n"]:
                del_group = self.no_commas("Enter y or n")
            if del_group in "Yesyes":
                old_dict.pop(group)

        pickle.dump(old_dict, open("known_locations.pkl", "wb"))
        print(loc + " has been removed from the list of saved locations.")
        self.back()

    def locations_reorder(self):
        old_dict = pickle.load(open("known_locations.pkl", "rb"))
        keys = list(old_dict.keys())
        group = self.get_index(keys, message="Which set of locations would you "
                                             "like to reorder?",
                               free_response=False)
        keys = list(old_dict[group].keys())
        print("Here is the current order of the locations in " + group + ": ")
        for i in range(len(keys)):
            print(str(i + 1), keys[i])
        print("\nEnter the numbers shown on the left one at a time, starting "
              "with the location you want listed first and ending with the "
              "one you want listed last.")
        new_sub_dict = {}
        while len(old_dict[group].keys()) > 0:
            print("\tRemaining: " + str(list(old_dict[group].keys())))
            next_elem = self.no_commas("")
            while not next_elem.isnumeric():
                next_elem = self.no_commas("Enter an integer.")
            next_elem = int(next_elem)

            new_sub_dict[keys[next_elem - 1]] = old_dict[group].pop(keys[next_elem - 1])

        old_dict[group] = new_sub_dict
        pickle.dump(old_dict, open('known_locations.pkl', 'wb'))
        self.back()

    def objectives(self):
        options = {'Add': "objectives_add",
                   'Remove': "objectives_remove",
                   'Reorder': "objectives_reorder"}
        message = "What would you like to do?"
        option = self.get_index(list(options.keys()), message=message,
                                free_response=False)
        self.to_do.append(options[option])

    def objectives_add(self):
        objectives = pickle.load(open("objectives.pkl", "rb"))
        print(objectives)
        add = self.no_commas("Is your objective in this list? (y/n)")
        while add.lower() not in ["y", "n"]:
            add = self.no_commas("Enter y or n")

        if add in "Yesyes":
            self.back()

        new_objective = self.no_commas("What is the name of the objective you'd"
                                       " like to add?")
        objectives.append(new_objective)
        pickle.dump(objectives, open("objectives.pkl", "wb"))
        print(new_objective + " has been added to the saved objectives.")
        self.back()

    def objectives_remove(self):
        objectives = pickle.load(open("objectives.pkl", "rb"))
        to_remove = self.get_index(objectives, free_response=False,
                                   message="Which item would you like to "
                                           "remove?")
        objectives.remove(to_remove)
        pickle.dump(objectives, open("objectives.pkl", "wb"))
        print(to_remove + " has been removed from the list of objectives.")
        self.back()

    def objectives_reorder(self):
        objectives = pickle.load(open("objectives.pkl", "rb"))
        print("Here is the current order of the objectives: ")
        for i in range(len(objectives)):
            print(str(i + 1), objectives[i])
        print("\nEnter the numbers shown on the left one at a time, starting "
              "with the objective you want listed first and ending with the "
              "one you want listed last.")
        new_order = []
        remaining = objectives.copy()
        while len(objectives) - len(new_order) > 0:
            print("\tRemaining: " + str(remaining))
            next_elem = self.no_commas("")
            while not next_elem.isnumeric():
                next_elem = self.no_commas("Enter an integer.")
            next_elem = int(next_elem)

            new_order.append(objectives[next_elem - 1])
            remaining.remove(objectives[next_elem - 1])

        pickle.dump(new_order, open('objectives.pkl', 'wb'))
        self.back()

    # TODO How to update installed version without messing up the pkl files?
