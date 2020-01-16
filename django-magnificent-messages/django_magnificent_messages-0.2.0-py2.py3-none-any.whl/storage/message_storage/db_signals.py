from django.dispatch import Signal

message_sent = Signal(providing_args=["message"])
message_read = Signal(providing_args=["message", "user"])
message_unread = Signal(providing_args=["message", "user"])
message_archived = Signal(providing_args=["message", "user"])
message_unarchived = Signal(providing_args=["message", "user"])
