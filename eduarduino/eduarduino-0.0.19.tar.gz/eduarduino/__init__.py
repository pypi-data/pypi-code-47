import pyfirmata, traceback
from serial import SerialException

SALIDA_DIGITAL = [2,4,7,8,12]
SALIDA_PWM = [3,5,6,9,10,11]
ENTRADA_ANALOGICA = [0,1,2,3,4,5]

__pines_salida = {}
__pines_entrada = {}
__placa = {}


def espera(segs):
    
    if not isinstance(segs, int) and not isinstance(segs, float):
        traceback.print_last()
        raise Exception("espera("+str(segs)+"): segs debe ser entero o de coma flotante")
        
    if segs<0 or segs>10:
        traceback.print_last()
        raise Exception("espera("+str(segs)+"): segs debe estar entre 0 y 10")
    
    __placa[0].pass_time(segs)


def escribe(pin, valor):
    
    if not isinstance(pin, int):
        traceback.print_last()
        raise Exception("escribe("+str(pin)+","+str(valor)+"): pin debe ser un entero")

    if not isinstance(valor, int) and not isinstance(valor, float):
        traceback.print_last()
        raise Exception("escribe("+str(pin)+","+str(valor)+"): valor debe ser entero o de coma flotante")
    
    if pin not in SALIDA_DIGITAL and pin not in SALIDA_PWM:
        traceback.print_last()
        raise Exception("escribe("+str(pin)+","+str(valor)+"): Pin de salida inválido")
    
    elif valor<0 or valor>1: 
        traceback.print_last()
        raise Exception("escribe("+str(pin)+","+str(valor)+"): El valor debe estar entre 0 y 1")
    
    elif valor!=0 and valor!=1 and pin in SALIDA_DIGITAL: 
        traceback.print_last()
        raise Exception("escribe("+str(pin)+","+str(valor)+"): Valor analógico en la salida digital")
    
    else:    
        __pines_salida[pin].write(valor)



def lee(pin):

    if not isinstance(pin, int):
        traceback.print_last()
        raise Exception("lee("+str(pin)+"): pin debe ser entero o de coma flotante")
    
    if pin not in ENTRADA_ANALOGICA:
        traceback.print_last()
        raise Exception("lee("+str(pin)+"): Pin de entrada inválido")
    
    
    return __pines_entrada[pin].read()

def init(setup, loop):

    conectado = False
    num_puerto = 0
    while not conectado and num_puerto<=10:
        try:
            __placa[0] = pyfirmata.Arduino("/dev/ttyUSB"+str(num_puerto))
            conectado = True
        except SerialException:
            num_puerto += 1
 
    if num_puerto==11:
        traceback.print_last()
        raise Exception("int("+str(setup)+","+str(loop)+"): puerto no encontrado")
    else:
        print("Conectado en /dev/ttyUSB"+str(num_puerto))
   
    _init(setup,loop)




def init_p(setup, loop, puerto):
    
    try:
        __placa[0] = pyfirmata.Arduino(puerto)
        print(puerto)
    except SerialException:
        raise Exception("int("+str(setup)+","+str(loop)+"): puerto no encontrado")
    
    _init(setup,loop)




def _init(setup, loop):
    
    if not callable(setup) or not callable(loop):
        traceback.print_last()
        raise Exception("int("+str(setup)+","+str(loop)+"): setup y loop deben ser funciones")
 
    for i in SALIDA_DIGITAL:
        __pines_salida[i] = __placa[0].get_pin("d:"+str(i)+":o")

    for i in SALIDA_PWM:
        __pines_salida[i] = __placa[0].get_pin("d:"+str(i)+":p")
    
    
    __placa[1] = pyfirmata.util.Iterator(__placa[0])
    __placa[1].start()
    
    for i in ENTRADA_ANALOGICA:
        __placa[0].analog[i].enable_reporting()
        __pines_entrada[i] = __placa[0].get_pin("a:"+str(i)+":i")

    __placa[0].pass_time(1) #Dejar 1 seg entre iterator y posible lectura    
    
    try:
        setup()
        while True:
            loop()
            
    except (KeyboardInterrupt, SystemExit):
        print("Terminando")
        #__placa[0].exit()