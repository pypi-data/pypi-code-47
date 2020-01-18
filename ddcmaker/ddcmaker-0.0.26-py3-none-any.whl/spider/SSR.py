from ddcmaker.public.Serial_Servo_Signal import serial_signal as sg


class serial_spider(sg):
    def __init__(self):
        super().__init__()
        self.Xpath = "/home/pi/hexapod/ActionGroups/"
