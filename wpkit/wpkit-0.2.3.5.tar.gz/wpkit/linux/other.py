def get_local_ip():
    import socket
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
# print(ip)