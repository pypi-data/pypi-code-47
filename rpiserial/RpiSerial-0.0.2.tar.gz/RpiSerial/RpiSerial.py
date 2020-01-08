import serial,time

# Copyright (c) 2020 Ashish Sharma
# This module is part of the IOT Interfaces, which is released under a
# MIT licence.

class Bluetooth:
    def __init__(self,port="/dev/ttyUSB0",baudrate=9600,timeout=0.5):
        self.Bluetooth_data=serial.Serial(port,baudrate,timeout=timeout)
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
    def __init__(self,port="/dev/ttyUSB0",baudrate=9600,timeout=0.3):
        self.RFID_data=serial.Serial(port,baudrate,timeout=timeout)
    def read(self):
        B_data = self.RFID_data.readline().decode('utf-8')
        if B_data == '':
            pass
        else:
            return B_data

class GPS:
    def __init__(self,port="/dev/ttyUSB0",baudrate=9600,timeout=0.5):
        self.GPS_data=serial.Serial(port,baudrate,timeout=timeout)
        
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
class GSM:
    def __init__(self,port="/dev/ttyUSB0",baudrate=9600,timeout=0.5):
        self.GSM_data=serial.Serial(port,baudrate,timeout=timeout)
        self.GSM_data.write("AT\r\n".encode('utf-8'))
        self.recvAck = self.GSM_data.read(100000).decode('utf-8')
    def call(self,contactNumber):
        self.contactNumbercommand = "ATD"+contactNumber+";\r\n"
        self.contactNumbercommand =self.contactNumbercommand.encode('utf-8')
        print("data : ",self.contactNumbercommand)
        self.GSM_data.write(self.contactNumbercommand)
        self.recvAck = self.GSM_data.read(100000).decode('utf-8')
        return self.recvAck
    def send_message(self,contactNumber,Message):
        self.send_messagecommand = '''AT+CMGS="'''+contactNumber+'''"\r\n'''
        self.send_messagecommand = self.send_messagecommand.encode('utf-8')
        self.GSM_data.write(self.send_messagecommand)
        self.recvAck = self.GSM_data.read(100000).decode('utf-8')
        time.sleep(1)
        self.send_messagecommand = Message+'''\x1a'''
        self.send_messagecommand = self.send_messagecommand.encode('utf-8')
        self.GSM_data.write(self.send_messagecommand)
        self.recvAck += self.GSM_data.read(100000).decode('utf-8')
        return self.recvAck
    def recv_message(self,message_location):
        self.message_init = "AT+CMGF=1\r\n"
        self.data = self.message_init.encode('utf-8')
        self.GSM_data.write(self.data)
        self.recv_ack = self.GSM_data.read(100000).decode('utf-8')
        
        self.message_location = "AT+CMGR="+str(message_location)+"\r\n"
        self.data = self.message_location.encode('utf-8')
        self.GSM_data.write(self.data)
        self.recv_ack = self.GSM_data.read(100000).decode('utf-8').split(',')
        self.recv_ack = self.recv_ack[4:len(self.recv_ack)]
        self.recv_ack1 = ""
        for i in self.recv_ack:
            self.recv_ack1 += i
        self.recv_ack1 = self.recv_ack1.split("\r\n")
        self.recv_ack1 = self.recv_ack1[1:len(self.recv_ack1)-3]
        self.recv_ack = ""
        for i in self.recv_ack1:
            self.recv_ack += i
        return self.recv_ack
    def send_AT(self,AT_command):
        self.GSM_data.write(AT_command.encode('utf-8'))
        self.recv_ack = self.GSM_data.read(100000).decode('utf-8')
        return self.recv_ack
