"""
UNIVERSAL LOG CONFIGURATOR
For this module to work you have to creathe a LogObject at the very first
__init__.py of your project. Now you just have to import this object from
the __init__ to each module you want to have loggs. Also, you need to
specify the project path to use external files. To get your project path
simply use the module os with the next line:

             'os.path.dirname(os.path.abspath(__file__))'

This universal log configurator it's an easy way to configure Python
logging with a clean code.

Also, this tool has a simple AutoLog to make debug logs with a decorator
on any function.
"""

from __future__ import absolute_import

import os
import logging
import inspect
import shutil

from datetime import datetime
from inspect import getframeinfo, stack

class LogObject():
    """
    Personal centralized logging experience with support to handle (avoid)
    Flask and URLLIB logs.
    """
    execution_time = str(datetime.now())[:18]
    logroot = None # This is the handler of the logging
    external_path = ""

    #This dictionary contains the booleans of the options you can select
    #when launch the constructor.
    booleans = {
        "debug_bool"        : False,
        "rich_debug_bool"   : False,
        "flask"             : False,
        "urllib"            : False,
        "clean_log"         : False,
        "error_file"        : False
    }

    #This dictionary have all the message information.
    message = {
        "header_format"  :   "",
        "message"        :   "",
        "level"          :   "",
        "line"           :   "",
        "file"           :   "",
        "funtion"        :   "",
        "caller_module"  :   ""
    }

    def __init__(self, debug_bool=False, rich_debug_bool=False,
                 external=None, clean_log=False, flask=False,
                 urllib=False, app=None):
        """Init of the LogObject
        This init will create the object and configure the logging.

        :param debug_bool: specify if DEBUG level messages will be
                           shown, defaults to False
        :type debug_bool: bool, optional

        :param rich_debug_bool: specify if the messages are detailed and
                                parseable, defaults to False
        :type rich_debug_bool: bool, optional

        :param external: send the path for the logs to save
        :type external: str, optional

        :param clean: clean the log folder, defaults to False
        :type clean: bool, optional

        :param flask: specify if flask is used on the project, defaults
                      to False
        :type flask: bool, optional

        :param urllib: specify if urllib is used on the project,
                       defaults to False
        :type urllib: bool, optional

        :param app: if flask is specified to be used, app will be the
                    object of Flask, defaults to None
        :type app: Flask Object, optional
        """
        # Initialize variables
        handler = logging.StreamHandler()
        self.logroot = logging.getLogger()
        self.booleans["debug_bool"] = debug_bool
        self.booleans["flask"] = flask
        self.booleans["urllib"] = urllib
        self.booleans["rich_debug_bool"] = rich_debug_bool
        self.booleans["external"] = external
        self.booleans["clean_log"] = clean_log
        self.root_dir = inspect.getmodule

        # Start logging configuration
        self.logroot.addHandler(handler)
        self.configure_logs(app)

        # Check if external file has to be created
        if external is not None:
            self.external_path = external
            self.externalize_logs(handler)

    def configure_logs(self, app=None):
        """ Initialize logs configuration.
        Initialize the logs configuration depending on the options
        entered when the object was created (constructor).

        :param app: If flask is specified, app is the objecto of flask,
                    defaults to None
        :type app: Flask Object, optional
        """
        #Initialize default logs.
        self.logroot.disabled = False
        if self.booleans["debug_bool"]:
            self.logroot.setLevel(logging.DEBUG)
        else:
            self.logroot.setLevel(logging.INFO)

        #Initialize flask logs if specified.
        if self.booleans["flask"]:
            logflask = logging.getLogger('werkzeug')
            app.logger.disabled = True
            logflask.disabled = False
            if self.booleans["debug_bool"]:
                logflask.setLevel(logging.DEBUG)
            else:
                logflask.setlevel(logging.INFO)

        #Initialize urllib logs if specified.
        if self.booleans["urllib"]:
            loglib = logging.getLogger('urllib3.connectionpool')
            loglib.disabled = False
            if self.booleans["debug_bool"]:
                loglib.setLevel(logging.DEBUG)
            else:
                loglib.setLevel(logging.INFO)

    def update_header_format(self, callerg=getframeinfo(stack()[1][0])):
        """Custom header maker for logs
        Change the format of the header as the logging module can't
        be modified properly with the method I'm using. For example,
        if I want to put the line number of the log, it will show the
        line of this library.

        This function will make a default logging header with the
        message or a parseable detailed logging in JSON format
        (dictionary).

        :param callerg: getframeinfo object to get some data, at the
                       start of the development of this function the
                       callerg object does more, but at this time it's
                       pretty much useless, defaults to
                       getframeinfo(stack()[1][0])
        :type callerg: getframeinfo Object, optional
        """
        # Set the parseable format of the header or just a simple loging
        if self.booleans["rich_debug_bool"]:
            self.message["header_format"] = {
                "level" : self.message["level"],
                "file" : callerg.filename,
                "line" : self.message["line"],
                "module" : self.message["caller_module"],
                "function" : self.message["function"],
                "message" : "None"
            }
        elif self.booleans["debug_bool"]:
            self.message["header_format"] = "[%s at %s:%s, function %s]: " \
                % (self.message["level"],
                   self.message["caller_module"],
                   self.message["line"],
                   self.message["function"])
        else:
            self.message["header_format"] = "[%s]: " % self.message["level"]

    def print_saved_message(self):
        """Will print the saved messages previously.
        Look at the saved message and take the saved level to show a
        message using the logging library.

        The modularization of this message print is to imitate the
        logging capabilities of just call the function without too
        many characters.
        """
        #Check wich to header use before show the message.
        if self.booleans["rich_debug_bool"]:
            #The next line raise a false pylint positive. It works propperly!
            self.message["header_format"]["message"] = self.message["message"]                      #pylint: disable=unsupported-assignment-operation
            text_to_show = self.message["header_format"].__str__()
        else:
            text_to_show = self.message["header_format"].__str__() \
                + self.message["message"].__str__()

        # Print the message depending on the level specified.
        if self.message["level"] == "INFO":
            logging.info(text_to_show)
        elif self.message["level"] == "WARNING":
            logging.warning(text_to_show)
        elif self.message["level"] == "ERROR":
            logging.error(text_to_show)
        elif self.message["level"] == "CRITICAL":
            logging.critical(text_to_show)
        elif self.message["level"] == "DEBUG":
            logging.debug(text_to_show)

    def externalize_logs(self, handler):
        """Write logs on external file.
        This will try to create the folder and files to save the external
        logs from the main module. In case it fails it won't try it again
        to prevent an infinite loop.

        :param handler: the logging handler.
        :type handler: logging object
        """
        root_dir = self.external_path
        # Delete all the logging folder if specified.
        if self.booleans["clean_log"]:
            try:
                shutil.rmtree(root_dir + "/logs")
                self.debug("Logs folder and it's content was removed.")
            except OSError:
                self.booleans["error_file"] = True
                self.error("Autolog couldn't remove the log folder.")

        # Check if the directory exists and create it if not.
        if not os.path.exists(root_dir + "/logs"):
            try:
                os.mkdir(root_dir + "/logs")
                self.debug("Logs folder created on %s." % root_dir)
            except OSError:
                self.booleans["error_file"] = True
                self.error("AutoLog couldn't create the folder for logs.")

        if self.booleans["error_file"]:
            # Create the new handler for logging on external file.
            exthand = logging.FileHandler(root_dir + "/logs/" \
                                                   + self.execution_time \
                                                   + ".log")

            # Apply changes on the handler and logroot.
            exthand.format = handler.format
            self.logroot.addHandler(exthand)

    #------------------- Log level calls from code --------------------#
    def log(self, message_text, function_name, line, caller_module
            callerg=getframeinfo(stack()[1][0]), level="DEBUG"):
        """Get ready the message to print
        Get all the messages from all the level calls and save them to
        print it later.

        :param message_text: Text of the message.
        :type message_text: str

        :param function_name: Name of the actual function.
        :type function_name: str

        :param line: Number of line
        :type line: str

        :param caller_module: This contains the information about the
                              caller module.
        :type caller_module: inspect object

        :param callerg: getframeinfo object to get some data, at the
                       start of the development of this function the
                       callerg object does more, but at this time it's
                       pretty much useless, defaults to
                       getframeinfo(stack()[1][0])
        :type callerg: getfrarmeinfo object, optional

        :param level: the level of the log, defaults to "DEBUG"
        :type level: str, optional
        """
        self.message["message"] = message_text
        self.message["level"] = level
        self.message["function"] = function_name
        self.message["line"] = line
        self.message["caller_module"] = caller_module.__name__
        self.update_header_format(callerg)
        self.print_saved_message()

    def info(self, message_text, lineno=None, function=None):
        """Print INFO
        Method to save a message on the object with INFO level.

        :param message_text: text to show on the log.
        :type message_text: str
        """
        callerg = getframeinfo(stack()[1][0])
        calleri = inspect.stack()[1]
        caller_module = inspect.getmodule(calleri[0])

        if lineno is None:
            lineno = callerg.lineno
        if function is None:
            function = callerg.function
        self.log(message_text, function, lineno, caller_module, callerg,
                 "INFO")

    def warning(self, message_text, lineno=None, function=None):
        """Print WARNING
        Method to save a message on the object with WARNING level.

        :param message_text: text to show on the log.
        :type message_text: str
        """
        callerg = getframeinfo(stack()[1][0])
        calleri = inspect.stack()[1]
        caller_module = inspect.getmodule(calleri[0])

        if lineno is None:
            lineno = callerg.lineno
        if function is None:
            function = callerg.function
        self.log(message_text, function, lineno, caller_module, callerg,
                 "WARNING")

    def error(self, message_text, lineno=None, function=None):
        """Print ERROR
        Method to save a message on the object with ERROR level.

        :param message_text: text to show on the log.
        :type message_text: str
        """
        callerg = getframeinfo(stack()[1][0])
        calleri = inspect.stack()[1]
        caller_module = inspect.getmodule(calleri[0])

        if lineno is None:
            lineno = callerg.lineno
        if function is None:
            function = callerg.function
        self.log(message_text, function, lineno, caller_module, callerg,
                 "ERROR")

    def critical(self, message_text, lineno=None, function=None):
        """Print CRITICAL
        Method to save a message on the object with CRITICAL level.

        :param message_text: text to show on the log.
        :type message_text: str
        """
        callerg = getframeinfo(stack()[1][0])
        calleri = inspect.stack()[1]
        caller_module = inspect.getmodule(calleri[0])

        if lineno is None:
            lineno = callerg.lineno
        if function is None:
            function = callerg.function
        self.log(message_text, function, lineno, caller_module, callerg,
                 "CRITICAL")

    def debug(self, message_text, lineno=None, function=None):
        """Print DEBUG
        Method to save a message on the object with DEBUG level.

        :param message_text: text to show on the log.
        :type message_text: str
        """
        callerg = getframeinfo(stack()[1][0])
        calleri = inspect.stack()[1]
        caller_module = inspect.getmodule(calleri[0])

        if lineno is None:
            lineno = callerg.lineno
        if function is None:
            function = callerg.function
        self.log(message_text, function, lineno, caller_module, callerg,
                 "DEBUG")
    #------------------------------------------------------------------#

    #Autolog decorator
    def autolog(self, function):
        """Decorator for automatic logging
        To beautify and easify some coding process. This will be allways
        a debug log because the user don't need to know what function
        is executing. This will be helpful for the developers.

        :param function: Function to autolog
        :type function: Function
        :return: The actual function output.
        :rtype: Unknown
        """
        def wrapper(*args, **kwargs):
            """
            Wrapper of the decorator, this covers the function and makes
            actions before and after.
            If the function has an error, this will let it explode. It
            could handle it but it's better to have more information.
            """

            #Initialize and declare variables
            message = ""
            function_input = []

            arguments = inspect.getfullargspec(function)[0]
            line = getframeinfo(stack()[1][0]).lineno
            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 2)
            function_name = calframe[1][3]

            # Look all the arguments and it's names, if an argument is
            # the default value it will be "Default" because this
            # wrapper can't get the value of default arguments.
            for argument in enumerate(arguments):
                index = argument[0]
                try:
                    arg = str(args[index])
                except IndexError:
                    arg = "Default"

                attribute = str(argument[1])
                function_input.append(attribute + ": " + arg)

            # Create the message to show on the log.
            message = "Starting function '%s', input values: %s" % \
                (function.__name__, function_input)

            # Call the debug logging method.
            self.debug(message, line, function_name)

            # Execute the function
            output = function(*args, **kwargs)

            # Check the output
            if output is None:
                message = "Function '%s' finished without output" \
                    % (function.__name__)
            else:
                message = "Function '%s' finished with output: %s" \
                    % (function.__name__, output)

            # Call the debug logging method again.
            self.debug(message, line, function_name)

            return output

        return wrapper
