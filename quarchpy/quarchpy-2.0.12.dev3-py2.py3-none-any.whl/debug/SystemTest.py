from quarchpy import *
from quarchpy.device import *
import pkg_resources
from pkg_resources import parse_version, get_distribution
import os
import platform
import time
import sys
import subprocess

def main ():
    print("")

    print("OS Name : " + os.name)
    print("Platform System : " + platform.system())
    print("Platfrom : " + platform.platform())
    if "nt" in os.name: print ("Platform Architecture : " + platform.architecture()[0])
    print("Platform Release :  " + platform.release())

    try:
        print("Quarchpy Version : " + pkg_resources.get_distribution("quarchpy").version)
    except:
        print("Unable to detect Quarchpy version")

    try:
        print("Python Version : " + sys.version)
    except:
        print("Unable to detect Python version")

    try:
        print("QIS version number: " + get_QIS_version())
    except:
        print("Unable to detect QIS version")

	#TODO print java version and jfx, should work for open java and openJFX
    try:
        javaVersion = bytes(subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)).decode()
        print("Java Version:"+ str(javaVersion))
    except:
        print("Unable to detect java version"
              "If Java is not installed then QIS and QPS will run")


	
	# Scan for quarch devices on the system
    print("")
    print("Test Device Connection")
    print("")
    deviceList = scanDevices('all', favouriteOnly=False)
    print("Device list with ConnTarget:\r\n" +str(deviceList))
    moduleStr = userSelectDevice(deviceList, nice=True, tableHeaders=["Module", "ConnTarget"])
    if moduleStr == "quit":
        return 0
    print("Selected module is: "+moduleStr)
    # Create a device using the module connection string
    myDevice = quarchDevice(moduleStr)
    QuarchSimpleIdentify(myDevice)

    # Close the module before exiting the script
    myDevice.closeConnection()


'''
This function demonstrates a very simple module identify, that will work with any Quarch device
'''
def QuarchSimpleIdentify(device1):
    # Print the module name
    print("Running the simple identify example.\n")
    print("Module Name:"),
    print(device1.sendCommand("hello?"))

    # Print the module identify and version information
    print("\nModule Identity Information:\n")
    print(device1.sendCommand("*idn?"))

'''
Gets the version number of qis if already running and if not it launches qis and checks the version number
'''
def get_QIS_version():
    qis_version = ""
    my_close_qis = False
    if isQpsRunning() == False:
        my_close_qis = True
        startLocalQis()
        
    myQis = qisInterface()
    qis_version = myQis.sendAndReceiveCmd(cmd="$version")
    if "No Target Device Specified" in qis_version:
        qis_version = myQis.sendAndReceiveCmd(cmd="$help").split("\r\n")[0]
    if my_close_qis:
        myQis.sendAndReceiveCmd(cmd = "$shutdown")
    return qis_version


if __name__ == "__main__":
    main()