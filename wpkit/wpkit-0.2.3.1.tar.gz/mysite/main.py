from wpkit.services.CloudOS import start_server
from wpkit.linux.tools import clean_port
port1=80
port2=8002
clean_port(port1)
clean_port(port2)
start_server(__name__,host="0.0.0.0",port1=port1,port2=port2)
