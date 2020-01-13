import rtmidi
import time

class midi:

    def __init__(self, midiport):

        self.midiout = rtmidi.MidiOut()
        if midiport == 'virtual':
            print('Virtual midi port used')
            self.midiout.open_virtual_port('Virtual Midi Out')
        else:
            self.midiout.open_port(int(midiport))

    def cc_tx(self, control_number, value):

        message = [0xB0, int(control_number), int(value)]
        self.midiout.send_message(message)

    def close(self):
        del self.midiout

