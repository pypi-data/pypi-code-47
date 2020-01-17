"""
KW18 is a csv-type format consisting of 3 files.
A row schema for each file is defined below.
[?] indicates an un-used row field.

file.txt: contains activity information.
[?] [1:ACTIVITY_TYPE_CODE] [2:ACTIVITY_ID] [?] [4:BEGIN]
[?] [6:END] [?] [?] [?] [?] [?] [12:N_PARTICIPANTS]
[ACTOR1_ID] [ACTOR2_ID] ...
[?] [ACTOR1_BEIGN] [?] [ACTOR1_END] [?] [ACTOR2_BEIGN] [?] [ACTOR2_END] ...

file.kw18: contains geometry information
[0:actor_id] [1:actor_track_length] [2:frame]
[?] [?] [?] [?] [?] [?] [9:top_left_x] [10:top_left_y] [11:bottom_right_x] [12:bottom_right_y]

file.kw18.types: contains actor type information
[0:ACTOR_ID] [1:ACTOR_TYPE]
"""
import csv
from typing import List

from boiler.definitions import ActivityType, all_activity_codes
from boiler.models import Activity, Actor, Box, Detection


def _deserialize_actor(row, n_participants, i, activity_begin, activity_end, actor_map):
    actor_id = int(row[13 + i])
    if n_participants == 1:
        actor_begin = activity_begin
        actor_end = activity_end
    elif n_participants > 1:
        actor_start_i = 13 + n_participants + (i * 4)
        actor_begin = int(row[actor_start_i + 1])
        actor_end = int(row[actor_start_i + 3])

    actor = Actor()
    if actor_id in actor_map:
        actor = actor_map[actor_id]
    actor.begin = actor_begin
    actor.end = actor_end
    actor.clip_id = actor_id
    actor_map[actor_id] = actor
    return actor


def deserialize_activities(file, activity_map, actor_map):
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        try:
            activity_type_code = int(row[1])
            activity_id = int(row[2])
            activity_begin = int(row[4])
            activity_end = int(row[6])
            n_participants = int(row[12])
            activity_type = all_activity_codes[activity_type_code]
            activity = Activity(
                activity_type=activity_type.value,
                begin=activity_begin,
                end=activity_end,
                clip_id=activity_id,
                actors=[
                    _deserialize_actor(
                        row, n_participants, i, activity_begin, activity_end, actor_map
                    )
                    for i in range(n_participants)
                ],
            )
            activity_map[activity_id] = activity
        except ValueError:
            continue


def deserialize_geom(file, actor_map):
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        try:
            actor_id = int(row[0])
            frame = int(row[2])
            box = [int(c) for c in row[9:13]]
            box = Box(left=box[0], top=box[1], right=box[2], bottom=box[3])
            keyframe = True  # TODO: how to detect?
            detection = Detection(frame=frame, box=box, keyframe=keyframe)
            if actor_id in actor_map:
                actor_map[actor_id].detections.append(detection)
            else:
                actor_map[actor_id] = Actor(clip_id=actor_id, detections=[detection])
        except ValueError:
            continue

    for actor in actor_map.values():
        actor.sort_detections()


def deserialize_types(file, actor_map):
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        actor_id = int(row[0])
        actor_type: str = row[1]
        if actor_id in actor_map:
            actor_map[actor_id].actor_type = actor_type
        else:
            actor_map[actor_id] = Actor(clip_id=actor_id, actor_type=actor_type)


def find_activity_code(activity_name: str):
    target_activity = ActivityType(activity_name)
    for code, activity in all_activity_codes.items():
        if activity == target_activity:
            return code
    raise ValueError(f'no numerical code exists for {target_activity}')


def serialize_types(actor_list: List[Actor]):
    for actor in actor_list:
        row = [actor.clip_id, actor.actor_type]
        yield ' '.join([str(d) for d in row]) + '\n'


def serialize_activities(activity_list: List[Activity], filler_char):
    for activity in activity_list:
        row = [
            filler_char,
            find_activity_code(activity.activity_type),
            activity.clip_id,
            filler_char,
            activity.begin,
            activity.end,
            filler_char,
            filler_char,
            filler_char,
            filler_char,
            filler_char,
            len(activity.actors),
        ]
        for actor in activity.actors:
            row.append(actor.clip_id)
        if len(activity.actors) > 1:
            for actor in activity.actors:
                row += [filler_char, actor.begin, filler_char, actor.end]
        yield ' '.join([str(d) for d in row]) + '\n'


def serialize_geom(actor_list: List[Actor], filler_char, keyframes_only=False):
    for actor in actor_list:
        for detection in actor.detections:
            if not keyframes_only or detection.keyframe:
                row = [
                    actor.clip_id,
                    actor.end - actor.begin,
                    detection.frame,
                    filler_char,
                    filler_char,
                    filler_char,
                    filler_char,
                    filler_char,
                    filler_char,
                ]
                row += detection.box.as_array()
                yield ' '.join([str(d) for d in row]) + '\n'


def serialize_to_files(
    output_basename: str,
    activity_list: List[Activity],
    actor_list: List[Actor],
    keyframes_only=False,
    filler_char='0',
):
    with open(output_basename + '.txt', 'w', encoding='utf-8') as yamlfile:
        for line in serialize_activities(activity_list, filler_char):
            yamlfile.write(line)
    with open(output_basename + '.kw18.types', 'w', encoding='utf-8') as yamlfile:
        for line in serialize_types(actor_list):
            yamlfile.write(line)
    with open(output_basename + '.kw18', 'w', encoding='utf-8') as yamlfile:
        for line in serialize_geom(actor_list, filler_char, keyframes_only=keyframes_only):
            yamlfile.write(line)
