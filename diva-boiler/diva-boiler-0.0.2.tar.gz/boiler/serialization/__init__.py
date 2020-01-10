from typing import List, Mapping, Tuple

from boiler.models import Activity, Actor
from boiler.serialization import kpf, kw18

serializers = {
    'kpf': kpf,
    'kw18': kw18,
}


def assign_entity_ids(
    activity_list: List[Activity],
) -> Tuple[Mapping[int, Activity], Mapping[int, Actor]]:
    """
    assign clip_id to all activities and actors in
    activity_list, given all actors appear in exactly 1 activity.
    """
    activity_map = {}
    actor_map = {}
    actor_i = 1
    for activity_i, activity in enumerate(activity_list, start=1):
        activity_map[activity_i] = activity
        activity.clip_id = activity_i
        for actor in activity.actors:
            actor_map[actor_i] = actor
            actor.clip_id = actor_i
            actor_i = actor_i + 1
    return (activity_map, actor_map)
