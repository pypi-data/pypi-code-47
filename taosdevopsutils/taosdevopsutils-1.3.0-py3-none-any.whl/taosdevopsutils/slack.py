""" Module to handle slack messaging """
import slack
import os
from taosdevopsutils import config
import requests
import json
import logging
import traceback


class Slack:
    def __init__(self, token=config.SLACK_API_TOKEN):
        self.client = slack.WebClient(token=token)

    def _handle_webhook(self, target: str, message: str):
        if isinstance(message, str):
            response = requests.post(
                target, data=message, headers={"Content-Type": "application/json"}
            )
            try:
                payload = json.loads(message)
            except json.JSONDecodeError:
                payload = {"text": message}
        else:
            payload = message

        response = requests.post(target, json=payload)
        return {
            "status_code": response.status_code,
            "ok": response.status_code == 200,
            "message": message,
            "response": response.text,
        }

    def _handle_direct_message(self, target: str, message: str):
        if isinstance(message, str):
            return self.client.chat_postMessage(
                channel=target, text=message, as_user=True
            )
        return self.client.chat_postMessage(channel=target, as_user=True, **message)

    def post_slack_message(self, target: str, message: str):
        if target.startswith("https://"):
            return self._handle_webhook(target, message)
        return self._handle_direct_message(target, message)


class Bot:
    def __init__(self, token=config.SLACK_API_TOKEN, logger=logging):
        self.client = slack.WebClient(token=token)
        self.rtm_client = slack.RTMClient(token=token)
        self.bot_commands = {}
        self.partial_commands = {}
        """ Partial command Dictionary, Used for command continuation"""

        self.logger = logger
        self.bot_data = self.client.auth_test()
        self.bot_string = f"<@{self.bot_data['user_id']}>"
        logger.info(f"Bot Info: {self.bot_data}")
        self._register_functions()
        self.start = self.rtm_client.start

    def _from_bot(self, data, **kwargs):
        return "bot_id" in data and data["bot_id"] == self.bot_data["bot_id"]

    @staticmethod
    def _get_thread(payload: dict) -> str:
        data = payload.get("data", {})
        return data.get("thread_ts") or data.get("ts")

    @staticmethod
    def _is_thread_reply(payload: dict) -> bool:
        return "thread_ts" in payload.get("data", {})

    @staticmethod
    def _has_parameter(command_string: dict, param_prefix="--") -> bool:
        return param_prefix in command_string

    @classmethod
    def _parse_command_string(cls, command_string: str, param_prefix="--"):
        """ Parses command inputs from a string.
        Returns a tuple of command, parsed_parameters.
        """
        pass
        if cls._has_parameter(command_string, param_prefix):
            command_string, *params = [
                part.strip() for part in command_string.split(param_prefix)
            ]
            parameter = {
                key: " ".join(values)
                for param_string in params
                for key, *values in [param_string.split(" ")]
            }
        else:
            parameter = {}
        return command_string, parameter

    def _is_talking_to_me(self, data) -> bool:
        """ Returns if this bots name is mentioned in a message """
        return self.bot_string in data.get("text", [])

    # Decorators
    def talking_to_me(self, func):
        """ Decorator that will supress function if bot was not mentioned. """

        def _internal_(**payload):
            data = payload["data"]
            if not self.bot_string in data.get("text", []):
                return
            return func(**payload)

        return _internal_

    def continue_partial(self, func):
        """ Decorator to handle command continuation
        The decorated function will be supressed if partial command has not
        been registered for this thread id.
        """

        def _internal_(*args, **payload):
            if self._from_bot(**payload) or not self._is_thread_reply(payload):
                return

            try:
                thread_id = self._get_thread(payload)
                command = self.partial_commands[thread_id]
            except KeyError:
                return

            self.logger.info("ContinuePayload: " + json.dumps(payload, default=str))
            return func(command["command_name"], *args, **payload)

        return _internal_

    def respond_to_slack(self, func):
        """ Decorator function that returns responses as a channel notification

        The function will wrap any function that is decorated with
        slack.RTMClient or receives a webclient and the data payload.
        """

        def _internal_(*args, rtm_client=None, web_client=None, **kwargs):
            try:
                response = func(*args, **kwargs)
                self.logger.info(f"Receieved Response: {response}")  # Convert to Logger

                if not isinstance(response, list):
                    response = [response] if response else []

                data = kwargs.get("data", {})
                channel_id = data.get("channel")
                thread_ts = data.get("ts")

                for message in response:
                    try:
                        message = message.decode()
                    except AttributeError:
                        pass

                    web_client.chat_postMessage(
                        channel=channel_id, text=message, thread_ts=thread_ts
                    )
                return response
            except Exception as e:
                self.logger.warn(f"HIT Exception in response:{e}")
                self.logger.warn(traceback.format_exc())
                raise

        return _internal_

    def fetch_partial(self, func):
        """ Decorator to assist with partial lookups.

        The decorated function will receive a partial command for the thread
        if registered otherwise None.
        """

        def _internal_(*args, thread_id=None, **payload):
            try:
                if payload:
                    partial_command = self.partial_commands[thread_id]
                    return func(
                        *args, thread_id=thread_id, partial=partial_command, **payload
                    )
            except KeyError:
                pass
            return func(*args, thread_id=thread_id, **payload)

        return _internal_

    def register(self, command_name):
        """ Decorator to register command to internal registry.

        Anytime @botname 'command_name' is mentioned in slack the string will
        be parsed and given to the decorated function.
        """

        def _wraps(func):
            self.logger.debug(f"Command Registered:{command_name}: {func}")
            self.bot_commands = {command_name: func, **self.bot_commands}
            return func

        return _wraps

    def _register_functions(self):
        """ Internal Command for creating the slack command processors. """

        @slack.RTMClient.run_on(event="message")
        @self.respond_to_slack
        def processor(data=None):
            if not self._is_talking_to_me(data):
                self.logger.debug(f"Not speaking to bot, returning")
                return
            raw_command_text = data.get("text", "").strip()
            raw_command_string = raw_command_text.split(self.bot_string)[1].strip()
            self.logger.info("Text Received:" + raw_command_text)

            command_string, parameters = self._parse_command_string(raw_command_string)
            command, *args = command_string.split(" ")
            self.logger.debug(f"Command Parsed:{command}")

            thread_id = self._get_thread({"data": data})

            try:
                self.logger.info(f"Parsed: {command_string}, {parameters}")
                return self.bot_commands[command](
                    command, *args, parameters=parameters, thread_id=thread_id
                )
            except KeyError:
                return "\n".join(
                    [
                        "Where you talking to me?",
                        "I must have not understood your command, the commands"
                        " I do know are ",
                        *[f"- {command}" for command in self.bot_commands.keys()],
                    ]
                )
            except Exception as e:
                print(e)
                self.logger.warn(e)
                raise

            return "ERROR"

        @slack.RTMClient.run_on(event="message")
        @self.continue_partial
        @self.respond_to_slack
        def continuer(command_name, data, **payload):
            """ Continues command if thread id of the message has a registered partial
            """
            raw_command_text = data.get("text", "").strip()
            thread_id = self._get_thread({"data": data})

            try:
                raw_command_string = raw_command_text.split(self.bot_string)[1]
                command_string, parameters = self._parse_command_string(
                    raw_command_string
                )
            except IndexError:
                command_string, parameters = self._parse_command_string(
                    raw_command_text
                )

            return self.bot_commands[command_name](
                command_name,
                *command_string.split(" "),
                parameters=parameters,
                thread_id=thread_id,
                **payload,
            )
