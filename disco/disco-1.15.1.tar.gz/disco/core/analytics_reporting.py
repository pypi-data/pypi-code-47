"""
Basic Analytics functionality. Exposed `setup_analytics` and `track`
Uses the `python-analytics` package
"""
import json
import os
import uuid

import analytics


def setup_analytics():
    """Sets up analytics tracking"""
    if analytics.write_key:
        return
    if not os.path.exists('.config'):
        return
    with open('.config') as json_file:
        data = json.load(json_file)
        if not data["segment"]:
            return
        analytics.write_key = data["segment"]


def track(event, payload, user_id=str(uuid.uuid4())):
    """Track single event. Refer to `python-analytics` `track` method for more
    info

    Args:
        event:
        payload:
        user_id:
    """
    if analytics.write_key:
        payload["interface"] = "SDK"
        analytics.track(user_id, event, payload)
