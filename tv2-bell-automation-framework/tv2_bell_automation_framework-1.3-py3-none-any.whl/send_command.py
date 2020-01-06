import time
import argparse
from tv2test.core import DeviceUnderTestFactory
from tv2test.platforms.mediafirst import MediaFirstHelper

'''
Python CLI command:
python <filename> --itachip <ITACHIP> --itachport <ITACHPORT> --delay <DELAY> <list of buttons to press>
Usage Example:
python send_mediafirst_command.py --itachip 192.168.1.75 --itachport 4998 --delay 2 MENU DOWN DOWN SELECT
'''

parser = argparse.ArgumentParser()
parser.add_argument('--itachip', required=True, help='itachip is the IP address of the iTach IR blaster')
parser.add_argument('--itachport', default=4998, type=int,
                    help='itachport is the port of the iTach IR blaster (defaults to 4998 if not specified)')
parser.add_argument('--delay', default=1.0,
                    help='delay is the number of seconds (float) to wait between commands (defaults to 1.0)')
parser.add_argument('buttons', nargs='*')

args = parser.parse_args()

test_options = {
    'itach_hostname': args.itachip,
    'itach_port': args.itachport,
    'max_duration': args.delay,
    'output_file': 'out_test_tune.mp4',
}

show_message = False

with DeviceUnderTestFactory().get_device('mediafirst', test_options) as dut:
    time.sleep(2.0)
    mf = MediaFirstHelper(dut)
    for button in args.buttons:
        dut.input.press(button, 1.0, show_message=show_message)
