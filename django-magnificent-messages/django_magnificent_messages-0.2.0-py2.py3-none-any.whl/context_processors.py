from . import *  # noqa


def django_magnificent_messages(request):
    """
    Pass all messages and notifications into context
    """
    return {
        "dmm": {
            'notifications': {
                'all': notifications.get(request),
                'count': notifications.count(request),
            },
            'messages': {
                'all': messages.all(request),
                'all_count': messages.all_count(request),
                'read': messages.read(request),
                'read_count': messages.read_count(request),
                'unread': messages.unread(request),
                'unread_count': messages.unread_count(request),
                'archived': messages.archived(request),
                'archived_count': messages.archived_count(request),
                'new': messages.new(request),
                'new_count': messages.new_count(request),
                'new_count_update_last_checked': messages.new_count_update_last_checked(request),
            }
        }
    }
