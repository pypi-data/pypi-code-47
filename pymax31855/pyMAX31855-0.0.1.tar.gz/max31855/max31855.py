#file: max31855.py
#author: Menschel (C) 2020
#purpose: interface max31855 IC with k-type thermistor from python3
#Note: testing with adafruit breakout board, the python module that Adafruit offers is apparently broken
 

#the IC is SPI read only, so we need spidev
import spidev

from max31855.k_type_lin import voltage2temp,temp2voltage


#we use ctypes struct to represent the input data from spi
from ctypes import c_int32,c_uint32,BigEndianStructure

class max31855msg(BigEndianStructure):
    
    _fields_ = [
                ('t_thermocouple',c_int32,14),#junction temperature in 0.25 deg C steps
                ('reserved2',c_uint32,1),
                ('fault',c_uint32,1),#OR-flag of scv,scg,oc
                ('t_referencejunction',c_int32,12),#junction temperature in 0.0625 deg C steps
                ('reserved',c_uint32,1),
                ('scv',c_uint32,1),#short-cut to supply voltage
                ('scg',c_uint32,1),#short-cut to ground 
                ('oc',c_uint32,1),#open-circut
                ]
    

def interpret_msg(data):
    msg = max31855msg.from_buffer_copy(data)
    
    fault = None
    t_tc = None
    t_rj = None
    t_tc_lin = None
    u_tc = None
    u_rj = None
    
    if msg.fault > 0:
        if msg.scv > 0:
            fault = "Short to VCC"
        elif msg.scg > 0:
            fault = "Short to GND"
        elif msg.oc > 0:
            fault = "Open Circuit"
        else:
            print(" ".join(["{0:02X}".format(d) for d in data]))
            print("fault {0}\n scv {1}\n scg {2}\n oc {3}\n ".format(msg.fault,msg.scv,msg.scg,msg.oc))
            raise NotImplementedError("Received general fault from device but none of the specific faults is set")
    
    if fault is None:
        #calculate the thermocouple temperature
        t_tc = msg.t_thermocouple*0.25
        #calculate the reference junction temperature
        t_rj = msg.t_referencejunction*0.0625
        
        
        #Extract of Datasheet, calculate the thermocouple voltage
        #V OUT = (41.276μV/°C) x (T R - T AMB )
        fac_u_t = 0.041276#mV per degC            
        u_tc =  (t_tc - t_rj) * fac_u_t
        
        
        #calculate the reference junction voltage
        u_rj = temp2voltage(t_rj)
        
        
        #linearize the voltage sum of reference junction and thermocouple into a temperature
        
        t_tc_lin = voltage2temp(u_rj + u_tc)
        
    ret = {"t_tc":t_tc,
           "t_rj":t_rj,
           "u_tc":u_tc,
           "u_rj":u_rj,
           "t_tc_lin":t_tc_lin,
           "fault":fault,
           #"rawdata":data,#for debug
           "hexdata":data.hex(),#for better reading while debugging
          }
    return ret

class max31855:


    def __init__(self,bus,device):
        self.bus = bus
        self.device = device
        self.spi = spidev.SpiDev()
        
    def read_value(self):
        """read a datagram from max31855 and return it as a usable dictionary"""
        #open the spi device
        self.spi.open(self.bus,self.device)
        self.spi.max_speed_hz=2000000
        self.spi.mode=0
        
        #read 4 bytes as the size of a message is 32bits
        data = bytes(self.spi.readbytes(4))
        
        #close the spi device
        self.spi.close()
        
        return interpret_msg(data=data)

        
    

    


if __name__ == '__main__':
    from pprint import pprint as pp
    import time
    obj_ = max31855(bus=0,device=0)
    try:
        while True:
            pp(obj_.read_value())
            time.sleep(5)
    except KeyboardInterrupt:
        pass
