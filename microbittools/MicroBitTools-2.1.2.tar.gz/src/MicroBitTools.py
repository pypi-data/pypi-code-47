import os
import shutil
import uflash
import requests
import serial
import microfs
import time
import json

readymicrobithexurl = "https://www.dropbox.com/s/ksk3p5cnr5znky6/SerialSystem.hex?dl=1"


class InternalTools:
    def yntoboolean(data="no"):
        data = data.lower()
        if data == "y":
            return True
        elif data == "n":
            return False
        else:
            return "ERROR: \nInput was not either y or n"
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'


def flash(pythonfile):
    drive = uflash.find_microbit()
    tryn = 0
    while drive == "":
        if tryn == 1:
            print("Please plug in a microbit")
        tryn = tryn + 1
        input()
        drive = uflash.find_microbit()
    pyfilenoext = pythonfile[:-3]
    os.system("cd " + os.getcwd())
    os.system('py2hex "' + pythonfile + '"')
    print("Moving to microbit.")
    shutil.move(pyfilenoext + ".hex", drive)
    print("Done!")


def flashF(folder):
    print("MicroBit is at: " + microfs.find_microbit()[0] + "\nMicroBit directory is at: " + uflash.find_microbit())
    try:
        mfiles = microfs.ls()
    except OSError as e:
        print(str(
            e) + "\nMicrobit is probably calibrating, calibrate and then try again\nIf it still does not work try to "
                 "replug your microbit or close other programs that is accessing your microbit")
        return "Could not write"
    print("Removing old stuff: " + str(mfiles))
    for file in mfiles:
        microfs.rm(file)

    files = os.listdir(folder)
    print("Flashing new stuff: " + str(files))
    for file in files:
        microfs.put(folder + "\\" + file)

    print("Flashed new stuff: " + str(microfs.ls()) + "\n")

    time.sleep(0.1)
    print("Done!" + "\n" +
          "Don't forget to name your main file \"main.py\"" + "\n" + InternalTools.bcolors.BOLD +
          "Reset your MicroBit to apply changes!"
          )
    # except OSError as e:
    #     exit(str(e) + "\n\nReplug microbit")
    # except TypeError as e:
    #     exit(str(e) + "\n\nReplug microbit")
    # SerialSystem.ser.open()


def export(arg1):
    flash(arg1)


class SerialSystem:
    ser = microfs.get_serial()
    ser.baudrate = 115200
    ser.close()

    microbitpath = uflash.find_microbit()
    before = {'Buttons': {'A': False, 'B': False}, 'Temp': 20, 'CompassHeading': 369,
                      'Accelerometer': {'Y': 0, 'X': 0, 'Z': 0}, 'Brightness': 0}

    def close(self):
        self.ser.close()

    def open(self):
        try:
            self.ser.open()
        except serial.serialutil.SerialException as e:
            print(str(e))

    # FIXA
    def readyMicroBit(self, printb=False):
        # shutil.copyfile(os.getcwd() + "\\src\\" + "microbitserialsystem.hex", self.microbitpath+"SerialSystem.hex")
        # shutil.copy
        if printb:
            print("Downloading HEX")
        url = readymicrobithexurl
        r = requests.get(url)
        if printb:
            print("Downloaded HEX")
            print("Fixing HEX")
        content = ""
        # contentb = r.content
        # contentb = str(contentb)
        # contentb = contentb[:-1]
        # contentb = contentb[2:]
        # contentsplit = contentb.split("\\n")
        # for i in contentsplit:
        #     content = content + i + "\n"
        content = r.content.decode("UTF-8")
        if printb:
            print("Fixed HEX\n" + content)
            print("Moving HEX to microbit")

        try:
            file = open("SerialSystem.hex", "w")

            file.write(content)

            file.close()

            shutil.move("SerialSystem.hex", uflash.find_microbit() + "SerialSystem.hex")
        except shutil.Error as e:
            print(e)
            print("SerialSystem hex already installed")
            os.remove(os.getcwd() + "\\SerialSystem.hex")
        if printb:
            print("Moved HEX to microbit")

    def display(self, screen=[
        [5, 6, 7, 6, 5],
        [6, 7, 8, 7, 6],
        [7, 8, 9, 8, 7],
        [6, 7, 8, 7, 6],
        [5, 6, 7, 6, 5]
    ]):
        fixedscreen = [0,0,0,0,0]
        yn = 0
        for y in screen:
            tempstring = ""
            xn = 0
            for x in y:
                tempstring = tempstring + str(screen[yn][xn])
                xn = xn + 1
            if y != 4:
                tempstring = tempstring + ":"
            fixedscreen[yn] = tempstring
            yn = yn + 1


        try:
            self.ser.open()
        except serial.serialutil.SerialException as e:
            pass # print(str(e))
        self.ser.write(bytes("?" + str(fixedscreen).replace(" ",""), 'utf-8'))



    def readRaw(self):
        try:
            self.ser.open()
        except serial.serialutil.SerialException as e:
            pass # print(str(e))
        data_raw = self.ser.readline()
        result = ""
        try:
            if data_raw != b'':
                result = data_raw.decode("utf-8")
        except UnicodeEncodeError as e:
            print("Skipping because of error: " + str(e))
        return result

    def read(self):
        try:
            self.ser.open()
        except serial.serialutil.SerialException as e:
            pass # print(str(e))
        try:
            mbd = self.ser.readline().decode("UTF-8")
            mbd = mbd.replace("'", '"')
        except serial.serialutil.SerialException:
            return {"Error": "Can not find MicroBit"}
        except UnicodeDecodeError as e:
            mbd = ""
            time.sleep(0.5)
            print(e)
        except IndexError:
            return {"Error": "Unknown error"}
        if mbd.startswith("?"):
            mbds = mbd.split("?")
            try:
                result = json.loads(mbds[1])
                if result["Buttons"]["A"] == "true":
                    result["Buttons"]["A"] = True
                elif result["Buttons"]["A"] == "false":
                    result["Buttons"]["A"] = False

                if result["Buttons"]["B"] == "true":
                    result["Buttons"]["B"] = True
                elif result["Buttons"]["B"] == "false":
                    result["Buttons"]["B"] = False
            except json.decoder.JSONDecodeError as e:
                print(mbds[1])
                print(e)
                result = {"Error": "Cant convert Json (MicroBit probably is using wrong firmware)"}
        else:
            result = self.before

        self.before = result
        return result


def test():
    print("SUCCESS")
