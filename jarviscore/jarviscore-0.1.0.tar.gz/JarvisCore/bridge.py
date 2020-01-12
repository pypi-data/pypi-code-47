from .channel import Channel
from .socket import SendSocket, ReadSocket
from .command import Command, CommandResponse
from .message import RawMessage
from time import sleep  

class Bridge(object):
    """description of class"""
    send_socket: SendSocket
    read_socket: ReadSocket
    channels: list
    active: bool
    


    def __init__(self, client):
        self.client = client
        self.active = True
        self.__init_sockets()
        self.__init_channels()
        pass


    def __init_sockets(self):
        self.read_socket = ReadSocket(self.client.nick, self.client.token)
        self.send_socket = SendSocket(self.client.nick, self.client.token)
        pass


    def __init_channels(self):
        self.channels = []
        proto_channel = Channel(name="proto")
        for chn in self.client.channels:
            self.channels.append(proto_channel.propogate(self.send_socket, chn))

    def __get_channel(self, name: str):
        for channel in self.channels:
            if channel.name == name:
                return channel
        

    def run(self):
        self.read_socket.activate(self.channels)
        self.send_socket.activate(self.channels)
        self.read_socket.start()
        self.send_socket.start()
        try:
            while self.active:
                sleep(0.0001)
        except KeyboardInterrupt:            
            self.read_socket.close()
            self.send_socket.close()


    def check_messages(self):
        pass
        



    def add_channel(self, channel: str):
        chn = Channel()
        self.channels.append(chn.propogate(self.send_socket, chn))
        self.send_socket.connect_to_channel(channel)
        self.read_socket.connect_to_channel(channel)
    
    def remove_channel(self, channel: str):
        for chn in self.channels:
            if chn.name == channel:
                self.channels.remove(chn)
        self.send_socket.disconnect_from_channel(channel)
        self.read_socket.disconnect_from_channel(channel)

    def leave_channel(self, channel: str):
        pass




    


