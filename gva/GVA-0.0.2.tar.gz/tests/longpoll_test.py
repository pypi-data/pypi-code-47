from gva.longPoll import LongPoll


class LongPollTest(LongPoll):
    def message_new(self, message):
        print("MESSAGE NEW: %s" % message.text)
