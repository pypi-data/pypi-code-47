import socket

def hello():
        hostname = socket.gethostname()
        return("Hello "+hostname)
