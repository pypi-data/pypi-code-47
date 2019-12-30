import os
from botfriend.bot import ScriptedBot

class TimeBot(ScriptedBot):
    ROOT_DIR = os.path.split(__file__)[0]
Bot = TimeBot
