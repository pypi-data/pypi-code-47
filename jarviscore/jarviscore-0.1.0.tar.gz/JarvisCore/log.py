from .model import Model
from .helpers import Helpers
from .settings import Settings
from pathlib import Path
from .errors import MissingSetting, ConfigFileNotFound

class _bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'py
    UNDERLINE = '\033[4m'


class Log():
    log_format: str
    instance: str
    verbose: list
    client: str
    model: Model

    def __init__(self, instance, client="Twitch", verbose=None, enable_db=False):
        if enable_db:
            self.model = Model()
        self.enable_db = enable_db
        if verbose is None:
            try:
                verbose = Settings().get_setting("log")
            except MissingSetting:
                verbose = "log"
            except ConfigFileNotFound:
                verbose = "log"
        

        self.log_format = "\033[92m{time}\033[0m ({level}) [{instance}]: {message}"
        self.log_file_format = "{time} ({level}) [{instance}]: {message}\n"
        self.instance = instance
        self.client = client
        if verbose == "debug":
            self.verbose = ["debug", "log", "info", "warn", "error"]
        elif verbose == "log":
            self.verbose = ["log", "info", "warn", "error"]
        elif verbose == "info":
            self.verbose = ["info", "warn", "error"]
        elif verbose == "warn":
            self.verbose = ["warn", "error"]
        elif verbose == "error":
            self.verbose = ["error"]


    def debug(self, message):
        if "debug" in self.verbose:
            self.__render({
                "time": Helpers().get_timestamp(),
                "level": "dbug",
                "instance": self.instance,
                "message": message
            })
        self.__record(message, "debug")

    def log(self, message):
        if "log" in self.verbose:
            self.__render({
                "time": Helpers().get_timestamp(),
                "level": "log_",
                "instance": self.instance,
                "message": message
            })
        self.__record(message, "log")
    
    def info(self, message):
        if "info" in self.verbose:        
            self.__render({
                "time": Helpers().get_timestamp(),
                "level": f"{_bcolors.OKBLUE}info{_bcolors.ENDC}",
                "instance": self.instance,
                "message": message
            })
        self.__record(message, "info")
    
    def chat(self, message, channel):
        if "info" in self.verbose:        
            self.__render({
                "time": Helpers().get_timestamp(),
                "level": f"{_bcolors.OKBLUE}chat{_bcolors.ENDC}",
                "instance": f"{_bcolors.OKGREEN}{channel}{_bcolors.ENDC}",
                "message": message
            })
        self.__record(message, "chat")
    
    def warn(self, message):
        if "warn" in self.verbose:
            self.__render({
                "time": Helpers().get_timestamp(),
                "level": f"{_bcolors.WARNING}warn{_bcolors.ENDC}",
                "instance": self.instance,
                "message": f"{_bcolors.WARNING}{message}{_bcolors.ENDC}"
            })
        self.__record(message, "warn")
        self.__send_pushover_alert(message, "warn")

    
    def error(self, message):
        if "error" in self.verbose:
            self.__render({
                "time": Helpers().get_timestamp(),
                "level": f"{_bcolors.FAIL}errr{_bcolors.ENDC}",
                "instance": self.instance,
                "message": f"{_bcolors.FAIL}{message}{_bcolors.ENDC}"
            })
        self.__record(message, "error")
        self.__send_pushover_alert(message, "error")

    def set_verbose(self, verbose):
        self.info(f"Updating verbosity to '{verbose}'")
        if verbose == "debug":
            self.verbose = ["debug", "log", "info", "warn", "error"]
        elif verbose == "log":
            self.verbose = ["log", "info", "warn", "error"]
        elif verbose == "info":
            self.verbose = ["info", "warn", "error"]
        elif verbose == "warn":
            self.verbose = ["warn", "error"]
        elif verbose == "error":
            self.verbose = ["error"]

    def set_instance(self, instance):
        self.instance = instance

    def __render(self, data):
        Path(str(Path().absolute())+'/logs').mkdir(parents=True, exist_ok=True)
        with open(Path(str(Path().absolute()) + "/logs/" + self.client + ".log"), "a") as f:
            f.write(self.log_file_format.format(**data))
        print(self.log_format.format(**data))


    def __record(self, message, level):
        sanitisedMessage = message \
            .replace("'", "''") \
            .replace("\"","\"\"")
        query = f"insert into Logs (Source, Message, LogLevel, LogTime, Component) values ('{self.instance}', '{sanitisedMessage}', '{level}', '{Helpers().get_timestamp()}', '{self.client}')"
        try:
            if self.enable_db:
                self.model.insert(query)
        except Exception as ex:
            print(f"{_bcolors.FAIL}An exception occurred saving the log to the database{_bcolors.ENDC}")
            print(f"Exception: {ex}")
            print(f"Query: {query}")
    
    def __send_pushover_alert(self, message: str, log_level: str):
        pass



