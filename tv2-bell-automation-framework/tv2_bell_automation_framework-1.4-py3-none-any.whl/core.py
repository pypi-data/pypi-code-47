'''
This module contains core classes for the tv2test package.

Classes:

DeviceUnderTest
    This is the primary class used by test cases to exercise
    the device under test and process display output.

DeviceUnderTestFactory
    This class is a factory for creating platform specific
    DeviceUnderTest class instances by configuring appropriate
    input and display objects.
'''
from tv2test.display import Display, _mainloop
from tv2test.platforms.mediafirst import MediaFirstRemoteControl
from tv2test.platforms.mediaroom import MediaRoomRemoteControl
import time


class DeviceUnderTestFactory():
    '''
    Factory class for DeviceUnderTest objects.

    Use get_device to create DeviceUnderTest objects configured
    for different platforms.
    '''
    def get_device(self, device_type, options):
        '''
        Factory method to construct DeviceUnderTest for a specific platform.
        '''

        factories = {
            'mediafirst': self.get_mediafirst_device,
            'mediaroom': self.get_mediaroom_device,
            'googlehome': self.get_google_home_device
        }
        factory = factories.get(device_type, 'Device type not recognized')
        if isinstance(factory, str):
            raise Exception(factory)
        return factory(options)

    def get_mediafirst_device(self, options):
        '''
        Create a DeviceUnderTest instance for MediaFirst
        '''

        if 'itach_hostname' in options:
            hostname = options['itach_hostname']
            port = options.get('itach_port', 4998)
            max_duration = options.get('max_duration', 30)
            output_file = options.get('output_file', 'output.mp4')
            dut = DeviceUnderTest('mediafirst', options)
            #dut.set_display(Display())
            dut.set_display(Display(_mainloop, output_file, options.get('is_video_recording', True)))
            dut.set_input(MediaFirstRemoteControl(hostname, port, dut))
            #dut.display.start(output_file, max_duration)

            return dut

    def get_mediaroom_device(self, options):
        '''
        Create a DeviceUnderTest instance for MediaRoom
        '''

        if 'itach_hostname' in options:
            hostname = options['itach_hostname']
            port = options.get('itach_port', 4998)
            max_duration = options.get('max_duration', 30)
            output_file = options.get('output_file', 'output.mp4')
            dut = DeviceUnderTest('mediaroom', options)
            #dut.set_display(Display())
            dut.set_display(Display(_mainloop, output_file, options.get('is_video_recording', True)))
            dut.set_input(MediaRoomRemoteControl(hostname, port, dut))
            #dut.display.start(output_file, max_duration)

            return dut

    def get_google_home_device(self, options):
        '''
        Create a DeviceUnderTest instance for Google Home testing with
        video capture output
        '''
        return DeviceUnderTest('googlehome', options)

class DeviceUnderTest():
    '''
    Class representing the device under test.

    The device under test is a combination of display and input
    objects which allow commands to be sent and output to be
    processed.

    Args:
        device_type: String identifier of the device (e.g. napa)
    '''

    def __init__(self, device_type, options):
        self.device_type = device_type
        self.options = options
        self.input = None
        self.display = None
        self.timestamps = []
        self._durations = []

    def __enter__(self):
        print('DeviceUnderTest.__enter__')
        self.display.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.display is not None:
            start_ts_found = False
            print('TIMESTAMPS ::')
            for timestamp in self.timestamps:
                for key, value in timestamp.items():
                    if key == 'test_start_time' and not start_ts_found:
                        start_timestamp = value
                        start_ts_found = True
                    if start_ts_found:
                        print('%s : %s secs' % (key, round(value - start_timestamp, 2)))
            print('\nDURATIONS ::')
            for duration in self.durations:
                print('%s : %s' % (duration["duration_name"], round(duration[(duration["duration_name"]+"_time")],2)))
            #self.display.stop()
            self.display.__exit__(exc_type, exc_val, exc_tb)

    def set_input(self, input):
        '''
        Set the input property for the device under test
        '''
        self.input = input

    def set_display(self, display):
        '''
        Set the display property for the device under test
        '''
        self.display = display

    def append_duration(self, duration_name:str, time:float):
        self._durations.append({"duration_name": duration_name, (duration_name+"_time"): time})
 
    @property
    def durations(self):
        return self._durations
