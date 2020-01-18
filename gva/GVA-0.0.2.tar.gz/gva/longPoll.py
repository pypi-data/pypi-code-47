import threading

import requests

from . import objects
from .methods.groups.getLongPollServer import getLongPollServer


class LongPoll:
    EVENT_MESSAGE_NEW = "message_new"
    EVENT_MESSAGE_ALLOW = "message_allow"
    EVENT_MESSAGE_REPLY = "message_reply"
    EVENT_MESSAGE_DENY = "message_deny"
    EVENT_MESSAGE_EDIT = "message_edit"
    EVENT_MESSAGE_TYPING_STATE = "message_typing_state"
    EVENT_PHOTO_NEW = "photo_new"
    EVENT_PHOTO_COMMENT_NEW = "photo_comment_new"
    EVENT_PHOTO_COMMENT_EDIT = "photo_comment_edit"
    EVENT_PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    EVENT_PHOTO_COMMENT_DELETE = "photo_comment_delete"
    EVENT_AUDIO_NEW = "audio_new"
    EVENT_VIDEO_NEW = "video_new"
    EVENT_VIDEO_COMMENT_NEW = "video_comment_new"
    EVENT_VIDEO_COMMENT_EDIT = "video_comment_edit"
    EVENT_VIDEO_COMMENT_RESTORE = "video_comment_restore"
    EVENT_VIDEO_COMMENT_DELETE = "video_comment_delete"
    EVENT_WALL_POST_NEW = "wall_post_new"
    EVENT_WALL_REPOST = "wall_repost"
    EVENT_WALL_REPLY_NEW = "wall_reply_new"
    EVENT_WALL_REPLY_EDIT = "wall_reply_edit"
    EVENT_WALL_REPLY_RESTORE = "wall_reply_restore"
    EVENT_WALL_REPLY_DELETE = "wall_reply_delete"
    EVENT_BOARD_POST_NEW = "board_post_new"
    EVENT_BOARD_POST_EDIT = "board_post_edit"
    EVENT_BOARD_POST_RESTORE = "board_post_restore"
    EVENT_BOARD_POST_DELETE = "board_post_delete"
    EVENT_MARKET_COMMENT_NEW = "market_comment_new"
    EVENT_MARKET_COMMENT_EDIT = "market_comment_edit"
    EVENT_MARKET_COMMENT_RESTORE = "market_comment_restore"
    EVENT_MARKET_COMMENT_DELETE = "market_comment_delete"
    EVENT_GROUP_LEAVE = "group_leave"
    EVENT_GROUP_JOIN = "group_join"
    EVENT_GROUP_CHANGE_SETTINGS = "group_change_settings"
    EVENT_GROUP_CHANGE_PHOTO = "group_change_photo"
    EVENT_GROUP_OFFICERS_EDIT = "group_officers_edit"
    EVENT_POLL_VOTE_NEW = "poll_vote_new"
    EVENT_USER_BLOCK = "user_block"
    EVENT_USER_UNBLOCK = "user_unblock"
    EVENT_CONFIRMATION = "confirmation"
    TYPES = {
        EVENT_MESSAGE_NEW: objects.Message,
        EVENT_MESSAGE_REPLY: objects.Message,
        EVENT_MESSAGE_EDIT: objects.Message,
        EVENT_MESSAGE_TYPING_STATE: objects.VkObject
    }

    def __init__(self, api):
        self.long_poll_server = LongPollServer()
        self.api = api
        self._get_long_poll_server(api)

    def message_new(self, message):
        pass

    def message_reply(self, message):
        pass

    def _get_long_poll_server(self, failed=0):
        response = getLongPollServer(self.api, group_id=self.api.const["group_id"])

        if response.failed == 2:
            self.long_poll_server.key = response["key"]
        elif response.failed == 3:
            self.long_poll_server.key = response["key"]
            self.long_poll_server.ts = response["ts"]
        else:
            self.long_poll_server.key = response["key"]
            self.long_poll_server.ts = response["ts"]
            self.long_poll_server.server = response["server"]

    def _parse(self, json):
        event_type = json["type"]
        object_of_class = json["object"]
        try:
            self.TYPES[event_type]
        except NameError:
            return False

        def start_event(target, args):
            threading.Thread(target=target, args=(args,)).start()

        if event_type == self.EVENT_MESSAGE_NEW:
            start_event(self.message_new, objects.Message(object_of_class))
        elif event_type == self.EVENT_MESSAGE_REPLY:
            start_event(self.message_reply, objects.Message(object_of_class))
        else:
            print("Unsupported callback event %s" % event_type)
            return False
        return True

    def run(self):
        lps = self.long_poll_server
        while True:
            link = f"{lps.server}?act=a_check&key={lps.key}&ts={lps.ts}&wait=25"
            response = requests.get(link).json()
            if "failed" in response:
                if response["failed"] == 1:
                    lps.ts = response["ts"]
                elif response["failed"] == 2:
                    self._get_long_poll_server(2)
                elif response["failed"] == 3:
                    self._get_long_poll_server(3)
            else:
                lps.ts = response["ts"]
                for event in response["updates"]:
                    self._parse(event)


class LongPollServer:
    __slots__ = {
        "key", "ts", "server"
    }
