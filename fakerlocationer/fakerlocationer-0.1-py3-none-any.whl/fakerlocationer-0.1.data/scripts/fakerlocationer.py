class FakerLocationer(object):
    def __init__(self, driver):
        self.driver = driver

    def returnDriver(self):
        return self.driver

    def setLocation(self, latitude, longitude):
        self.driver.execute_script(
            "navigator.geolocation.getCurrentPosition = (s, e) => {s({coords: {latitude: " + str(latitude) + ",longitude: " + str(longitude) + "}});};")
