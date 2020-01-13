"""
@ Stefanie Fiedler 2019
@ Alexander Teubert 2019
Version vom 09.01.2019

for Hochschule Anhalt, University of Applied Sciences
in coorperation with axxeo GmbH
"""

from EasyModbusSilaaCooling.modbusClient import ModbusClient as MBC
from HeliosEthernetSilaaCooling.Helios_HexConverter import str2duohex, duohex2str
from HeliosEthernetSilaaCooling.Helios_Errors import errortable, warningtable, infotable
from re import compile, search, group
from logging import debug, info, warning, error, critical, basicConfig, DEBUG, INFO, WARNING, ERROR, CRITICAL

"""
set-up the logger module by using the basicConfig - method
level - level of severity, on which the logger starts writing output, might be changed between:
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL
filename - name of the logfile, ending on .log
filemode - possible modes:
    w - write, overwrites existing file
    a - append, standard mode, appends on existing log file
format - sets the standard format for the logged string
"""

basicConfig(
    level=DEBUG,
    filename="Helios_Ethernet.log",
    filemode="w",
    format="%(asctime())s: %(name)s - %(levelname)s - %(message)s"
)

class COM():
    """
    Implementation of a Modbus TCP/IP-Client to access read and writeable attributes of a Helios KWL Device
    """

    def __init__(self, ip = "192.168.1.199", port = 502):

        if isinstance(ip, str): self.__ip = ip
        else: error("The ip-adress should be given as a string!")

        if isinstance(port, int): self.__port = port
        else: error("Please check your input! The tcp-port should be given as an integer!")

        self.__timeout = 2
        self.__device_id = 180

        """
        setup for the Modbus-Connection
        """

        self.modbusclient = MBC(self.__ip, self.__port)
        self.modbusclient.unitidentifier = self.__device_id
        self.modbusclient.timeout = self.__timeout
        self.modbusclient.connect()

        info("Connecting to the client for the first time!")
        debug("Setting date-format to dd.mm.yyyy and operation-mode to automatic to test the connection")

        """
        set date-format to dd.mm.yyyy
        """

        self.modbusclient.write_multiple_registers(0, str2duohex("v00052=mm.dd.yyyy"))

        """
        set mode to automatic
        """

        self.modbusclient.write_multiple_registers(0, str2duohex("v00101=0"))

        #self.modbusclient.close()
        info("Modbus client succesfully running!")

    def __del__(self):
        self.modbusclient.close()
        info("Modbus client succesfully stopped!")

    def read_temp(self):
        """
        reads several temperature values from slave and returns them as a list of float-values
        """

        """
        read outdoor-air-temperature (variable v00104) / Aussenluft
        """
        debug("Reads the sensor for the outdoor-air-temperature...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00104"))
        outTemp = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        """
        read supplied-air-temperature (variable v00105) / Zuluft
        """
        debug("Reads the sensor for the supplied-air-temperature...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00105"))
        suppTemp = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        """
        read exhaust-air-temperature (variable v00106) / Fortluft
        """
        debug("Reads the sensor for the exhaust-air-temperature...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00106"))
        exhaustTemp = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        """
        read extract-air-temperature (variable v00107) / Abluft
        """
        debug("Reads the sensor for the extract-air-temperature...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00107"))
        extractTemp = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        info("Successfully read all temperature sensors!")
        return float(outTemp), float(suppTemp), float(exhaustTemp), float(extractTemp)

    def get_date(self):
        """
        outputs the slaves time and date
        """

        """
        read system-clock (variable v00005)
        """
        debug("Reads the system-clock...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00005"))
        time = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        """
        read system-date (variable v00004)
        """
        debug("Reads the system-date...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00004"))
        date = duohex2str(self.modbusclient.read_holdingregisters(0,9))[7:]

        info("Successfully read time and date!")
        return time, date

    def set_date(self, time, date):
        """
        sets the slave time and date
        """

        """
        sets the slave date / v00004
        by using a regular expression, we check if the date-format is correct
        """

        debug("Checking if the given date matches the pattern...")
        if (compile(r"^\d\d/\d\d/\d\d\d\d$").search(date)) & (date[:2]=<31) & (date[3:5]=<12):
            debug("Setting the slaves date...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00004="+date))
            info("Successfully set the date!")

        else: error("Please check your date format! It should be dd.mm.yyyy")

        """
        sets the slave time / v00005
        by using a regular expression, we check if the time-format is correct
        """
        debug("Checking if the given date matches the pattern...")
        if (compile(r"^\d\d:\d\d:\d\d$").search(time)) & (time[:2]=<24) & (time[3:5]=<60) & (time[6:]=<60):
            debug("Setting the slaves time...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00005="+time))
            info("Successfully set the time!")

        else: error("Please check your time format! It should be hh:mm:ss")

    def read_management_state(self):
        """
        outputs the state of the humidity, carbon-dioxide and voc-management
        """

        """
        read humidity management-state (variable v00033)
        """
        debug("Reading the humidity management state...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00033") )
        humidity_state = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]

        """
        read carbon-dioxide management-state (variable v00037)
        """
        debug("Reading the carbon-dioxide management state...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00037") )
        carbon_state = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]

        """
        read voc management-state (variable v00040)
        """
        debug("Reading the voc management state...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00040") )
        voc_state = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]

        info("Successfully read all management states from the slave!")
        return int(humidity_state), int(carbon_state), int(voc_state)

    def read_management_opt(self):
        """
        outputs the defined optimum value for the humidity, carbon-dioxide and voc-management
        """

        """
        read optimum humidity level in percent (variable v00034)
        """
        debug("Reading the optimum humidity level in percent...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00034"))
        humidity_val = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]

        """
        read optimum carbon-dioxide concentration in ppm (variable v00038)
        """
        debug("Reading the optimum carbon-dioxide concentration in ppm...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00038") )
        carbon_val = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]

        """
        read optimum voc concentration in ppm (variable v00041)
        """
        debug("Reading the optimum voc concentration in ppm...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00041") )
        voc_val = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]

        info("Successfully set all optimal values for the air quality-sensors!")
        return int(humidity_val), int(carbon_val), int(voc_val)

    def write_management_state(self, state_humidity, state_carbon, state_voc):
        """
        writes the state of the humidity, carbon-dioxide and voc-management
        """
        debug("Checking legimaticy of the input values...")
        if (isinstance(state_humidity, int) & isinstance(state_carbon, int) & isinstance(state_voc, int)):
            """
            write humidity management-state (variable v00033)
            """
            debug("Setting the state on the humidity management...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00033="+ str(state_humidity)) )

            """
            write carbon-dioxide management-state (variable v00037)
            """
            debug("Setting the state on the carbon-dioxide management...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00037="+ str(state_carbon)) )

            """
            write voc management-state (variable v00040)
            """
            debug("Setting the state on the voc management...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00040="+ str(state_voc)) )

            info("Successfully wrote all optimal values to the slave")

        else: error("Please check the validicity of your input values!")

    def write_management_opt(self, opt_humidity, opt_carbon, opt_voc):
        """
        sets the optimum value for the humidity, carbon-dioxide and voc-management
        """
        debug("Checking legimaticy of the input values...")
        if (isinstance(opt_humidity, int) & isinstance(opt_carbon, int) & isinstance(opt_voc, int)
            & 20 =< opt_humidity =< 80 & 300 <= opt_carbon <= 2000 & 300 <= opt_voc <= 2000):
            """
            set the optimum percentage of air-humidity /  between 20% and 80% (variable v00034)
            """
            debug("Setting the optimal level of air-humidity...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00034="+ str(opt_humidity)) )

            """
            set the optimum concentration of carbon-dioxide / between 300 and 2000 ppm (variable v00038)
            """
            debug("Setting the optimal concentration of carbon-dioxide...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00038="+ str(opt_carbon)) )

            """
            set the optimum concentration of voc / between 300 and 2000 ppm (variable v00041)
            """
            debug("Setting the optimal concetration of voc...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00041="+ str(opt_voc)) )

            info("Successfully wrote all optimal values to the slave")

        else: error("Please check the validicity of your input values!")


    def state_preheater(self, *preheater):
        """
        sets/ reads the state of the preheater / 0 = off, 1 = on (variable v00024)
        """
        debug("Checking input to determine, if to read or set the state of the slaves preheater...")
        try:
            if isinstance(preheater[0], int) & (preheater[0] in (0,1)):
                debug("Setting state of preheater...")
                self.modbusclient.write_multiple_registers(0, str2duohex("v00024="+ str(preheater[0])) )
                info("Successfully wrote state to the preheater!")

        except IndexError:
            debug("Reading state of preheater...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00024"))
            state = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]
            info("Successfully read state of the preheater!")
            return state

    def read_fan_level(self):
        """
        read fan level in percents (variable v00103)
        """
        debug("Reading fan level in percents...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00103") )
        level = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]
        info("Successfully read fan level in percents!")
        return int(level)

    def read_fan_rpm(self):
        """
        read the revolutions per minute for the supply fan (variable v00348)
        """
        debug("Reading supply fans rpm...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00348") )
        supply = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]

        """
        read the revolutions per minute for the extraction fan (variable v00349)
        """
        debug("Reading extraction fans rpm...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00349") )
        extraction = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]

        info("Successfully read the rpm of extraction and suppply fan!")
        return int(supply), int(extraction)

    def write_fan_stage(self, supply, extraction):
        """
        sets the state for the supply and  extraction fans / stages 1-4
        """
        debug("Checking the input values for the supply and extraction fans stages...")
        if (isinstance(supply, int)) & (isinstance(extraction, int)) & (extraction in (1,2,3,4)) & (supply in (1,2,3,4)):
            """
            sets the stage for the supply fan (variable v01050)
            """
            debug("Setting the supply fans stage...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v01050="+ str(supply)) )
            info("Successfully set the supply fans stage!")

            """
            sets the stage for the extraction fan (variable v01051)
            """
            debug("Setting the extraction fans stage...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v01051="+ str(extraction)) )
            info("Successfully set the extraction fans stage!")

    def read_fan_stage(self):
        """
        read supply fan stage / 1-4 (variable v01050)
        """
        self.modbusclient.write_multiple_registers(0, str2duohex("v01050") )
        supply = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]

        """
        read extraction fan stage / 1-4 (variable v01051)
        """
        self.modbusclient.write_multiple_registers(0, str2duohex("v01051") )
        extraction = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]
        return int(supply), int(extraction)

    def get_state(self):
        """
        receive error messages from the Helios Slave
        """

        string = ""

        """
        read errors as integer values / v01123
        """
        debug("Requesting error codes from the slave...")
        try:
            self.modbusclient.write_multiple_registers(0, str2duohex("v01123") )
            string = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]
            info("Successfully read error message from the slave!")
            return errortable(int(string)), "error"

        except KeyError:
            """
            read warnings as integer values / v01124
            """
            debug("Requesting warning codes from the slave...")
            try:
                self.modbusclient.write_multiple_registers(0, str2duohex("v01124") )
                string = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]
                info("Successfully read warnings from the slave!")
                return warningtable(int(string)), "warning"

            except KeyError:
                """
                read informations on the state of the KWL EC 170 W / v01125
                """
                debug("Requesting information codes on the state of the slave...")
                try:
                    self.modbusclient.write_multiple_registers(0, str2duohex("v01125") )
                    string = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]
                    info("Successfully informations from the slave!")
                    return infotable(int(string)), "state"

                except KeyError:
                    return "Keine Fehler, Warnungen oder Infos vorhanden!"

    def clear_state(self):
        """
        clears the memory of the error register
        """
        debug("Clearing the error register...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v02015=1") )
        info("Successfully cleared the memory of the error register!")
