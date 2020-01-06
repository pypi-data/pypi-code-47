import gc
import os
import sys
import time
import unittest
import argparse
import traceback
from datetime import datetime
from tv2test.config import config_vars
from importlib import import_module
from tv2test.core import DeviceUnderTestFactory
from tv2test.platforms.mediafirst import MediaFirstHelper
from tv2test.platforms.mediaroom import MediaRoomHelper
from tv2test.extend_test_framework import TestCaseModule
from tv2test.constants import ConstDeviceNames

'''
Python CLI command:
python <filename> <list of test cases path> --itachip <ITACHIP> --itachport <ITACHPORT> 
--iters <NUMBER_OF_ITERATIONS> -c <VALUE> --vdev <VIDEO_DEVICE>
Usage Example:
python tv2test-run.py test_case_path_1 test_case_path_2 --itachip 192.168.1.75 --itachport 4998 
--iters 2 -c True --vdev /dev/video0
'''

# Order of arguments value assignment
# 1. argument from args parse
# 2. variables from config file
# 3. environment variable

itachip_default = config_vars.get('ITACHIP', os.environ.get('ITACHIP', None))
itachport_default = config_vars.get('ITACHPORT', os.environ.get('ITACHPORT', None))
vdev_default = config_vars.get('VDEV', os.environ.get('VDEV', None))
iters_default = config_vars.get('ITERS', os.environ.get('ITERS', 1))
teams_webhook_url_default = config_vars.get('TEAMS_WEBHOOK_URL', os.environ.get('TEAMS_WEBHOOK_URL', None))
elk_url_default = config_vars.get('ELK_URL', os.environ.get('ELK_URL', None))
google_api_key_default = config_vars.get('GOOGLE_API_KEY', os.environ.get('GOOGLE_API_KEY', None))
is_video_recording_default = config_vars.get('IS_VIDEO_RECORD', os.environ.get('IS_VIDEO_RECORD', True))

parser = argparse.ArgumentParser()
parser.add_argument('--itachip', default=itachip_default, help='itachip is the IP address of the iTach IR blaster')
parser.add_argument('--itachport', default=itachport_default, type=int,
                    help='itachport is the port of the iTach IR blaster (defaults to 4998, if not specified)')
parser.add_argument('--vdev', default=vdev_default,
                    help='Video device (defaults to \'/dev/video0\', if not specified)')
parser.add_argument('-c', help='To continuously run tests')
parser.add_argument('--iters', default=iters_default, type=int, help='To run tests n number of times (defaults to 1, if not specified)')
parser.add_argument('--teams_webhook_url', default=teams_webhook_url_default, help='Webhook URL to post fail test case result in MS Teams')
parser.add_argument('--elk_url', default=elk_url_default, help='ELK URL to post test case details to elastic search')
parser.add_argument('--google_api_key', default=google_api_key_default, help='Google API Key for Google vision OCR')
parser.add_argument('--is_video_recording', default=is_video_recording_default, help='Flag to check whether to save and record video')
parser.add_argument('test_cases', nargs='*', help='<package>/<class>/<function>')

args = parser.parse_args()
test_number = 1

# Iterate over the number of times to execute the test cases, Or continous execution
while True if args.c else args.iters > 0:
    # Iterate over the test cases to run
    for test_case_path in args.test_cases:
        try:
            test_case_full_path = 'tests/%s' % test_case_path
            test_path_partition = test_case_full_path.rpartition('/')
            filename = test_path_partition[0]
            funcname = test_path_partition[-1]
            test_case_name =  filename.rpartition('/')[-1]
            video_output_file_name = 'out_%s.mp4' % test_case_name

            import_dir, module_file = os.path.split(os.path.abspath(filename))
            import_name, module_ext = os.path.splitext(module_file)

            # Import module
            sys.path.insert(0, import_dir)
            mod = import_module(import_name)
            test_case_class = getattr(mod, funcname)

            test_case_device_name = (getattr(test_case_class, "get_device_name"))(test_case_class)

            print("====== Device Name:-", test_case_device_name)

            options = {
                'itach_hostname': args.itachip,
                'teams_webhook_url': args.teams_webhook_url,
                'elk_url':args.elk_url,
                'google_api_key': args.google_api_key,
                'is_video_recording': args.is_video_recording,
                'output_file': video_output_file_name
            }

            test_result = False
            timeout_time = 15.0
            test_options = options.copy()

            with DeviceUnderTestFactory().get_device(test_case_device_name, test_options) as dut:
                device_names = ConstDeviceNames()
                mf = None

                if device_names.MEDIA_FIRST == test_case_device_name:
                    mf = MediaFirstHelper(dut)
                elif device_names.MEDIA_ROOM == test_case_device_name:
                    mf = MediaRoomHelper(dut)
                
                mf.initialize_screen()
                dut.display.add_text_annotation('Starting test case: %s' % test_case_name, top_left_cord_pos=(0, 0), duration=12.0)

                suite = unittest.TestSuite()
                suite.addTest(TestCaseModule.parametrize(test_case_class, dut=dut, mf=mf, test_name=test_case_name, test_result=test_result, test_number=test_number))
                runner = unittest.TextTestRunner(verbosity=2)
                result = runner.run(suite)
                timestamps = dut.timestamps

            time.sleep(3.0)
            TestCaseModule.merge_audio_video(video_output_file_name, timestamps)
            test_number += 1
            del sys.modules[import_name]
            objects = gc.collect()
            print("NO OF OBJECTS: ",objects)
            TestCaseModule.memory_check()
        except Exception as err:
            # EXCEPTION LOGGING BLOCK
            print('EXCEPTION OCCURRED ::: ', err)
            if 'filename' not in locals():
                filename = 'Un-Identified'
            with open("error_logs.txt", "a") as log:
                date_now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                log.write('\n--------------------------------\n\n')
                log.write('ERROR LOG-DATE : %s\nTEST CASE : %s\nERROR TRACEBACK (Details):\n' % (date_now_str, filename))
                traceback.print_exc(file=log)
            pass
    n = gc.collect()
    print('UNREACHABLE OBJECTS:', n)
    args.iters -= 1
