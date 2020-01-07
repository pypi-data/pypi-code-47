'''
Routine to run on local ground station for CASS flights
Saves txt files for aircraft information (header) and each individual flight
Written by: Jessica Blunt
Updated: December 2019
Based on code by Brian Greene, November 2019
Center for Autonomous Sensing and Sampling
University of Oklahoma
'''

import os
import sys
import csv
import datetime as dt
from datetime import datetime
from contextlib import suppress
import numpy as np
import pickle
from utils import UI, ExitException
from admin import Admin

# noinspection SpellCheckingInspection
class Checklist(UI):

    def __init__(self):
        #
        # Load existing data
        #
        self.ndict = pickle.load(open("../user_settings/ndict.pkl", "rb"))
        self.known_locations = \
            pickle.load(open("../user_settings/known_locations.pkl", "rb"))

        #
        # Get needed system info
        #
        self.localNextcloud = True
        self.user = os.path.expanduser("~")
        self.dt_now = datetime.now(tz=dt.timezone(dt.timedelta(hours=0)))
        self.dt_today = datetime(day=self.dt_now.day, month=self.dt_now.month,
                                 year=self.dt_now.year)
        try:
            self.log_dir = os.path.join(self.user, "Nextcloud", "Logs")
            if not os.path.exists(self.log_dir):
                os.mkdir(self.log_dir)
        except FileNotFoundError:
            self.localNextcloud = False
            self.log_dir = os.path.join("..", "Logs")
            if not os.path.exists(self.log_dir):
                os.mkdir(self.log_dir)


        #
        # Directions
        #
        print("Answer all questions without commas. \nTo go back, enter \"!\"\n"
              "To enter admin mode, set the operator's name to \"admin\"\n")


        #
        # Define to-do list to track progress, allow to go back
        #
        self.to_do = ["operator", "platform", "find_header", "location",
                      "flight_pattern", "objective", "legal",
                      "scoop", "weather", "planned_alt", "preflight_checks",
                      "start_info", "end_info", "emergency",
                      "postflight_checks", "comment", "nextcloud"]
        self.step_index = 0
        self.overwrite = False  # if True, user MUST enter answer for ALL
        # steps, even if the answers have previously been entered

        #
        # Hold all info gathered
        #
        self.flight_info = {}
        self.is_first = False

        # start the process...
        while self.step_index < len(self.to_do):
            with suppress(ExitException):
                self.step()

    def step(self):
        self.__getattribute__(self.to_do[self.step_index])()
        self.step_index += 1
        self.overwrite = False

    def get_time(self, date):
        time_str = input(">> ")
        try:
            if (len(time_str) < 4):
                raise ValueError()
            dt = datetime.strptime(f"{date.strftime('%Y%m%d')}_{time_str}",
                                   "%Y%m%d_%H%M")
        except ValueError:
            print("Please enter valid 24-hr time in UTC as HHMM")
            dt = self.get_time(date)
        return dt

    def define_new_loc(self, group):
        """ Allow user to add, remove, and change order of locations

        """
        choice = self.no_commas("Would you like to save this location? [y/n]")
        if choice in "yes" or choice in "YES" or choice in "Yes":
            write_new_loc = True
            if group in self.known_locations.keys():
                region = self.known_locations[group]\
                    [list(self.known_locations[group].keys())[0]]["region"]
                self.flight_info["region"] = region
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
                self.flight_info["region"] = region

            long_name = self.no_commas("What is the full name of your "
                                       "location?")
            self.flight_info["location_name"] = long_name
            location_id = self.no_commas("What 4-5 character ID would you like "
                                         "to assign to " + long_name + "?")
            self.flight_info["location_id"] = location_id

        elif choice in "no" or choice in "NO" or choice in "No":
            self.flight_info["location_id"] = None
            write_new_loc = False

        lat = self.no_commas("What your latitude?")
        self.flight_info["lat"] = lat
        lon = self.no_commas("What is your longitude?")
        self.flight_info["lon"] = lon
        alt = self.no_commas("What is your altitude in meters?")
        self.flight_info["alt"] = alt
        choice = self.no_commas("Is there a Mesonet station nearby? [y/n]")
        if choice in "yesYesYES":
            mesonet_id = self.no_commas("Enter the station's 4-letter "
                                        "identifier.")
            self.flight_info["mesonet_id"] = mesonet_id
        else:
            mesonet_id = None
            self.flight_info["mesonet_id"] = mesonet_id

        if write_new_loc:
            if group not in self.known_locations.keys():
                self.known_locations[group] = {}
            self.known_locations[group][location_id] = \
                {"location_name": long_name, "lat": lat,
                 "lon": lon, "surface_altitude": alt,
                 "region": region, "mesonet_id": mesonet_id}
            pickle.dump(self.known_locations,
                        open("../user_settings/known_locations.pkl", "wb"))

            loc_info = {"location_name": long_name, "lat": lat, "lon": lon,
                        "surface_altitude": alt,
                        "region": region, "mesonet_id": mesonet_id}
        else:
            loc_info = {"lat": lat, "lon": lon, "surface_altitude": alt,
                        "mesonet_id": mesonet_id}

        for key in loc_info.keys():
            self.flight_info[key] = loc_info[key]


    def operator(self):
        if "operator" not in self.flight_info or self.overwrite:
            inp = self.no_commas("Name of person filling out checklist: ")
            if inp in "AdminadminADMIN":
                Admin()
                sys.exit()
            else:
                self.flight_info["operator"] = inp

    def find_header(self):
        # TODO check if overwrite
        self.is_first = self.no_commas("Is this your first flight today? y/n")
        while self.is_first.lower() not in ["y", "n"]:
            self.is_first = self.no_commas("Enter y or n")
        if self.is_first in "y":
            self.is_first = True
            return
        else:
            self.is_first = False
        # find associated header file
        f_read = f"{self.dt_today.strftime('%Y%m%d')}" + \
                 self.flight_info["platform_id"] + "_log_header.csv"
        is_header = self.no_commas("Is this the correct header file? y/n\n"
                                   + f_read)
        while is_header not in ["y", "n"]:
            is_header = input(">> ")
        if is_header == "y":
            f_read_path = os.path.join(self.log_dir, f_read)
        else:
            while True:
                print("Please input the file name to the header file")
                f_in = input(">> ")
                try:
                    f_read_path = os.path.join(self.log_dir, f_in)
                except FileNotFoundError:
                    print("That file could not be found.")
                    continue
                break

        header = np.genfromtxt(f_read_path, dtype=str, delimiter=",",
                               skip_header=1)
        # TODO make header a dictionary accessible elsewhere

    def platform(self):
        """ Prompt user for platform ID
        """
        if "platform_id" not in self.flight_info.keys() or self.overwrite:
            id = self.get_index(list(self.ndict.keys()),
                                message="Enter aircraft N number:")
            if id in "Other":
                self.update_ndict()
                self.platform()
            else:
                self.flight_info["platform_id"] = id

    def location(self):
        """ Ask user for location from list
        """
        loc_keys = list(self.known_locations.keys())

        # Find location group (state or country)
        print("Where are you?")
        group = self.get_index(loc_keys,
                               "What state (US) or country are you in?")

        if group not in self.known_locations.keys():
            self.define_new_loc(group)

        specific_loc_keys = list(self.known_locations[group].keys())
        print("Which location?")
        location_id = self.get_index(specific_loc_keys, free_response=False)
        if location_id in "Other":
            self.define_new_loc(group)
        else:
            loc_info = self.known_locations[group][location_id]
            self.flight_info["location_id"] = location_id
            for key in loc_info.keys():
                self.flight_info[key] = loc_info[key]

    def flight_pattern(self):

        if "flight_pattern" not in self.flight_info.keys() or self.overwrite:
            pattern_list = ["Direct profile", "Helical profile",
                            "Stair step profile",
                            "Hover", "Photogrammetry grid", "Test flight"]
            self.flight_info["flight_pattern"] = \
                self.get_index(pattern_list,
                               message="Enter flight pattern (no commas): ")

    def objective(self):
        if "objective" not in self.flight_info.keys() or self.overwrite:
            print("Chose one or more of the following objectives. If\n"
                  "you chose more than one, separate them with \";\"")
            obj_list = pickle.load(open("../user_settings/objectives.pkl",
                                        "rb"))
            for obj in obj_list:
                print(obj)
            self.flight_info["objective"] = self.no_commas("Objective(s): ")

    def legal(self):
        if "authorization_type" not in self.flight_info.keys() \
                or self.overwrite:
            print("Flight permissions: ")
            per_list = ["COA", "Part 107"]
            per_name = self.get_index(per_list, free_response=False)
            self.flight_info["authorization_type"] = per_name
            if per_name == "COA":
                self.flight_info["pilots_on_site"] = \
                    self.no_commas("List names of all pilots on site separated "
                                   "by \";\"")
            else:
                self.flight_info["pilots_on_site"] = ""
            self.flight_info["PIC"] = self.no_commas("Pilot in Command: ")

    def scoop(self):
        if "scoop" not in self.flight_info.keys() or self.overwrite:
            if self.ndict[self.flight_info["platform_id"]]:
                print("Scoop ID:")
                self.flight_info["scoop_id"] = \
                    self.get_index(["A", "B", "C", "D"],
                                   message="Enter scoop number: ")
            else:
                self.flight_info["scoop_id"] = ""

    def weather(self):
        if "cloud" not in self.flight_info.keys() or self.overwrite:
            print("Cloud cover: ")
            sky_list = ["0%", "1-25%", "26-50%", "51-75%", "76-100%"]
            cloud = self.get_index(sky_list, free_response=False)
            if "76-100%" in cloud:  # swapped order - 0% is in 10 0%
                r = self.no_commas("Is it precipitating? If yes be sure to "
                                   "denote type in remarks. y/n")
                while r not in ["y", "n"]:
                    r = input(">> ")
                if r == "y":
                    rain = "yes"
                else:
                    rain = "no"
            else:
                rain = "no"
            self.flight_info["cloud"] = cloud
            self.flight_info["rain"] = rain

        if self.flight_info["mesonet_id"] == "":  # this is in locations
            self.flight_info["wind_from_direction"] = \
                self.no_commas("What direction (in degrees) is the "
                               "wind coming from?")
            self.flight_info["wind_speed"] = \
                self.no_commas("What is the ambient wind speed (in m/s)?")
            self.flight_info["wind_speed_gust"] = \
                self.no_commas("About how fast is the wind gusting to? "
                               "(in m/s)")
        else:
            self.flight_info["wind_from_direction"] = ""
            self.flight_info["wind_speed"] = ""
            self.flight_info["wind_speed_gust"] = ""

    def planned_alt(self):
        if "max_planned_alt" not in self.flight_info or self.overwrite:
            self.flight_info["max_planned_alt"] = self.no_commas("Planned "
                                                                 "maximum "
                                                                 "altitude: ")

    def preflight_checks(self):
        checklist = [
            "Check for visual obstacles and potential source of "
            "interference (antennas, \n"
                "electrical lines, metal structures) ",
            "Clear and agree on a takeoff and landing zone ",
            "Check current wind speed and humidity at the location, decide "
            "if it's \n"
                "appropriate for safe flight ",
            "Perform visual inspection of the vehicle - props not damaged, "
            "props tight, \n"
                "center of gravity, orientation and connection of RH, GPS, "
            "data transfer \n"
                "antennas, mechanical check ",
            "Check Mission planner laptop battery charge ",
            "Confirm mission planner running ",
            "Connect ground station RF to laptop ",
            "Turn on controller and check voltage ",
            "Plug in the UAV's battery and let it boot up stationary for 20 "
            "seconds ",
            "Connect telemetry (baud 57600, select serial link, confirm "
            "heartbeat) ",
            "Confirm no error messages with mission planner ",
            "Confirm GPS fix type (outdoors must get 3D fix) ",
            "Check data logging ",
            "Place vehicle at launch point",
            "Check flight mode on controller",
            "Confirm data logging software running",
            "Check sensors are in correct range",
            "Review flight plan - verbal and on mission planner",
            "Test audio communications among participants",
            "Check if all participants ready for flight",
            "Press the safety button on the vehicle until solid red - now "
            "live and armed",
            "Check the LED for status of the vehicle. Should see a blinking "
            "green light indicating GPS lock",
            "Arm motors and call clear prop"
        ]
        for i in range(len(checklist)):
            print("\n")
            input(f">>{checklist[i]}")

        print("Finished with pre-takeoff checklist.")

    def start_info(self):
        # TODO clean known_locations, ndict
        # launch time, battery num, voltage
        if "launch_time" not in self.flight_info.keys() or self.overwrite:

            self.flight_info["battery_id"] = \
                self.no_commas("Battery number (enter unknown if unknown)")
            self.flight_info["battery_voltage_initial"] = self.no_commas(
                "Battery voltage: Enter only the battery voltage in volts "
                "without units.")
            print("Enter takeoff time as 24-hr UTC HHMM")
            self.flight_info["launch_time_utc"] = self.get_time(self.dt_today)

    def end_info(self):
        if "max_achieved_alt" not in self.flight_info.keys() or self.overwrite:
            self.flight_info["battery_voltage_final"] = self.no_commas(
                "Battery voltage: Enter only the battery voltage in "
                "volts without units.")
            print("Enter landing time as 24-hr UTC HHMM.")
            self.flight_info["land_time_utc"] = self.get_time(self.dt_today)
            self.flight_info["max_achieved_alt"] = \
                self.no_commas("Enter maximum altitude achieved in meters.")

    def emergency(self):
        if "emergency_landing" not in self.flight_info.keys() or self.overwrite:
            emergency = \
                self.no_commas("---Emergency landing required? y/n---\n"
                               "This includes landing for airspace incursion "
                               "purposes,\n"
                               "critical battery RTL, or loss of control of "
                               "aircraft. If yes,\n"
                               "please fill out proper documentation in the "
                               "CASS Google Drive folder.\n"
                               "Also be sure to denote in remarks.")
            while emergency not in ["y", "n"]:
                emergency = input(">> ")

            if emergency == "y":
                print("---EMERGENCY CAUSED BY VISUAL AND FLIGHT CONDITION---")
                print("If Flight conditions turned unsafe (wind excess, sudden "
                      "fog or rain, lost sight or communication)")
                print("or Mission planner shows out of range parameters, "
                      "perform the following:")
                print("-Trigger RTL mode")
                print("-Confirm safe landing and shut off")
                print("")
                print("---EMERGENCY CAUSED BY GPS ERRORS---")
                print("If Mission planners shows GPS errors, DO NOT TRIGGER "
                      "RTL. Perform the following:")
                print("-Change to stabilize mode")
                print("-Return to base by pilot's flight skills")
                print("-Confirm safe landing and shut off")
                print("")
                error_str = self.no_commas("Take note of error messages in "
                                           "mission planner and what triggered "
                                           "emergency:")
                print("Continuing with post-flight checklist.")
            else:
                error_str = ""

            self.flight_info["emergency_landing"] = emergency
            self.flight_info["emergency_remarks"] = error_str

    def postflight_checks(self):
        checklist = ["Notify observers and participants that mission complete",
                     "Disarm vehicle",
                     "Perform PPK (if applicable)",
                     "Disconnect battery",
                     "Inspect vehicle"]
        for i in range(len(checklist)):
            print("\n")
            input(f">>{checklist[i]}")

        print("Finished with post_landing checklist.")

    def comment(self):
        if "private_remarks" not in self.flight_info.keys() or self.overwrite:
            self.flight_info["private_remarks"] = \
                self.no_commas("Additional remarks or "
                               "comments (for CASS only):")
            self.flight_info["remarks"] = \
                self.no_commas("Additional remarks or comments:")

    def nextcloud(self):

        self.flight_info["launch_time_utc"] = \
            self.flight_info['launch_time_utc'].strftime('%Y%m%d_%H%M')
        self.flight_info["land_time_utc"] = \
            self.flight_info['land_time_utc'].strftime('%Y%m%d_%H%M')
        self.flight_info["timestamp"] = self.dt_now.strftime("%Y%m%d_%H%M%S")

        #
        # Header
        #
        if self.is_first:
            f_header = f"{self.flight_info['timestamp']}" + \
                       self.flight_info["platform_id"] + "_log_header.csv"
            f_header_path = os.path.join(self.log_dir, f_header)
            headers = ("timestamp", "operator", "location_id", "location_name",
                         "surface_altitude", "mesonet_id", "region",
                         "pilots_on_site", "objective", "authorization_type",
                         "platform_id", "scoop_id")
            fw = open(f_header_path, "w")
            writer = csv.writer(fw, delimiter=",")
            writer.writerow(headers)
            data = []
            for i in range(len(headers)):
                data.append(self.flight_info[headers[i]])
            writer.writerow(data)
            fw.close()

        #
        # Flight
        #

        f_flight = f"{self.flight_info['launch_time_utc']}" + \
                   self.flight_info["platform_id"] + "_flight_log.csv"
        f_flight_path = os.path.join(self.log_dir, f_flight)

        headers = ("timestamp", "operator", "PIC", "battery_id", "cloud",
                   "rain", "battery_voltage_initial", "max_planned_alt",
                   "launch_time_utc", "max_achieved_alt", "land_time_utc",
                   "battery_voltage_final", "emergency_landing",
                   "emergency_remarks", "private_remarks", "remarks")

        data = []
        for i in range(len(headers)):
            data.append(self.flight_info[headers[i]])
        fw = open(f_flight_path, "w")
        writer = csv.writer(fw, delimiter=",")
        writer.writerow(headers)
        writer.writerow(data)

        fw.close()

        if not self.localNextcloud:
            is_done = input("Is this your last flight?\n>>")
            if is_done.capitalize() in "YES":
                print("Copy this link into your browser and upload the "
                      "contents of " +
                      os.path.join(os.path.abspath(".."), "Logs")
                      + ":\n https://10.197.13.220/s/qXjandWWu26v4hO")

Checklist()
