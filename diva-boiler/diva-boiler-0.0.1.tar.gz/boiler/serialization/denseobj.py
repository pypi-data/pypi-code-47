"""
python object serialization for boiler models, mostly for debugging and
console logging purposes.  If you find yourself writing tools to parse
these, we should stop and evaluate why.
"""
from typing import Callable

from boiler.models import Activity, Actor, Detection


def serialize_detection(detection: Detection):
    arr = [detection.frame, detection.box]
    if detection.keyframe:
        arr.append('keyframe')
    return arr


def serialize_actor(actor: Actor, detection_serializer: Callable = serialize_detection):
    return {
        'type': actor.actor_type,
        'range': [actor.begin, actor.end],
        'detections': [detection_serializer(d) for d in actor.detections],
    }


def serialize_activity(
    activity: Activity,
    actor_serializer: Callable = serialize_actor,
    detection_serializer: Callable = serialize_detection,
):
    return {
        'type': activity.activity_type,
        'range': [activity.begin, activity.end],
        'actors': [
            actor_serializer(a, detection_serializer=serialize_detection) for a in activity.actors
        ],
    }


def _serialize_error(err):
    e = err
    ret = []
    while e:
        ret.append(str(e))
        e = e.__cause__
    return ret


def serialize_validation_errors(fatals):
    output = []
    for fatal in fatals:
        output.append(_serialize_error(fatal))
    return [' '.join(errs) for errs in output]
