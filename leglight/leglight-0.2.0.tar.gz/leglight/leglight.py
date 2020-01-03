import requests
import logging

class LegLight:

    def __init__(self, address, port, name="", server=""):
        # Init info from discovery, or user controlled
        self.address = address
        self.port = port
        
        # We don't current use name or server, so can be null
        self.name = name
        self.server = server

        # On init, go talk to the light and get the full product info
        res = requests.get("http://{}:{}/elgato/accessory-info".format(address,port))
        details = res.json()
        self.productName = details['productName']
        self.hardwareBoardType = details['hardwareBoardType']
        self.firmwareBuildNumber = details['firmwareBuildNumber']
        self.firmwareVersion = details['firmwareVersion']
        self.serialNumber = details['serialNumber']
        self.display = details['displayName']

        # On init, we'll also go get the current status of the light
        self.isOn = None
        self.isBrightness = None
        self.isTemperature = None
        self.info()

    def __repr__(self):
        return "Elgato Light {} @ {}:{}".format(self.serialNumber, self.address, self.port)

    def on(self):
        """ Turns the light on """
        logging.debug("turning on " + self.display)
        data = '{"numberOfLights":1,"lights":[{"on":1}]}'
        res = requests.put('http://{}:{}/elgato/lights'.format(self.address, self.port), data=data)
        self.isOn = res.json()['lights'][0]['on']

    def off(self):
        """ Turns the light off """
        logging.debug("turning off " + self.display)
        data = '{"numberOfLights":1,"lights":[{"on":0}]}'
        res = requests.put('http://{}:{}/elgato/lights'.format(self.address, self.port), data=data)
        self.isOn = res.json()['lights'][0]['on']

    def brightness(self, level):
        """ Sets the light to a specific brightness (0-100) level """
        logging.debug("setting brightness {} on {}".format(level, self.display))
        if 0 <= level <= 100:
            data = '{"numberOfLights":1,"lights":[{"brightness":'+'{}'.format(level)+'}]}'
            res = requests.put('http://{}:{}/elgato/lights'.format(self.address, self.port), data=data)
            self.isBrightness = res.json()['lights'][0]['brightness']
        else:
            logging.warn("INVALID BRIGHTNESS LEVEL - Must be 0-100")

    def incBrightness(self, amount):
        """ Increases the light brightness by a set amount """
        self.info()
        self.brightness(self.isBrightness + amount)

    def decBrightness(self, amount):
        """ Decreases the light brightness by a set amount """
        self.info()
        self.brightness(self.isBrightness - amount)

    def color(self, temp):
        """ Sets the light to a specific color temperature (2900-7000k) """
        logging.debug("setting color {}k on {}".format(temp, self.display))
        if 2900 <= temp <= 7000:
            data = '{"numberOfLights":1,"lights":[{"temperature":'+'{}'.format(self.colorFit(temp))+'}]}'
            res = requests.put('http://{}:{}/elgato/lights'.format(self.address, self.port), data=data)
            self.isTemperature = self.postFit(res.json()['lights'][0]['temperature'])
        else:
            logging.warn("INVALID COLOR TEMP - Must be 2900-7000")

    def incColor(self, amount):
        """ Increases the lights color temperature by a set amount """
        self.info()
        self.color(self.isTemperature + amount)

    def decColor(self, amount):
        """ Decreases the lights color temperature by a set amount """
        self.info()
        self.color(self.isTemperature - amount)

    def info(self):
        """ Gets the current light status. """
        logging.debug("getting info for " + self.display)
        res = requests.get('http://{}:{}/elgato/lights'.format(self.address, self.port))
        status = res.json()['lights'][0]
        self.isOn = status['on']
        self.isBrightness = status['brightness']
        self.isTemperature = self.postFit(status['temperature'])
        return({'on':self.isOn,'brightness':self.isBrightness,'temperature':self.isTemperature})

    def colorFit(self, val):
        """Take a color temp (in K) and convert it to the format the Elgato Light wants"""
        return round(987007 * val**-0.999, 0)

    def postFit(self, val):
        """Take the int that the Elgato Light returns and convert it roughly back to color temp (in K)"""
        return round(1000000*val**-1, -2)

    ### Firmware section is for documentational purposes. Not in anyway near ready for use.
    # def updateFirmware(self, file):
        # PUT /elgato/firmware-update/prepare -- Data: {"size":785207}
        # PUT /elgato/firmware-update/data?offset=0
        # PUT /elgato/firmware-update/data?offset=4096
        # PUT /elgato/firmware-update/data?offset=8192
        # ...
        # POST /elgato/firmware-update/execute
