import unittest
import traceback
from datetime import datetime
from tv2test.merge_audio_video import MGAudio, MGVideo, MergeAudioVideo 
from tv2test.constants import ConstTestCaseFailReason, ConstDeviceNames, ConstElk, ConstTCType
import requests
import json
import time
import abc
import os
from tv2test.elk_bell import ELKBell, ELKBellDocMapping
from tv2test.utilities.system_utility import SystemUtility
from config import config_vars


class TestCaseModule(unittest.TestCase, metaclass=abc.ABCMeta):
    """
    TestCase classes that need to be parametrized should
    inherit from this class.
    """
    audio_file_path = None

    def __init__(self, method_name='run_test', test_name=None, dut=None, mf=None, test_result=False, test_number=0, audio_file_path=None):
        super(TestCaseModule, self).__init__(method_name)
        const_tc_type = ConstTCType()
        self.test_name = test_name
        self.dut = dut
        self.mf = mf
        self.test_result = test_result
        self.test_number = test_number
        self.const_fail_reason = ConstTestCaseFailReason()
        self.fail_reason = None
        self.tc_type = const_tc_type.BELL_TEST_CASE
        audio_file_path = audio_file_path

    'Abstract method to get device name. Every inherited class must implement this method to return device name'
    @classmethod
    @abc.abstractmethod
    def get_device_name(cls):
        raise NotImplementedError

    @staticmethod
    def parametrize(testcase_klass, test_name=None, dut=None, mf=None, test_result=False, test_number=0, audio_file_path=None):
        """
        Create a suite containing all tests taken from the given
        subclass, passing them the parameters.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        suite.addTest(testcase_klass(testnames[0], test_name=test_name, dut=dut, mf=mf, test_result=test_result, test_number=test_number))
        return suite

    def assertTrue(self, test_result):
        print('TEST RESULT ::: ', test_result)
        if not test_result:
            print('-- TEST CASE FAILED --')
            print("-- REASON:-", self.fail_reason)
            url = self.dut.options.get('teams_webhook_url', None)
            data = {
                'summary': 'Test Case Report',
                'sections': [
                    {
                        'title': 'Test-Case details:',
                        'facts': [
                            {
                                'name': 'Test Name:',
                                'value': self.test_name
                            },
                            {
                                'name': 'Test Result:',
                                'value': '<b>Fail</b>'
                            },
                        ]
                    }
                ]
            }
            response = requests.post(url, data=json.dumps(data))
        else:
            with open("pass_logs.txt", "a") as log:
                date_now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                log.write('\n--------------------------------\n\n')
                log.write('%s. PASS CASE LOG-DATE : %s\nTEST CASE : %s\n' % (self.test_number, date_now_str, self.test_name))
                traceback.print_exc(file=log)
            print('TEST CASE NAME ::: ', self.test_name)
            print('-- TEST CASE PASSED -- PASS NUMBER:: ', self.test_number)
        
        is_data_send_to_elastic_flag = self.dut.options.get('is_data_send_to_elastic', None)
        if is_data_send_to_elastic_flag == True:
            self.send_tc_data_to_elk()
        super().assertTrue(test_result)

    def get_end_time(self):
        end_time = None
        for timestamp in self.dut.timestamps:
            if timestamp.get('test_end_time') is not None:
                end_time = timestamp.get('test_end_time')
                break
        if end_time is None:
            end_time = time.time()
            self.dut.timestamps.append({'test_end_time': time.time()})

        return end_time

    def send_tc_data_to_elk(self):
        system_utility = SystemUtility()
 
        data = {
            'name': self.test_name,
            'durations': self.dut.durations,
            'timestamps': self.dut.timestamps,
            'pass_status': self.test_result,
            'setup_box_acct_no': '',
            'setup_box_device_code': '',
            'setup_box_id': '', 
            'video_url': '',
            'pass_percentage': 1 if self.test_result == True else 0,
            'type': self.tc_type,
            'device_type': self.get_device_name(),
            'host_name': system_utility.host_name,
            'user_name': system_utility.user_name,
            'completion_time': str(self.get_end_time()),
            'fail_reason': self.fail_reason if self.fail_reason is not None else "",
            'created': datetime.now()
        }
  
        const_elk = ConstElk()
        elk = ELKBell(index_name=const_elk.IDX_BELL_TEST_CASES, doc_type=const_elk.DOC_TEST_DETAILS, elk_mapping=ELKBellDocMapping())
        elk.insert_data(data=data)

    @staticmethod
    def memory_check():
        print('IN MEMORY CHECK')
        with open('/proc/meminfo') as file:
            for line in file:
                print(line)
                if 'MemFree' in line:
                    free_mem_in_kb = line.split()[1]
                    print(free_mem_in_kb)
                    if int(free_mem_in_kb) < 200000:
                        print('EXPLICIT APPLICATION EXIT')
                        exit()
                    break

    @staticmethod
    def merge_audio_video(video_file_path, timestamps):
        if TestCaseModule.audio_file_path is not None:
            for timestamp in timestamps:
                if timestamp.get('test_start_time') is not None:
                    start_time = timestamp.get('test_start_time')
                elif timestamp.get('audio_cmd_play_time') is not None:
                    audio_cmd_timestamp = timestamp.get('audio_cmd_play_time')
                    audio_launch_time = round(audio_cmd_timestamp - start_time, 2)
                    break
            video_1 = MGVideo("./%s" % video_file_path)
            print('VIDEO :: ', video_1)
            audio_1 = MGAudio(TestCaseModule.audio_file_path, audio_launch_time)
            print('AUOI : ', audio_1)
            merg_audio_video = MergeAudioVideo(video_file=video_1, audio_files=[audio_1])
            new_file_name = merg_audio_video.merge()[1]
            if os.path.exists(new_file_name):
                if os.path.exists(video_file_path):
                    os.remove(video_file_path)
                    os.rename(new_file_name,video_file_path)
