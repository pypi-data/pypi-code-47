import requests
class LegLight:

    def __init__(self, name, address, port, server):
        self.name = name
        self.address = address
        self.port = port
        self.server = server
        res = requests.get("http://{}:{}/elgato/accessory-info".format(address,port))
        details = res.json()
        self.productName = details['productName']
        self.hardwareBoardType = details['hardwareBoardType']
        self.firmwareBuildNumber = details['firmwareBuildNumber']
        self.firmwareVersion = details['firmwareVersion']
        self.serialNumber = details['serialNumber']
        self.display = details['displayName']

    def __repr__(self):
        return "Elgato Light {} @ {}:{}".format(self.serialNumber, self.address, self.port)

    def on(self):
        print("turning on " + self.display)
        data = '{"numberOfLights":1,"lights":[{"on":1}]}'
        res = requests.put('http://{}:{}/elgato/lights'.format(self.address, self.port), data=data)

    def off(self):
        print("turning off " + self.display)
        data = '{"numberOfLights":1,"lights":[{"on":0}]}'
        res = requests.put('http://{}:{}/elgato/lights'.format(self.address, self.port), data=data)

    def brightness(self, level):
        print("setting brightness {} on {}".format(level, self.display))
        if 0 <= level <= 100:
            data = '{"numberOfLights":1,"lights":[{"brightness":'+'{}'.format(level)+'}]}'
            res = requests.put('http://{}:{}/elgato/lights'.format(self.address, self.port), data=data)
            #print(res.text)
        else:
            print("INVALID BRIGHTNESS LEVEL - Must be 0-100")

    def color(self, temp):
        print("setting color {}k on {}".format(temp, self.display))
        if 3000 <= temp <= 7000:
            # Confused? The lights accept a value of 332 (3000k) to 143 (7000k), turns out to be
            # 1,000,000 / the temperature. I assume it is to do with light be logarithmic?
            # https://docs.google.com/spreadsheets/d/1JcL3pD-Vivhq_89TfZArhED-eGTaCJXNRpu5A3wp2Tw/
            transcode = 1000000 / temp
            data = '{"numberOfLights":1,"lights":[{"temperature":'+'{}'.format(transcode)+'}]}'
            res = requests.put('http://{}:{}/elgato/lights'.format(self.address, self.port), data=data)
            #print(res.text)
        else:
            print("INVALID COLOR TEMP - Must be 3000-7000")