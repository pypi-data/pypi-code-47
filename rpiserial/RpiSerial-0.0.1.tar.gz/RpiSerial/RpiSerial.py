import serial

# Copyright (c) 2020 Ashish Sharma
# This module is part of the IOT Interfaces, which is released under a
# MIT licence.

class Bluetooth:
    def __init__(self,port="/dev/ttyUSB0",boudrate=9600,timeout=0.5):
        self.Bluetooth_data=serial.Serial(port,boudrate,timeout=timeout)
    def read(self):
        B_data = self.Bluetooth_data.readline().decode('utf-8')
        if B_data == '':
            pass
        else:
            return B_data
    def write(self,data):
        data = bytes(str(data).encode('utf-8'))
        self.Bluetooth_data.write(data)
        
class RFID:
    def __init__(self,port="/dev/ttyUSB0",boudrate=9600,timeout=0.3):
        self.RFID_data=serial.Serial(port,boudrate,timeout=timeout)
    def read(self):
        B_data = self.RFID_data.readline().decode('utf-8')
        if B_data == '':
            pass
        else:
            return B_data

class GPS:
    def __init__(self,port="/dev/ttyUSB0",boudrate=9600,timeout=0.5):
        self.GPS_data=serial.Serial(port,boudrate,timeout=timeout)
        
    def read(self):
        while True:
            try:
                GPS_recdata = self.GPS_data.readline().decode('utf-8')
                GPS_NEW_DATA=GPS_recdata.split(',')
                if '$GPRMC' in GPS_NEW_DATA:
                    Lat  = str(float(GPS_NEW_DATA[3])/100).split('.')
                    Lat1 = Lat[0]
                    Lat2 = str(int(int(Lat[1])/60))
                    Lat  = Lat1+'.'+Lat2
                    
                    Long = str(float(GPS_NEW_DATA[5])/100).split('.')
                    Long1 = Long[0]
                    Long2 = str(int(int(Long[1])/60))
                    Long  = Long1+'.'+Long2
                    
                    Time = str(int(float(GPS_NEW_DATA[1])))
                    Second = int(Time[-2::])
                    Minute = int(Time[-4:-2])+30
                    Hour   = int(Time[0:-4])+5
                    if Minute >= 60:
                        Minute = Minute-60
                        Hour = Hour+1
                    Time = str(Hour)+":"+str(Minute)+":"+str(Second)
                    
                    Date = GPS_NEW_DATA[9]
                    Date = Date[0:-4]+"/"+Date[-4:-2]+"/"+Date[-2::]
                    
                    return Lat,Long,Time,Date
                else:
                    pass
            except UnicodeDecodeError:
                pass
