from logging import Handler

from opsas.utils.HttpSession import HttpSession


class SlackMessager(HttpSession):

    def __init__(self, logger, token, channel):
        super().__init__(logger, endpoint='https://slack.com/api')
        self.session.headers.setdefault('Authorization', 'Bearer ' + token)
        self.session.headers.setdefault('Content-Type', 'application/json')
        self.channel = channel

    def post_payload(self, payload):
        response = self.request_conn(method='post', path='/chat.postMessage', data=payload).json()
        self.logger.info(response)
        return response

    def send_text_message(self, message):
        payload = {
            'channel': self.channel,
            'text': message,
            'type': 'text'
        }
        return self.post_payload(payload)

    def send_message(self, message, infolevel="debug", thread_ts=None):
        payload = self.make_payload(message, infolevel, thread_ts=thread_ts)
        return self.post_payload(payload)

    def create_thread(self, name):
        response = self.send_text_message(name)
        return response['ts']

    def make_payload(self, message, loglevel, thread_ts=None):
        self.logger.debug(loglevel)
        payload = {
            'channel': self.channel,
            'blocks': [
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "image",
                            "image_url": f"http://img.justcalm.ink/{loglevel}.png",
                            "alt_text": f"{loglevel} icon"
                        },
                        {
                            "type": "mrkdwn",
                            "text": message
                        }
                    ]
                }
            ]
        }
        if thread_ts is not None:
            payload['thread_ts'] = thread_ts
        return payload


class SlackLogHandler(Handler):
    """
    Use slack as log handlers
    :argument
    token: str, slack bot token
    channel: str, slack app oauth token
    logger: local logger used by slack handler
    """
    _thread_ts_list = {}

    def __init__(self, token, channel, logger):
        super().__init__()
        self.bot = SlackMessager(token=token, channel=channel, logger=logger)
        print("__II")

    """
    slackloghandler will send message to slack channel by default.
    When used create sessopm, all logs will send as reply to this message
    """

    def create_session(self, name):
        self._thread_ts_list[name] = self.bot.create_thread(name)

    def emit(self, record):
        msg = self.format(record)
        thread_name = record.name
        thread_ts = self._thread_ts_list.get(thread_name, None)
        return self.bot.send_message(message=msg, infolevel=record.levelname.lower(), thread_ts=thread_ts)
