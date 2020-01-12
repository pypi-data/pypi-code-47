import sys
from importlib import util
from copy import deepcopy
from os import path, listdir

from .socket import SendSocket
from .command import Command, CommandResponse
from .message import *
from .errors import ExtensionAlreadyLoaded, ExtensionNotFound, ExtensionFailed, NoEntryPointError 
from .log import Log


class Channel():

    name: str
    __modules: dict
    __commands: dict
    socket: SendSocket

    def __init__(self, name: str = "undefined"):
        self.name = name
        self.__modules = {}
        self.__commands = {}

        self.log = Log(instance=name, client="Twitch Channel")
        pass

    # Public commands for use in the Bridge and in Commands

    def propogate(self, socket: SendSocket, channel_name: str):
        self.name = channel_name
        self.log.set_instance(channel_name)
        newchannel = deepcopy(self)
        newchannel.__cache_commands()
        newchannel.socket = socket
        if channel_name != "undefined":
            newchannel.socket.join(channel_name)
        return newchannel
        


    def send(self, message):
        self.log.debug(f"not implemented: SEND > {message}")
        # self.__bridge..... 
        pass

    def load_command(self, command):
        self.__commands[command.name] = command



    # Callbacks used by the bridge for all Messages sent via the inbound socket.

    ### to do: add the rest of the message types in here

    # Base Callback
    def on_raw(self, data: RawMessage):
        self.log.debug("`on_raw` invoked.")
        for command in self.__get_command_with_handler("on_raw"):
            command.on_raw(data)

    # IRC: Membership Callbacks

    def on_join(self, data: Join):
        self.log.debug("`on_join` invoked.")
        for command in self.__get_command_with_handler("on_join"):
            command.on_join(data)

    def on_part(self, data: Part):
        self.log.debug("`on_part` invoked.")
        for command in self.__get_command_with_handler("on_part"):
            command.on_part(data)

    def on_mode(self, data: Mode):
        self.log.debug("`on_mode` invoked.") 
        for command in self.__get_command_with_handler("on_mode"):
            command.on_mode(data)

    def on_names(self, data: Names):
        self.log.debug("`on_names` invoked.")
        for command in self.__get_command_with_handler("on_names"):
            command.on_names(data)

    # IRC: Command & Tag Callbacks

    def on_clearchat(self, data: ClearChat):
        self.log.debug("`on_clearchat` invoked.")
        for command in self.__get_command_with_handler("on_clearchat"):
            command.on_clearchat(data)

    def on_clearmessage(self, data: ClearMessage):
        self.log.debug("`on_clearmessage` invoked.")
        for command in self.__get_command_with_handler("on_clearmessage"):
            command.on_clearmessage(data)
    
    def on_hosttarget(self, data: HostTarget):
        self.log.debug("`on_hosttarget` invoked.")
        for command in self.__get_command_with_handler("on_hosttarget"):
            command.on_hosttarget(data)

    def on_notice(self, data: Notice):
        self.log.debug(f"`on_notice` invoked. (not implemented)")
        for command in self.__get_command_with_handler("on_notice"):
            command.on_notice(data)

    def on_reconnect(self, data: Reconnect):
        self.log.debug("`on_reconnect` invoked.")
        for command in self.__get_command_with_handler("on_reconnect"):
            command.on_reconnect(data)

    def on_roomstate(self, data: RoomState):
        self.log.debug("`on_roomstate` invoked.")
        for command in self.__get_command_with_handler("on_roomstate"):
            command.on_roomstate(data)

    def on_userstate(self, data: UserState):
        self.log.debug("`on_userstate` invoked.")
        for command in self.__get_command_with_handler("on_userstate"):
            command.on_userstate(data)

    def on_globaluserstate(self, data: GlobalUserState):
        self.log.debug("`on_globaluserstate` invoked.")
        for command in self.__get_command_with_handler("on_globaluserstate"):
            command.on_globaluserstate(data)

    def on_privmessage(self, data: PrivateMessage):
        self.log.debug("`on_privmessage` invoked.")
        for command in self.__get_command_with_handler("on_privmessage"):
            command.on_privmessage(data)
        
    def on_usernotice(self, data: UserNotice):
        self.log.debug("`on_usernotice` invoked.")
        for command in self.__get_command_with_handler("on_usernotice"):
            command.on_usernotice(data)

    def on_ritual_usernotice(self, data: RitualUserNotice):
        self.log.debug("`on_ritual_usernotice` invoked.")
        for command in self.__get_command_with_handler("on_ritual_usernotice"):
            command.on_ritual_usernotice(data)

    def on_bitbadgeupgrade_usernotice(self, data: BitBadgeUpgradeUserNotice):
        self.log.debug("`on_bitbadgeupgrade_usernotice` invoked.")
        for command in self.__get_command_with_handler("on_bitbadgeupgrade_usernotice"):
            command.on_bitbadgeupgrade_usernotice(data)

    def on_raid_usernotice(self, data: RaidUserNotice):
        self.log.debug("`on_raid_usernotice` invoked.")
        for command in self.__get_command_with_handler("on_raid_usernotice"):
            command.on_raid_usernotice(data)

    def on_subscriber_usernotice(self, data: SubscriberUserNotice):
        self.log.debug("`on_subscriber_usernotice` invoked.")
        for command in self.__get_command_with_handler("on_subscriber_usernotice"):
            command.on_subscriber_usernotice(data)
    
    def on_giftedsubscriber_usernotice(self, data: GiftedSubscriberUserNotice):
        self.log.debug("`on_giftedsubscriber_usernotice` invoked.")
        for command in self.__get_command_with_handler("on_giftedsubscriber_usernotice"):
            command.on_giftedsubscriber_usernotice(data)

    def on_command(self, data: CommandMessage):
        self.log.debug("`on_command` invoked.")
        for command in self.__get_command_with_handler("on_command"):
            command.on_command(data)






    # backend commands for managing the loading and processing of command modules
    
    def __cache_commands(self):
        commands = []
        for _file in listdir(path.join(path.dirname(__file__), 'commands/')):
            if "__init__" not in _file:
                print ("r1: Found: ", _file)
                filename, ext = path.splitext(_file)
                if '.py' in ext:
                    commands.append(f'jarviscore.commands.{filename}')
        
        if path.exists("commands/"):
            for _file in listdir('commands/'):
                print ("r2: Found: ", _file)
                filename, ext = path.splitext(_file)
                if '.py' in ext:
                    commands.append(f'commands.{filename}')

        for extension in reversed(commands):
            try:
                print("attempting to load: ", extension)
                self._load_command(f'{extension}')
            except Exception as e:
                exc = f'{type(e).__name__}: {e}'
                print(f'Failed to load extension {extension}\n{exc}')
        

    def _load_command(self, name):
        if name in self.__modules:
            raise ExtensionAlreadyLoaded(name)

        spec = util.find_spec(name)
        if spec is None:
            raise ExtensionNotFound(name)

        self._load_from_module_spec(spec, name)

    
    def _load_from_module_spec(self, spec, key):
        lib = util.module_from_spec(spec)
        sys.modules[key] = lib
        try:
            spec.loader.exec_module(lib)
        except Exception as e:
            del sys.modules[key]
            raise ExtensionFailed(key, e) from e

        try:
            setup = getattr(lib, 'setup')
        except AttributeError:
            del sys.modules[key]
            raise NoEntryPointError(key)

        try:
            setup(self)
        except Exception as e:
            del sys.modules[key]
            self._call_module_finalizers(lib, key)
            raise ExtensionFailed(key, e) from e
        else:
            self.__modules[key] = lib

    

    def _call_module_finalizers(self, lib, key):
        try:
            teardown = getattr(lib, 'teardown')
        except AttributeError:
            pass
        else:
            try:
                teardown(self)
            except Exception:
                pass
        finally:
            self.__modules.pop(key, None)
            sys.modules.pop(key, None)

    def __get_command_with_handler(self, handler: str):
        for command in self.__commands:
            try:
                if hasattr(self.__commands[command], handler):
                    yield self.__commands[command]
            except AttributeError:
                pass
            


            


        
        

    
