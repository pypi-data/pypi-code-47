import unittest
import pathlib
import os, sys, traceback
import yaml
import pickledb

from os.path import dirname, abspath
from shutil import copyfile
from flashlexiot.backend.thread import BasicPubsubThread, ExpireMessagesThread
from flashlexiot.sdk import FlashlexSDK

def loadConfig(configFile):
    cfg = None
    with open(configFile, 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return cfg

class TestFlashlexSDK(unittest.TestCase):

    def setUp(self):
        fn = pathlib.Path(__file__).parent / 'test-config.yml'

         #get defaults for data and keys
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config = loadConfig("{0}/test-config.yml".format(dir_path))

        self.sdk = FlashlexSDK(config)

        config = self.sdk.getConfig()
        config["flashlex"]["app"]["db"]["dataPath"] = pathlib.Path(__file__).parent 
        config["flashlex"]["app"]["db"]["subscriptionData"] = 'data/subscription2.db'
        self.sdk.setConfig(config)

        message1 = {
            "pk": "b300d03c-7bd4-4110-9489-5ef59abb1981",
            "timestamp": 1553978975.5232847,
            "datetime": "2019-03-30 13:49:35",
            "message": {
                "topic": "pubsub/foobar30",
                "payload": {
                    "message": "Sending a basic message...",
                    "sequence": 151
                },
                "pos": 1,
                "retain": 0,
                "mid": 1
            }
        }
        
        message2 = {
            "pk": "a300d03c-7bd4-4110-9489-5ef59abb1981",
            "timestamp": 1553978976.5232847,
            "datetime": "2019-03-30 13:49:35",
            "message": {
                "topic": "pubsub/foobar30",
                "payload": {
                    "message": "Sending a basic message...",
                    "sequence": 151
                },
                "pos": 1,
                "retain": 0,
                "mid": 1
            }
        }

        subscriptionDataPath = "{0}/{1}".format(
            config["flashlex"]["app"]["db"]["dataPath"], 
            config["flashlex"]["app"]["db"]["subscriptionData"])

        subscriptionDb = pickledb.load(subscriptionDataPath, False)
        subscriptionDb.set(message1['pk'], message1)
        subscriptionDb.set(message2['pk'], message2)
        subscriptionDb.dump()

    def test_load_config(self):
        self.assertEqual('testThing1', self.sdk.getConfig()["flashlex"]["thing"]["name"])

    def test_get_messages(self):
        messages = self.sdk.getSubscribedMessages()
        self.assertEqual(2,len(messages))

    def test_remove_message(self):
        config = self.sdk.getConfig()
        messages = self.sdk.getSubscribedMessages()
        self.sdk.removeMessageFromStore(messages[0])
        messages = self.sdk.getSubscribedMessages()
        self.assertEqual(1,len(messages))

    def tearDown(self):
        print('tear down')

        config = self.sdk.getConfig()
        subscriptionDataPath = "{0}/{1}".format(
            config["flashlex"]["app"]["db"]["dataPath"], 
            config["flashlex"]["app"]["db"]["subscriptionData"])

        os.remove(subscriptionDataPath)



if __name__ == '__main__':
    unittest.main()
