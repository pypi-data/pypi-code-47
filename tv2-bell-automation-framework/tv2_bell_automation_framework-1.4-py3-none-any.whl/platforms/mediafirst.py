'''
This module contains classes specific to the Ericsson MediaFirst platform.
'''

import cv2
import os
import time
import numpy as np
from tv2test.devices.core import RemoteControl
from tv2test.devices.itachirblaster import ITachIRBlaster
import tv2test.imgmatch as imgmatch
import tv2test.ocr as ocr
from datetime import datetime
from tv2test.display import Region
from tv2test.constants import ConstantPosterRegions


class MediaFirstRemoteControl(RemoteControl):
    '''
    Class to send IR codes to MediaFirst set-top boxes.

    IR codes have been learned from an Arris VIP5662W set-top box.
    '''

    key_codes = {
        "SELECT" : {
            "name" : "[SELECT]",
            "code" : "sendir,1:1,4,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,12,12,12,12,12,12,24,12,3452,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,12,12,12,12,12,12,24,12,3433,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,24,12,12,12,12,12,12,24,12,12,24,12,3800\r\n"
        },
         "EXIT" : {
            "name" : "[EXIT]",
            #"code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,12,12,24,24,24,12,3442,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,12,12,24,24,24,12,3424,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,12,12,24,24,24,12,3423,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,12,12,12,12,24,24,12,12,24,12,12,12,3800\r\n"
            "code": "sendir,1:1,1,38109,1,1,11,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,12,12,24,24,24,12,3438,11,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,12,12,24,24,24,12,3448,11,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,12,12,24,24,24,12,3421,11,24,24,12,12,12,12,24,12,12,24,24,24,12,12,24,12,12,24,12,12,12,12,24,12,12,12,3800\r\n"
        },
        "MENU" : {
            "name" : "[MENU]",
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,24,12,12,24,24,24,12,3455,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,24,12,12,24,24,24,12,3409,12,24,24,12,12,12,12,24,12,12,24,24,24,24,12,12,12,12,24,12,12,24,24,24,12,3800\r\n"
        },
        "ON_DEMAND": {
            "name": "[ON_DEMAND]",
            "code": "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,12,12,24,24,12,12,24,24,3446,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,12,12,24,24,12,12,24,24,3800\r\n"
        },
        "INFO" : {
            "name" : "[INFO]",
            "code" : "sendir,1:1,2,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,24,24,12,12,12,12,24,12,3425,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,24,24,12,12,12,12,24,12,3409,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,24,12,12,24,12,12,12,12,12,12,12,12,3800\r\n"
        },
        "GUIDE" : {
            "name" : "[GUIDE]",
            "code" : "sendir,1:1,5,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,12,12,12,12,12,12,24,12,3429,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,12,12,12,12,12,12,24,12,3418,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,12,12,12,12,12,12,24,12,3419,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,12,12,12,12,24,12,12,24,24,12,12,12,3800\r\n" 
        },
        "VOD" : {
            "name" : "[VOD]", 
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,12,12,24,24,12,12,24,24,3451,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,12,12,24,24,12,12,24,24,3468,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,12,12,24,24,12,12,24,24,3469,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,12,12,24,24,12,12,24,24,3418,12,24,24,12,12,12,12,24,12,12,24,24,24,24,12,12,24,24,24,12,12,24,12,12,12,3800\r\n" 
        },
        "UP" : { 
            "name" : "[UP]",
            "code": "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,12,12,24,12,12,24,3410,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,12,12,24,12,12,24,3435,12,24,24,12,12,12,12,24,12,12,24,24,24,24,12,12,24,24,24,24,24,24,12,3800\r\n"
        },
        "DOWN" : { 
            "name" : "[DOWN]",
            "code" : "sendir,1:1,3,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,12,12,24,24,24,12,3449\r\n"
        },
        "RIGHT" : {
            "name" : "[RIGHT]",
            "code" : "'sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,24,12,12,12,12,12,12,24,3454,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,24,12,12,12,12,12,12,24,3437,12,24,24,12,12,12,12,24,12,12,24,24,24,24,24,12,12,24,12,12,24,24,12,12,12,3800\r\n"
        },
        "LEFT" : {
            "name" : "[LEFT]",
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,12,12,12,12,24,24,3445,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,12,12,12,12,24,24,3414,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,12,12,12,12,24,24,3426,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,24,12,12,12,12,12,12,24,12,12,24,12,3800\r\n"
        },
        "1" : { 
            "name" : "[1]",
            "code" : "​​sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,12,12,24,24,12,3418,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,12,12,24,24,12,3445,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,12,12,24,24,12,3422,12,24,24,12,12,12,12,24,12,12,24,24,24,24,12,12,24,24,12,12,24,24,12,12,12,3800\r\n" 
        },
        "2" : {
            "name" : "[2]",
            "code" : "sendir,1:1,2,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,24,24,3398,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,24,24,3438,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,24,24,3409,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,24,24,3800\r\n"
        },
        "3" : {
            "name" : "[3]",
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,12,12,24,12,3465,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,12,12,24,12,3449,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,12,12,24,12,3416,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,12,12,24,12,3449,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,12,12,24,12,3449,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,12,12,24,12,3416,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,12,12,24,12,12,24,12,3438,12,24,24,12,12,12,12,24,12,12,24,24,24,24,24,12,12,12,12,12,12,24,24,24,12,3800\r\n"
        },
        "4" : {
            "name" : "[4]",
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,24,12,12,24,3453,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,24,12,12,24,3424,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,24,12,12,24,3800\r\n"
        },
        "5" : {
            "name" : "[5]",
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,24,24,24,12,3407,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,24,24,24,12,3800\r\n"
        },
        "6" : {
            "name" : "[6]",
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,12,12,24,24,3430,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,12,12,24,24,3409,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,12,12,24,24,3800\r\n"
        },
        "7" : {
            "name" : "[7]",
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,12,12,12,12,24,12,3433,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,12,12,12,12,24,12,3444,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,12,12,24,12,12,12,12,24,12,3800\r\n"
        },
        "8" : {
            "name" : "[8]",
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,24,12,12,12,12,24,3412,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,24,12,12,12,12,24,3800\r\n"
        },
        "9" : {
            "name" : "[9]",
            "code" : "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,24,12,12,24,24,12,3420,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,24,12,12,24,24,12,3444,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,24,12,12,24,24,12,3800\r\n"
        },
        "0": {
            "name": "[0]",
            "code": "sendir,1:1,3,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,24,24,24,24,3405,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,24,24,24,24,3445,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,12,12,24,24,24,24,24,3800\r\n"
        },
        "SEARCH": {
            "name": "[SEARCH]",
            "code": "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,12,12,24,24,12,12,12,12,12,12,3800\r\n"
        },
        "APP_LAUNCHER": {
            "name": "[APP_LAUNCHER]",
            "code": "sendir,1:1,1,37993,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,24,12,12,12,12,12,12,12,12,12,3422,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,24,12,12,12,12,12,12,12,12,12,3429,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,12,12,12,12,24,24,24,24,12,12,3700\r\n"
        },
        "PAUSE": {
            "name": "[PAUSE]",
            "code": "sendir,1:1,1,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,24,24,12,12,24,12,3413,12,12,12,24,24,24,12,12,12,12,24,24,24,24,12,12,24,12,12,24,24,12,12,24,12,3438,12,24,24,12,12,12,12,24,12,12,24,24,24,24,24,24,24,12,12,24,12,12,24,3800\r\n"
        },
        "SKIP_BACK": {
            "name": "[SKIP_BACK]",
            "code": "sendir,1:1,10,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,12,12,12,12,12,12,24,24,12,3442,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,12,12,12,12,12,12,24,24,12,3460,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,24,12,12,24,12,12,24,12,12,24,3800\r\n"
        },
        "SKIP_FORWARD": {
            "name": "[SKIP_FORWARD]",
            "code": "sendir,1:1,3,38109,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,12,12,24,24,12,12,24,3411,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,12,12,24,24,12,12,24,3454,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,12,12,12,12,24,24,12,12,12,12,12,12,3800\r\n"
        },
        "REWIND": {
            "name": "[REWIND]",
            "code": "sendir,1:1,1,37993,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,12,12,12,12,24,24,24,3413,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,12,12,12,12,24,24,24,3420,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,12,12,12,12,24,24,12,12,12,12,12,12,3700\r\n"
        },
        "FAST_FORWARD": {
            "name": "[FAST_FORWARD]",
            "code": "sendir,1:1,1,37993,1,1,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,12,12,12,12,24,12,12,24,12,3442,12,12,12,24,24,24,12,12,12,12,24,24,24,24,24,24,12,12,12,12,24,12,12,24,12,3448,12,24,24,12,12,12,12,24,12,12,24,24,24,12,12,12,12,12,12,24,24,12,12,12,12,12,12,3700\r\n"
        }
    }

    def __init__(self, hostname, port=4998, dut=None):
        self.itachirblaster = ITachIRBlaster(hostname, port)
        self.dut = dut

    def press(self, key, message=None, delay=0.5, show_message=True, timestamp_name=None):
        '''
        Press a MediaFirst remote control button

        Args:
            button: Name of the button to press
            delay: Sleep time after button press is sent
            show_message: To show the message on display
            timestamp_name: Name of the timestamp to append on the list
        '''
        if key in self.key_codes:
            print('INPUT KEY PRESS :::', key)
            code = self.key_codes[key]['code']
            # To add message in the video, if the flag is True
            if show_message:
                self.dut.display.add_text_annotation(key, background_color=(0, 200, 0))
                if message is not None:
                    self.dut.display.add_text_annotation(message)

            self.itachirblaster.send_command(code, delay)
            key_press_timestamp = time.time()
            if not timestamp_name:
                timestamp_name = '%s press' % (key)
            self.dut.timestamps.append({timestamp_name: key_press_timestamp})
            time.sleep(delay)
        else:
            raise Exception('Key not found: ' + key)

    def press_and_wait(self, key, wait_fn, message=None):
        '''
        Press a MediaFirst remote control button and wait

        Args:
            button: Name of the button to press
            wait_fn: Function to process display output from the device under test
        '''
        if key in self.key_codes:
            code = self.key_codes[key]['code']
            self.dut.display.add_text_annotation(key, background_color=(0, 200, 0))
            if message is not None:
                self.dut.display.add_text_annotation(message)
            self.itachirblaster.send_command(code)
            wait_fn()
        else:
            raise Exception('Key not found: ' + key)


class MediaFirstHelper:
    '''
    Class containing helper functions for MediaFirst testing
    '''

    def __init__(self, dut):
        self.dut = dut
        self.dut.timestamps.append({'test_start_time': time.time()})

    def initialize_screen(self):
        self.dut.display.add_text_annotation('Resetting test case', top_left_cord_pos=(0, 0), duration=6.0)
        self.dut.input.press('MENU')
        time.sleep(2.0)
        gvision = ocr.GVisionOcr()
        execution_start_time = time.time()
        timeout_time = 15.0
        #text_name = '"Please Wait"'
        while True:
            frame = self.dut.display.get_frame()
            please_wait_text_check = gvision.ocr_text(self.dut, frame, Region(810, 94, 316, 120), text='Checking for \'Please Wait\'')
            print('PLEASE WAIT TEXT :: ', please_wait_text_check)
            if len(please_wait_text_check) == 0:
                break
            if not please_wait_text_check[0] == 'Please wait':
                break
            if time.time() - execution_start_time >= timeout_time:
                print('INITIAL TIMEOUT FAILURE')
                break
        self.dut.input.press('GUIDE', timestamp_name='initialize_guide_1')
        self.dut.input.press('GUIDE', timestamp_name='initialize_guide_2')

    def tune_to_channel(self, channel_number, show_message=True):
        '''
        Tune to the specified live channel
        '''
        if show_message:
            self.dut.display.add_text_annotation('Tune to channel ' + str(channel_number), duration=6.0)

            # Check if guide is open
            frame = self.dut.display.get_frame()
            gvision = ocr.GVisionOcr()
            texts = gvision.ocr_text(self.dut, frame, Region(36, 28, 352, 142))
            guide_open = False
            for text in texts:
                if 'guide' in text.lower():
                    guide_open = True

            # Open guide to exit any apps
            if not guide_open:
                self.dut.input.press('GUIDE')
                frame = self.dut.display.get_frame()
                gvision = ocr.GVisionOcr()
                texts = gvision.ocr_text(self.dut, frame, Region(36, 28, 352, 142))
                guide_open = False
                for text in texts:
                    if 'guide' in text.lower():
                        guide_open = True

                if not guide_open:
                    raise Exception('Cannot open guide')

        # Close the guide
        self.dut.input.press('GUIDE', 1.0)

        if show_message:
            # Tune to channel
            self.dut.display.add_text_annotation('Tune to channel ' + str(channel_number))
        channel_str = str(channel_number)
        for n in channel_str:
            self.dut.input.press(n)
        time.sleep(1.0)
        self.dut.input.press('DOWN')

    def initialize_guide_screen(self):
        '''
        Press commands to initialize the guide screen
        '''
        self.dut.input.press('SELECT', 3.0)
        self.dut.input.press('GUIDE', 3.0)

    def initial_guide_time(self):
        '''
        Returns the date and time of the initial guide screen.
        '''
        gvision = ocr.GVisionOcr()
        frame = self.dut.display.get_frame()
        now_date = gvision.ocr_text(self.dut, frame, Region(70, 430, 280, 95))[0].split(' ')[-1]
        now_time = gvision.ocr_text(self.dut, frame, Region(1610, 50, 280, 95))[0]
        now_date_time_str = '%s %s' % (now_date, now_time)
        now_datetime = datetime.strptime(now_date_time_str, '%m/%d %I:%M %p')
        return now_datetime

    def get_current_guide_time(self):
        '''
        Validate the guide text is present in the current screen.
        Returns program title from the guide screen.
        Returns date time from current guide screen.
        '''
        validate_guide_text = True
        current_screen_datetime = None
        program_title = None
        frame = self.dut.display.get_frame()
        gvision = ocr.GVisionOcr()
        guide_text = gvision.ocr_text(self.dut, frame, Region(80, 40, 230, 90))[0]
        if guide_text.lower() != 'guide':
            validate_guide_text = False
            return validate_guide_text, current_screen_datetime, program_title
        program_title = gvision.ocr_text(self.dut, frame, Region(403, 503, 437, 65))[0]
        extracted_string = gvision.ocr_text(self.dut, frame, Region(70, 430, 580, 95))
        current_screen_date = extracted_string[0].split(' ')[-1]
        current_screen_time = extracted_string[1]
        current_screen_date_time_str = '%s %s' % (current_screen_date, current_screen_time)
        current_screen_datetime = datetime.strptime(current_screen_date_time_str, '%m/%d %I:%M %p')
        return validate_guide_text, current_screen_datetime, program_title

    def validate_reached_screen(self, expected_date, current_screen_datetime):
        '''
        Validate the current screen has reached the expected screen.
        Reach the expected screen, if not reached.
        '''
        while (expected_date.month != current_screen_datetime.month and
               expected_date.day != current_screen_datetime.day and
               expected_date.hour != current_screen_datetime.hour):
            if expected_date.month != current_screen_datetime.month:
                total_month_clicks = abs((current_screen_datetime.month - expected_date.month) * 1440)
                if expected_date.month < current_screen_datetime.month:
                    for click in range(total_month_clicks):
                        self.dut.input.press('RIGHT', 1.0)
                else:
                    for month in range(total_month_clicks):
                        self.dut.input.press('LEFT', 1.0)
            if expected_date.day != current_screen_datetime.day:
                total_day_clicks = abs((current_screen_datetime.day - expected_date.day) * 48)
                if expected_date.day < current_screen_datetime.day:
                    for day in range(total_day_clicks):
                        self.dut.input.press('RIGHT', 1.0)
                else:
                    for day in range(total_day_clicks):
                        self.dut.input.press('LEFT', 1.0)
            if expected_date.hour != current_screen_datetime.hour:
                total_hour_clicks = abs((current_screen_datetime.hour - expected_date.hour) * 2)
                if expected_date.hour < current_screen_datetime.hour:
                    for hour in range(total_hour_clicks):
                        self.dut.input.press('RIGHT', 1.0)
                else:
                    for hour in range(total_hour_clicks):
                        self.dut.input.press('LEFT', 1.0)

    def open_bell_app_launcher(self):
        '''
        Returns success or failure boolean value to check whether the app launched or not.
        Returns the time taken to launch the bell app launcher.
        '''
        launch_success = False
        timeout_time = 15.0
        time_taken = 0.0

        def validate_bell_app_launcher():
            frame = self.dut.display.get_frame()
            template_support_icon = cv2.imread(os.path.join(os.path.dirname(__file__), 'templates', 'mediafirst', 'template_support_icon.png'))
            template_youtube_icon = cv2.imread(os.path.join(os.path.dirname(__file__), 'templates', 'mediafirst', 'template_youtube_icon.png'))
            template_netflix_icon = cv2.imread(os.path.join(os.path.dirname(__file__), 'templates', 'mediafirst', 'template_netflix_icon.png'))
            if (imgmatch.match_template(self.dut, template_support_icon, frame, crop_rect=Region(0, 960, 1900, 100)) or
                imgmatch.match_template(self.dut, template_youtube_icon, frame, crop_rect=Region(0, 960, 1900, 100)) or
                imgmatch.match_template(self.dut, template_netflix_icon, frame, crop_rect=Region(0, 960, 1900, 100))):
                return True
            return False

        try:
            self.dut.input.press('MENU')
            execution_start_time = time.time()
            self.dut.input.press('APP_LAUNCHER')

            while True:
                if validate_bell_app_launcher():
                    self.dut.timestamps.append({'bell_app_launched_at': time.time()})
                    time_taken = time.time() - execution_start_time
                    self.dut.append_duration("bell_app_launch", time_taken)
                    launch_success = True
                    break
                if time.time() - execution_start_time >= timeout_time:
                    print('TIMEOUT FAILURE')
                    break
        except Exception as e:
            pass
        print('LAUNCH SUCCESS FLAG ::: ', launch_success)
        return launch_success

    def record_timestamp(self, timestamp_name):
        '''
        Record a timestamp manually
        '''
        self.dut.timestamps.append({timestamp_name: time.time()})

    def record_duration(self, duration_name):
        '''
        Record a duration manually
        '''
        self.dut.append_duration(duration_name, time.time())

    def calculate_duration(self, duration_name, start_timestamp_nm, end_timestamp_nm):
        '''
        Adds a new duration with the time difference between two timestamps
        '''
        start_timestamp = 0.0
        end_timestamp = 0.0
        for timestamp in reversed(self.dut.timestamps):
            if end_timestamp_nm in timestamp.keys():
                end_timestamp = timestamp[end_timestamp_nm]
                end_timestamp_index = (self.dut.timestamps).index(timestamp)
                break
        for timestamp in reversed(self.dut.timestamps[:end_timestamp_index]):
            if start_timestamp_nm in timestamp.keys():
                start_timestamp = timestamp[start_timestamp_nm]
                break
        duration_diff = end_timestamp - start_timestamp
        self.dut.append_duration(duration_name, time.time())

    def calculate_intermediate_duration(self, duration_name, start_timestamp_nm,
                                        intermediate_timestamp_nm, end_timestamp_nm):
        '''
        Adds a new duration with the time difference between intermediate timestamps
        '''
        start_timestamp = 0.0
        intermediate_timestamp = 0.0
        end_timestamp = 0.0
        for timestamp in reversed(self.dut.timestamps):
            if end_timestamp_nm in timestamp.keys():
                end_timestamp = timestamp[end_timestamp_nm]
                last_index = (self.dut.timestamps).index(timestamp)
                break
        for timestamp in reversed(self.dut.timestamps[:last_index]):
            if intermediate_timestamp_nm in timestamp.keys():
                intermediate_timestamp = timestamp[intermediate_timestamp_nm]
                last_index = (self.dut.timestamps).index(timestamp)
                break
        for timestamp in reversed(self.dut.timestamps[:last_index]):
            if start_timestamp_nm in timestamp.keys():
                start_timestamp = timestamp[start_timestamp_nm]
                break
        if intermediate_timestamp == 0.0:
            duration_diff = end_timestamp - start_timestamp
        else:
            duration_diff = end_timestamp - intermediate_timestamp
        self.dut.append_duration(duration_name, duration_diff)

    def verify_vod_bell_icon(self):
        '''
        Verify whether the Bell logo is present in the VOD store
        '''
        template_bell_icon = cv2.imread(os.path.join(os.path.dirname(__file__), 'templates', 'mediafirst', 'template_vod_bell_icon.png'))
        return imgmatch.match_template(self.dut, template_bell_icon, self.dut.display.get_frame(),
                                        crop_rect=Region(24, 24, 370, 200), timestamp_name='vod_bell_logo_verified_at')

    def vod_launch(self, timeout_time=15.0):
        '''
        Launch the VOD store
        Verify whether the Bell logo is present in the VOD store
        Return is_vod_launched flag
        '''
        # Press the VOD button to launch the VOD store
        self.dut.input.press('VOD', timestamp_name='vod_select_press')
        # Confirm VOD store launched by finding the large Bell logo at the top of the menu
        execution_start_time = time.time()
        while True:
            if self.verify_vod_bell_icon():
                self.calculate_duration('vod_launch_time', 'vod_select_press', 'vod_bell_logo_verified_at')
                return True
            if time.time() - execution_start_time >= timeout_time:
                print('VOD launch TIMEOUT FAILURE')
                return False
        return False

    def detect_vod_poster(self):
        '''
        Detect the poster in the VOD store
        '''
        constant_class = ConstantPosterRegions()
        if asset_type == 'season':
            crop_rect = constant_class.series_poster_region
        elif asset_type == 'movie':
            crop_rect = constant_class.movie_poster_region  
        else :
            crop_rect = Region(474, 298, 1422, 416)

        frame = self.dut.display.get_frame()
        annotation = self.dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.width, crop_rect.height),
                                                        text='poster detect', duration=2.0)
        cropped_frame = frame[crop_rect.y:crop_rect.y + crop_rect.height,
                              crop_rect.x:crop_rect.x + crop_rect.width]
        histogram_value = cv2.calcHist([cropped_frame], [0], None, [256], [0, 256])

        if np.size(np.where(histogram_value > 100)) > 100:
            self.dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.width, crop_rect.height),
                                    text='poster detect',
                                    duration=3.0,
                                    color=(0,128, 0),
                                    annotation_id=annotation.annotation_id)
            return True
        return False

    def search_and_detect_new_releases(self):
        '''
        Search and verify new releases.
        '''
        for i in range(9):
            frame = self.dut.display.get_frame()
            gvision = ocr.GVisionOcr()
            texts = gvision.ocr_text(self.dut, frame, Region(1280, 54, 600, 85),text='New release movies')
            
            for text in texts :
                if 'New release movies' in text:
                    self.dut.input.press('SELECT')
                    return True
            self.dut.input.press('DOWN')
        return False
