"""
These models only provide the necessary properties for ingesting, exporting,
and validation of diva annotations for a SINGLE clip.  They are not intended
to map directly to stumpf models.

They are only useful internally to this library, and are intended as a
translation layer for data either before or after it exists within the stumpf
system.
"""

from itertools import groupby
from typing import List, NamedTuple, Optional

import attr

from boiler.definitions import ActivityType, ActorType


class Box(NamedTuple):
    left: int
    top: int
    right: int
    bottom: int


@attr.s(auto_attribs=True, kw_only=True)
class Detection:
    frame: int
    box: Optional[Box] = None
    keyframe: bool = False


@attr.s(auto_attribs=True, kw_only=True)
class Actor:
    clip_id: Optional[int] = None
    actor_type: Optional[ActorType] = None
    begin: int = 0
    end: int = 0
    detections: List[Detection] = attr.Factory(list)  # [left, top, right, bottom]

    def sort_detections(self):
        self.detections = sorted(self.detections, key=lambda d: d.frame)


@attr.s(auto_attribs=True, kw_only=True)
class Activity:
    activity_type: ActivityType
    begin: int
    end: int
    clip_id: Optional[int] = None
    status: Optional[str] = None
    actors: List[Actor] = attr.Factory(list)


def summarize_activities(activity_list: List[Activity]):
    def activity_keyfunc(v):
        return v.activity_type

    def actor_keyfunc(v):
        return v.actor_type

    activity_counts = []
    for key1, group1 in groupby(sorted(activity_list, key=activity_keyfunc), key=activity_keyfunc):
        group1_list = list(group1)
        activity_counts.append(
            {
                'name': key1,
                'count': len(group1_list),
                'frame_length_sum': sum([a.end - a.begin for a in group1_list]),
            }
        )

    actors = []
    for act in activity_list:
        for actor in act.actors:
            actors.append(actor)
    actor_counts = []
    for key2, group2 in groupby(sorted(actors, key=actor_keyfunc), key=actor_keyfunc):
        group2_list = list(group2)
        actor_counts.append(
            {
                'name': key2,
                'count': len(group2_list),
                'frame_length_sum': sum([a.end - a.begin for a in group2_list]),
            }
        )

    return {
        'activities': {'count': len(activity_list), 'by_type': activity_counts,},
        'actors': {'count': len(actors), 'by_type': actor_counts},
    }
