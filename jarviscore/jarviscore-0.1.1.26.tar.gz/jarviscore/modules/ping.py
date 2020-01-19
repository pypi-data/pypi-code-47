from .. import Module, Log
from .. import PrivateMessage, CommandMessage

log = Log("CORE:Ping", verbose="log")
class Ping(Module):

    def __init__(self, channel):
        Module.__init__(self, "Ping")
        self.channel = channel

    def on_privmessage(self, data: PrivateMessage):
        if "ping" == data.message_text and data.user_id == "82504138":
            self.channel.send("pong")
    
    def on_command(self, data: CommandMessage):
        if "ping" == data.KEYWORD and data.user_id == "82504138":
            self.channel.send("pong")


def setup(channel):
    channel.load_module(Ping(channel))
    log.log(f"[{channel.name}]: Loaded Module Ping")

def teardown(channel):
    log.log(f"[{channel.name}]: Removed Module Ping")