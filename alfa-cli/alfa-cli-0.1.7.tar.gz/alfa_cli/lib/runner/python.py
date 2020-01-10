import cProfile
import os
import pstats
import json
import importlib
import re
import sys

from alfa_sdk.common.exceptions import AlfaConfigError


class PythonRunner:
    def __init__(self, invoke_config):
        self.invoke_config = invoke_config
        self.handler = self.import_handler()

    #

    def get_handler_definition(self, invoke_config):
        ERROR_MESSAGE = "invoke function handler not defined"

        invoke_config_function = invoke_config.get("function")
        if not invoke_config_function:
            raise AlfaConfigError(message="Invalid configuration", error=ERROR_MESSAGE)

        invoke_config_handler = invoke_config_function.get("handler")
        if not invoke_config_handler:
            raise AlfaConfigError(message="Invalid configuration", error=ERROR_MESSAGE)

        return invoke_config_handler

    def get_handler_parameters(self, invoke_config):
        ERROR_MESSAGE = "invoke function parameters not defined"

        invoke_config_function = invoke_config.get("function")
        if not invoke_config_function:
            raise AlfaConfigError(message="Invalid configuration", error=ERROR_MESSAGE)

        invoke_config_parameters = invoke_config_function.get("parameters")
        if not invoke_config_parameters:
            raise AlfaConfigError(message="Invalid configuration", error=ERROR_MESSAGE)

        return invoke_config_parameters

    #

    def import_handler(self):
        sys.path.insert(0, os.path.join(os.getcwd(), "invoke"))

        handler_definition = self.get_handler_definition(self.invoke_config)
        module_name = ".".join(handler_definition.split(".")[:-1])
        function_name = handler_definition.split(".")[-1]

        module = importlib.import_module(module_name)
        invoke = getattr(module, function_name)

        return invoke

    #

    def run(self, problem, to_profile, profile_sort):
        arguments = self.map_problem_to_arguments(problem)

        if to_profile:
            return self.run_profile(arguments, profile_sort)

        return self.handler(*arguments)

    def map_problem_to_arguments(self, problem):
        parameters = self.get_handler_parameters(self.invoke_config)

        if type(problem) is not dict:
            try:
                problem = json.loads(problem)
            except ValueError:
                raise ValueError("Problem must be a valid JSON string or a dict.")

        return self.get_parameter_values(parameters, problem)

    def get_parameter_values(self, parameters, problem):
        arguments = []
        for parameter in parameters:
            if isinstance(parameter, dict):
                for name, default_value in parameter.items():
                    arguments.append(problem.get(name, default_value))
            else:
                arguments.append(problem.get(parameter))

        return tuple(arguments)

    #

    def run_profile(self, arguments, sort):
        profiler = cProfile.Profile()
        profiler.enable()

        try:
            result = self.handler(*arguments)
        finally:
            profiler.disable()
            profile_stats = pstats.Stats(profiler, stream=sys.stdout)

            if sort:
                parsed_sort = re.sub(r"[\(\)\[\]]", "", sort).split(",")
                profile_stats.sort_stats(*parsed_sort)
            else:
                profile_stats.sort_stats("time")

            profile_stats.print_stats()

        return result
