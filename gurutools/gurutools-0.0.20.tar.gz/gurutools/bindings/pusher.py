from celery import shared_task
from .settings import PUSHER_QUEUE

@shared_task(name='pusher.push_to_pubnub')
def push_to_pubnub(channel, message):
    """

### Example usage:

```
from gurutools.bindings.pusher import delegate_push

delegate_push(
    method = "push_to_pubnub",
    args = (channel, content),
    version = "1"
```
    """
    pass

@shared_task(name='pusher.push_to_stream')
def push_to_stream(collection, serialized_object, verb, actor_id = None, custom_message = None, extra_data = {}, enrich = True, *args, **kwargs):
    """
### Basic usage:
push_to_stream(
    'appointmentview',
    serialized_data,
    verb = 'toggle_calendar',
    custom_message='Turned calendar on for view "My View"'
)
    """
    pass


PUSH_MAP = {
    # version 1:
    "1": {
        "push_to_pubnub": push_to_pubnub,
        "push_to_stream": push_to_stream
    }
}


def delegate_push(method_name, args, kwargs={}, version = "1"):
    print(method_name, args, kwargs, version)
    method_to_call = PUSH_MAP.get(version).get(method_name)
    return method_to_call.apply_async(
        args,
        kwargs,
        queue=PUSHER_QUEUE,
        serializer='json'
    )

def activity_update(actor_id, feed, verb, context, message):
    """
context = {'is_calendar': False, 'owner': 1, 'title': 'My view', 'auto_reports_schedule': None, 'type': 'personal', 'auto_invoice_schedule': None, 'serializer': 'schedule.v3.serializers.list.AppointmentListSerializer', 'practitioners': [1,125], 'id': 11, 'modified_date': '2019-11-16T02:05:46.270752Z', 'created_date': '2019-11-16T02:05:46.270675Z', 'filters': {}, 'description': None, 'spaces': [9], 'auto_invoice': False, 'auto_reports': False}
activity_update(1, 'appointmentview', 'toggle_calendar', context, 'toggling the calendar')
    """
    args = (feed, context)
    kwargs = {
        "actor_id": actor_id,
        "verb":verb,
        "custom_message":message
    }
    delegate_push("push_to_stream", args, kwargs, version="1")
