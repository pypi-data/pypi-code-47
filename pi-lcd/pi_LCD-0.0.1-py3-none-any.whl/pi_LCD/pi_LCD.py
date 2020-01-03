from RPi.GPIO import *
import time as t
# Copyright (c) 2020 Ashish Sharma
# This module is part of the IOT Interfaces, which is released under a
# MIT licence.
class LCD:
    def __init__(self,mode = "BOARD",RS_pin = 3,EN_pin = 5,D4 = 7,D5 = 8,D6 = 10,D7 = 11):
        '''mode = BCM or BOARD
RS_pin = RS pin Number
EN_pin = Enable pin Number
D4     = D4 pin Number
D5     = D5 pin Number
D6     = D6 pin Number
D7     = D7 pin Number'''
        self.RS_pin = RS_pin
        self.EN_pin = EN_pin
        self.D4     = D4
        self.D5     = D5
        self.D6     = D6
        self.D7     = D7
        self.mode   = mode
        if self.mode == "BOARD":
            setmode(BOARD)
        elif self.mode == "BCM":
            setmode(BCM)
        setwarnings(False)
        self.pin_list=[D4,D5,D6,D7]
        for i in range (0,len(self.pin_list)):
            setup(self.pin_list[i],OUT)
        setup(self.RS_pin,OUT)
        setup(self.EN_pin,OUT)

        for i in range (0,len(self.pin_list)):
            output(self.pin_list[i],0)
        output(self.RS_pin,0)
        output(self.EN_pin,0)        
        self.CMD(0x01)
        self.CMD(0x02)
        self.CMD(0x28)
        self.CMD(0x06)
        self.CMD(0x0c)
    def PORT(self,P):
        j=0x10
        for i in range (0,len(self.pin_list)):
            if((P & j)==j):
                output(self.pin_list[i],1)
            else:
                output(self.pin_list[i],0)
            j=j*2

    def CMD(self,C):
        P=(C & 0xF0)
        self.PORT(P)
        output(self.RS_pin,0)
        output(self.EN_pin,1)
        t.sleep(0.01)
        output(self.EN_pin,0)

        P=((C<<4) & 0xF0)
        self.PORT(P)
        output(self.RS_pin,0)
        output(self.EN_pin,1)
        t.sleep(0.01)
        output(self.EN_pin,0)
        
    def DATA(self,d):
        P=(d & 0xF0)
        self.PORT(P)
        output(self.RS_pin,1)
        output(self.EN_pin,1)
        t.sleep(0.01)
        output(self.EN_pin,0)

        
        P=((d<<4) & 0xF0)
        self.PORT(P)
        output(self.RS_pin,1)
        output(self.EN_pin,1)
        t.sleep(0.01)
        output(self.EN_pin,0)

    def data_as_string(self,loc,text):
        '''show data as a string format'''
        g=''
        g=text
        self.CMD(loc)
        for i in range(0,len(g)):
            self.DATA(ord(g[i]))
            
    def clear_screen(self):
        '''clear screen '''
        self.CMD(0x01)
    def make_animation(self,char_data,RAM_loc):
        '''Example: char_data = ["00000100",
"00000100",
"00000100",
"00000100",
"00010101",
"00001110",
"00000100",
"00000000"]
RAM_loc = 0x40
make_animation(char_data,RAM_loc)'''
        self.char_data  = char_data
        self.RAM_loc    = RAM_loc
        self.CMD(RAM_loc)
        for i in self.char_data:
            self.DATA(int(i,2))
    def start_animation(self,ani_loc,ani_no):
        '''Example : start animation(0x80,0)'''
        self.CMD(ani_loc)
        self.DATA(ani_no)
