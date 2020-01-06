
class RemoteControl:

    def press(self, key, delay=0.5):
        '''Abstract method to press a remote control button

        Args:
            key: Name of the button to press
            delay: Sleep time after button press is sent
        '''
        pass

    def press_and_wait(self, key, wait_fn):
        '''Abstract method to press a remote control button and wait

        Args:
            key: Name of the button to press
            wait_fn: Function to process display output from the device under test
        '''
        pass

class VoiceControl():

    def say_file(self, filename):
        '''Abstract method to play an audio file
        '''
        pass

    def say_tts(self, text):
        '''Abstract method to convert text to speech and play
        '''
        pass