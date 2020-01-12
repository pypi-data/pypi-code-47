from ..command import Command
from ..message import PrivateMessage, CommandMessage

class Ping(Command):

    def __init__(self, channel):
        Command.__init__(self, "Ping")
        self.channel = channel

    def on_privmessage(self, data: PrivateMessage):
        if "ping" == data.message_text and data.user_id == "82504138":
            self.channel.socket.send_message(data.channel, "Pong")
            log(f"sent, 'Pong' to '{data.channel}'")
    
    def on_command(self, data: CommandMessage):
        if "ping" == data.KEYWORD and data.user_id == "82504138":
            self.channel.socket.send_message(data.channel, "Pong")
            log(f"sent, 'Pong' to '{data.channel}'")

def log(msg):
    print(f"CORE|PING: {msg}")


def setup(channel):
    channel.load_command(Ping(channel))
    log(f"[{channel.name}]: Loaded Module Ping")

def teardown(channel):
    log(f"[{channel.name}]: Removed Module Ping")