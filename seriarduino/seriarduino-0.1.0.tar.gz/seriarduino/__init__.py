import serial
import os.path


class SeriArduino:
    serial = None

    def __init__(self, address = None, bauds = 9600):
        if address is None:
            for name in ['ACM0', 'ACM1', 'USB0', 'USB1']:
                serialAddress = '/dev/tty' + name
                if os.path.exists(serialAddress):
                    break

        self.serial = serial.Serial(serialAddress, bauds)

    def write(self, val):
        self.serial.write(str(">" + val + "<").encode())
        
    def read(self):
        data = None
        while True:
            data = self.serial.readline().decode()[:-2]
            if data.startswith(">") and data.endswith("<"): # the commands are encapsulated
                data = data[1:-1] # we strip the encapsulation characters
                break # exit while
            else:
                print("[Arduino Serial] " + data) # we still print the other Arduino messages
        return data
