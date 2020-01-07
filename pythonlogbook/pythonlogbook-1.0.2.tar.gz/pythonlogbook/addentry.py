# import the os module
import os #makes directory modification work
from datetime import datetime #gets date and time

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

#beginningPath = r"/" #os.getcwd()
originalPath = r"/home/luke/Documents"
os.chdir(originalPath) #maybe allow for the user to choose save destination in the future
path = os.getcwd()
print ("The location of your logbook willl be %s" % path)

def createDirectory(lastDirectory, newDirectoryTitle):
    newDirectory = lastDirectory + "/" + newDirectoryTitle
    if not os.path.exists(newDirectory):
        os.mkdir(newDirectory)
        print(newDirectoryTitle + " folder created")
    else:
        print(newDirectoryTitle + " path exists")

    return newDirectory

#creates all directorys by calling a function, returning the path it created and then calling another function with that functions return as parameter
logPath = createDirectory(originalPath, "logbook")
yearPath = createDirectory(logPath, now.strftime("%Y"))
monthPath = createDirectory(yearPath, now.strftime("%m"))
datePath = createDirectory(monthPath, now.strftime("%d"))

#Makes text file
#determines what to call the text file depending on the date and how many files have been created on that date
datePartOfLogname = now.strftime("%m-%d-%Y")
timePartOfLogname = now.strftime("%H:%M:%S")
logname = datePartOfLogname + "_" + timePartOfLogname
finalLogPath = datePath + "/" + logname

finalLogPath = datePath + "/" + logname
f = open(finalLogPath,"w+")

#writes date and time as first line of txt file
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
f.write(dt_string)
print("File name is " + logname)
#webbrowser.open(finalLogPath) #opens txt file in text editor

text = input("Entry here: ")
f.write("\n" + text)
print("File saved as " + logname)
