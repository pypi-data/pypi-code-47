from wpkit.services.CloudOS import start_server
from wpkit.linux import clean_port,get_local_ip
port1=80
port2=8002
clean_port(port1)
clean_port(port2)
start_server(__name__,host=get_local_ip() or "127.0.0.1",port1=port1,port2=port2)
