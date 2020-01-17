"""
These models only provide the necessary properties for ingesting, exporting,
and validation of diva annotations for a SINGLE clip.  They are not intended
to map directly to stumpf models.

They are only useful internally to this library, and are intended as a
translation layer for data either before or after it exists within the stumpf
system.
"""
from typing import List, Optional

import attr


def interpolate_point(a, b, delta):
    return round(((1 - delta) * a) + (delta * b))


@attr.s(auto_attribs=True, kw_only=True)
class Box:
    left: int = 0
    top: int = 0
    right: int = 0
    bottom: int = 0

    def interpolate(self, other: 'Box', distance: float) -> 'Box':
        left = interpolate_point(self.left, other.left, distance)
        top = interpolate_point(self.top, other.top, distance)
        right = interpolate_point(self.right, other.right, distance)
        bottom = interpolate_point(self.bottom, other.bottom, distance)
        return Box(left=left, top=top, right=right, bottom=bottom)

    def as_array(self) -> List[int]:
        return [self.left, self.top, self.right, self.bottom]

    def equals(self, other: 'Box') -> bool:
        return all([a == b for a, b in zip(self.as_array(), other.as_array())])


@attr.s(auto_attribs=True, kw_only=True)
class Detection:
    frame: int
    box: Box = attr.Factory(Box)
    keyframe: bool = False

    def interpolate(self, other: 'Detection', frame: int) -> 'Detection':
        distance = (frame - self.frame) / (other.frame - self.frame)
        box = self.box.interpolate(other.box, distance)
        return Detection(frame=frame, box=box, keyframe=False)

    def equals(self, other: 'Detection'):
        return self.frame == other.frame and self.box.equals(other.box)


@attr.s(auto_attribs=True, kw_only=True)
class Actor:
    clip_id: Optional[int] = None
    actor_type: str = ''
    begin: int = 0
    end: int = 0
    detections: List[Detection] = attr.Factory(list)

    def sort_detections(self):
        self.detections = sorted(self.detections, key=lambda d: d.frame)

    def prune(self, check=False):
        def get_next_keyframe(arr: List[Detection]) -> Detection:
            for d in arr:
                if d.keyframe:
                    return d
            raise ValueError('There are frames after the final keyframe!')

        while True:
            pruned = []
            last_keyframe: Detection = self.detections[0]
            next_keyframe: Detection = get_next_keyframe(self.detections[1:])
            for i, d in enumerate(self.detections):
                if i == 0 or i == len(self.detections) - 1:
                    continue
                if next_keyframe.frame <= d.frame:
                    next_keyframe = get_next_keyframe(self.detections[(i + 1) :])  # noqa: E203
                intp = last_keyframe.interpolate(next_keyframe, d.frame)
                is_keyframe = not intp.equals(d)
                if not is_keyframe and d.keyframe:
                    if check:
                        return d.frame  # check has failed
                    d.keyframe = False
                    pruned.append(d)
                if d.keyframe:
                    last_keyframe = d
            if len(pruned) == 0:
                break
        return -1


@attr.s(auto_attribs=True, kw_only=True)
class Activity:
    activity_type: str
    begin: int
    end: int
    clip_id: Optional[int] = None
    status: Optional[str] = None
    actors: List[Actor] = attr.Factory(list)

    def prune(self):
        [a.prune() for a in self.actors]
