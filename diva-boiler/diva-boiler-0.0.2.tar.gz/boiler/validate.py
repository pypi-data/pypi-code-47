import re
from typing import Callable, List

from boiler.definitions import activity_spec, ActivityType, actor_codes, ActorType
from boiler.models import Activity, Actor, Detection


def validate_activity_actor_types(actor_string: str, activity_type: ActivityType) -> bool:
    if type(activity_type) is not ActivityType:
        raise ValueError('activity type must be instance of ActivityType')
    if type(actor_string) is not str:
        raise ValueError('actor string must be string')
    pattern = activity_spec[activity_type]
    if pattern is not None:
        sorted_actor_string = ''.join(sorted(actor_string))
        pattern = f'^{pattern}$'
        result = re.match(pattern, sorted_actor_string)
        if result is None:
            msg = 'activity spec validation failed for {}: {} found, ' '{} expected'
            raise ValueError(
                msg.format(activity_type.value, sorted_actor_string, activity_spec[activity_type],)
            )
    return True


def validate_detection(detection: Detection):
    """
    * detections have 4 int corners
    * detection: top < bottom, left < right
    * frame is int
    * keyframe is bool
    """
    box = detection.box
    assert len(box.as_array()) == 4, 'detection box should have 4 corners'
    for value in box.as_array():
        if type(value) is not int:
            raise ValueError(f'element {value} of detection box should be integer')
    assert type(detection.frame) is int, 'frame should be integer'
    assert (
        type(detection.keyframe) is bool
    ), f'keyframe should be boolean, found {detection.keyframe}'
    assert box.left < box.right, f'left ({box.left}) should be < right ({box.right})'
    assert box.top < box.bottom, f'top ({box.top}) should be < bottom ({box.bottom})'


def validate_actor(actor: Actor, detection_validator: Callable = validate_detection):
    """
    * all detections are within actor's timerange
    * actor's type is valid
    * there are <= 1 detection per frame
    * bonus: verify keyframes are real
    """
    for detection in actor.detections:
        try:
            detection_validator(detection)
        except (ValueError, AssertionError) as err:
            raise ValueError('detection_frame={}'.format(detection.frame)) from err
        assert (
            actor.begin <= detection.frame <= actor.end
        ), 'detection outside of actor timerange [{}, {}], {}'.format(
            actor.begin, actor.end, detection.frame
        )
    assert (
        ActorType(actor.actor_type) is not None
    ), f'actor should have valid type: {actor.actor_type}'
    assert len(actor.detections) >= 2, 'actor must have at least a start and end frame'
    failed_frame = actor.prune(check=True)
    assert failed_frame < 0, f'frame={failed_frame} interpolation detected on keyframe'
    assert actor.detections[0].frame == actor.begin, 'actor must have detection for begin frame'
    assert actor.detections[0].keyframe, 'begin frame must be keyframe'
    assert actor.detections[-1].frame == actor.end, 'actor must have frame for end frame'
    assert actor.detections[-1].keyframe, 'end frame must be keyframe'


def validate_activity(
    activity: Activity,
    actor_validator: Callable = validate_actor,
    detection_validator: Callable = validate_detection,
):
    """
    * activity type is valid
    * actors involved are appropriate for activity type
    * actors framerange is within activity framerange
    """
    actor_string = ''
    activity_type = ActivityType(activity.activity_type)
    for actor in activity.actors:
        try:
            actor_validator(actor, detection_validator=detection_validator)
        except (ValueError, AssertionError) as err:
            raise ValueError('actor_id={}'.format(actor.clip_id)) from err
        actor_type = ActorType(actor.actor_type)
        actor_string += actor_codes[actor_type]
        assert activity.begin <= actor.begin <= activity.end, 'actor must begin in range'
        assert activity.begin <= actor.end <= activity.end, 'actor must end in range'
    validate_activity_actor_types(actor_string, activity_type)


def validate_activities(
    activity_list,
    activity_validator: Callable = validate_activity,
    actor_validator: Callable = validate_actor,
    detection_validator: Callable = validate_detection,
):
    fatals: List[Exception] = []
    if len(activity_list) == 0:
        fatals += [ValueError('found activities to validate')]
    for activity in activity_list:
        try:
            activity_validator(
                activity, actor_validator=actor_validator, detection_validator=detection_validator,
            )
        except (ValueError, AssertionError) as err:
            new_err = ValueError('activity_id={}'.format(activity.clip_id))
            new_err.__cause__ = err
            fatals += [new_err]
    return fatals
