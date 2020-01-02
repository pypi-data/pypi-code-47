from unittest import TestCase
from taosdevopsutils.slack import Slack, Bot
import slack
import requests


class TestSlackClass:
    def test_slack_posts_http_when_given_webhook(self, mocker):
        slack_mock = mocker.patch.object(slack.WebClient, "chat_postMessage")
        requests_mock = mocker.patch.object(requests, "post")
        slack_client = Slack()
        slack_client.post_slack_message("https://slack/webhook/somehook", "SomeMessage")
        assert not slack_mock.called
        assert requests_mock.called

    def test_slack_posts_message_when_given_user_id(self, mocker):
        slack_mock = mocker.patch.object(slack.WebClient, "chat_postMessage")
        requests_mock = mocker.patch.object(requests, "post")
        slack_client = Slack()
        slack_client.post_slack_message("U123456", "SomeMessage")
        assert slack_mock.called
        assert not requests_mock.called

    def test_slack_wraps_simple_strings_in_text_json(self, mocker):
        message = "SomeMessage"
        expected_payload = {"text": message}
        requests_mock = mocker.patch.object(requests, "post")

        slack_client = Slack()
        slack_client.post_slack_message("https://slack/webhook/somehook", "SomeMessage")

        requests_mock.assert_called_with(
            "https://slack/webhook/somehook", json=expected_payload
        )


class TestSlackBot:
    def test_slack_bot_registers_function(self, mocker):
        slack_mock = mocker.patch.object(slack.WebClient, "auth_test")
        slack_mock.return_value = {"user_id": "BOTA"}
        bot = Bot()

        @bot.register("testfunction")
        def test():
            return "Hello World"

        assert bot.bot_commands["testfunction"] == test
