import yaml
import requests
import jwt
import json
import uuid
import os,sys, traceback
import datetime
import pickledb


def openFile(fileName):
    data = ""
    with open (fileName, "r") as f:
        data = f.read()
    return data

def createToken(thingId, payload, privateKey):
    return jwt.encode(payload, privateKey, algorithm='RS256', headers={'kid': thingId}).decode('utf-8')
    
class FlashlexSDK(object):

    def __init__(self, config):
        if(type(config) == 'str'):
            self._config = self.loadConfig(config)
        else:
            self._config = config
       
    def getConfig(self):
        return self._config
    
    def setConfig(self, config):
        self._config = config
    
    def loadConfig(self, configFile):
        cfg = None
        with open(configFile, 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return cfg

    def getSubscribedMessages(self, count=-1, sortMessages=True, reverse=False):
        subscriptionDataPath = "{0}/{1}".format(
            self._config["flashlex"]["app"]["db"]["dataPath"], 
            self._config["flashlex"]["app"]["db"]["subscriptionData"])

        subscriptionDb = pickledb.load(subscriptionDataPath, False, sig=False)
        listKeys = subscriptionDb.getall()
        messages_all = []
        for key in listKeys:
            messages_all.append(subscriptionDb.get(key))

        print(messages_all)
        if(sortMessages):
            sorted(messages_all, key=lambda message: message["timestamp"], reverse=reverse)
        if(count>0):
            return messages_all[:count]
        else:     
            return messages_all
  
    def removeMessageFromStore(self, message):
        subscriptionDataPath = "{0}/{1}".format(
            self._config["flashlex"]["app"]["db"]["dataPath"], 
            self._config["flashlex"]["app"]["db"]["subscriptionData"])

        if 'pk' in message:
            subscriptionDb = pickledb.load(subscriptionDataPath, False, sig=False)
            subscriptionDb.rem(message['pk'])
            subscriptionDb.dump()
        else:
            raise KeyError('pk key is required')

    def setMessageToStore(self, message):
        subscriptionDataPath = "{0}/{1}".format(
            self._config["flashlex"]["app"]["db"]["dataPath"], 
            self._config["flashlex"]["app"]["db"]["subscriptionData"])

        #should add pk if missing
        if 'pk' not in message:
            message["pk"] = str(uuid.uuid4()).replace("-","")[:12]

        subscriptionDb = pickledb.load(subscriptionDataPath, False, sig=False)
        subscriptionDb.set(message['pk'], message)
        subscriptionDb.dump()


    
    def collectMessage(self, message):
        """
        uses the certificate to generate an asymetric token
        that can be verified by the public key at flashlex,
        messages cannot be collected unless the key is 
        verified.
        """
        thingId=self._config["flashlex"]["thing"]["id"]
        print("collecting message from thing: {0}".format(thingId))
        print(self._config["flashlex"]["thing"]["keys"]["path"])
        privateKey = openFile("{0}/{1}".format(
            self._config["flashlex"]["thing"]["keys"]["path"], 
            self._config["flashlex"]["thing"]["keys"]["privateKey"]))

        
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=360),
            'nbf': datetime.datetime.utcnow() - datetime.timedelta(seconds=360),
            'iss': 'urn:thing:{0}'.format(thingId),
            'aud': 'urn:flashlex:{0}'.format(thingId)
        }

        jwt = createToken(thingId, payload, privateKey)
        
        url = "{0}/{1}/v1/things/{2}/collect".format(
                self._config["flashlex"]["app"]['api']["endpoint"],
                self._config["flashlex"]["app"]['api']["env"],
                self._config["flashlex"]["thing"]["id"])
        # payload = {'key1': 'value1', 'key2': 'value2'}        
        headers={"Authorization":"Bearer {0}".format(jwt), 'Content-Type': 'application/json'}
        print(url, message, headers)

        try:
            r = requests.post(url, 
                data=json.dumps(message), 
                headers=headers)
            print(r.text)    
            return r.status_code
        except:
            print("there was a problem.")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)

            return 500
        


