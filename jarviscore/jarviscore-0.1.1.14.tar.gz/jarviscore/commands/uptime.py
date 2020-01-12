from ..command import Command
from ..message import CommandMessage
from ..httpclient import HTTPClient, WebResponse

from datetime import datetime

class Uptime(Command):

    def __init__(self, channel):
        Command.__init__(self, "Uptime")
        self.channel = channel
    
    def on_command(self, data: CommandMessage):
        if "uptime" == data.KEYWORD:
            client = HTTPClient("Uptime Command Handler")
            streamURL = f"https://api.twitch.tv/helix/streams?user_login={data.channel}"
            response = client.GetFromTwitch(streamURL)
            message = ""
            if len(response.json["data"]) > 0:
                delta = datetime.utcnow() - datetime.strptime(response.json["data"][0]["started_at"],"%Y-%m-%dT%H:%M:%SZ")
                seconds = int(round(delta.total_seconds()))
                minutes, seconds = divmod(seconds, 60)
                hours, minutes = divmod(minutes, 60)
                message = "{:d} hours, {:02d} minutes".format(hours, minutes)
            else:
                message = f"{data.display_name} isn't live right now, please try again later when the stream is live."
            self.channel.socket.send_message(data.channel, message)

            log(f"sent, '{message}' to '{data.channel}'")

def log(msg):
    print(f"CORE|UPTIME: {msg}")


def setup(channel):
    channel.load_command(Uptime(channel))
    log(f"[{channel.name}]: Loaded Module Uptime")

def teardown(channel):
    log(f"[{channel.name}]: Removed Module Uptime")