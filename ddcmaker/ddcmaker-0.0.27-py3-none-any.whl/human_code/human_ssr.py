from ddcmaker.public.Serial_Servo_Signal import serial_signal as sg


class serial_human(sg):
    def __init__(self):
        super().__init__()
        self.Xpath = "/home/pi/human_code/ActionGroups/"
