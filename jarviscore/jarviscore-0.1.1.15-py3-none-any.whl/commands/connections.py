from ..command import Command
from ..message import PrivateMessage, CommandMessage

class Connections(Command):

    def __init__(self, channel):
        Command.__init__(self, "Connections")
        self.channel = channel
    
    def on_command(self, data: CommandMessage):
        if data.KEYWORD == "join":
            if data.channel != self.channel.name and \
            (data.args[1] == data.display_name.lower() or data.user_id == "82504138"):
                self.channel.socket.connect_to_channel(data.args[1])
                self.channel.socket.send_message(data.channel, f"Attempting to connect to `{data.args[1]}`")
                log(f"Attempting to connect to `{data.args[1]}`")
            else:
                log(f"unauthorised attempt to connect to `{data.args[1]}`")

def log(msg):
    print(f"Connections: {msg}")


def setup(channel):
    channel.load_command(Connections(channel))
    log(f"[{channel.name}]: Loaded Module Connections")

def teardown(channel):
    log(f"[{channel.name}]: Removed Module Connections")