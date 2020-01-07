import socket
import getpass

class SystemUtility():
    
    @property
    def host_name(self):
        return socket.gethostname()

    @property
    def user_name(self):
        return getpass.getuser()
