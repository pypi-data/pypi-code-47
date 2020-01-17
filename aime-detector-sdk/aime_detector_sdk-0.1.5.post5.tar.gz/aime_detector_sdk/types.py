from typing import TypeVar


class DetectConfigs:
    def __init__(self, w, h, resize_out_ratio=4.0, threshold_distance=100.0, redzone_threshold_distance=100.0, max_fps=10,
                 delay_detected=0.5, max_miss=3.0):
        self.w = w  # Width of single video frame
        self.h = h  # Height of single video frame
        self.resize_out_ratio = resize_out_ratio
        self.threshold_distance = threshold_distance  # Farthest distance to keep in conversation
        self.redzone_threshold_distance = redzone_threshold_distance  # Farthest distance to start greeting
        self.max_fps = max_fps  # Maximum frame per second to process
        self.max_miss = max_miss  # Maximum time to be wait before terminate the conversation
        self.delay_detected = delay_detected  # Maximum time to be wait before start the conversation


class HumanName(str):  # complex human name other than simple str
    prefix = None
    suffix = None
    attributes = {}

    def get_attr(self, k, default=None):
        return self.attributes.get(k, default)

    def set_attr(self, k, val=None):
        self.attributes[k] = val

    def to_file(self, fd):
        if isinstance(fd, str):
            with open(fd, 'w') as f:
                return self.to_file(f)
        fd.write(self)
        fd.write('\n')
        if self.prefix is not None:
            fd.write(self.prefix)
        fd.write('\n')
        if self.suffix is not None:
            fd.write(self.suffix)
        fd.write('\n')
        for (k, v) in self.attributes.items():
            if v is not None:
                fd.write('{}: {}\n'.format(k, v))

    @staticmethod
    def from_file(fd):
        if isinstance(fd, str):
            with open(fd, 'r') as f:
                return HumanName.from_file(f)
        name = fd.readline().strip()
        suffix = None
        prefix = None
        n_prefix = fd.readline().strip()
        if len(n_prefix) != 0:
            prefix = n_prefix
        n_suffix = fd.readline().strip()
        if len(n_suffix) != 0:
            suffix = n_suffix
        attributes = {}
        for line in fd.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            comps = line.split(':', 1)
            if len(comps) != 2:
                continue
            k = comps[0].strip()
            v = comps[1].strip()
            if k in ['name', 'prefix', 'suffix']:
                if k == 'name':
                    name = v
                elif k == 'prefix':
                    prefix = v
                elif k == 'suffix':
                    suffix = v
                continue
            attributes[k] = v
        name = HumanName(name)
        name.suffix = suffix
        name.prefix = prefix
        name.attributes = attributes
        return name


HumanNameT = TypeVar('HumanNameT', str, HumanName)


class VisionDetectorHuman:
    class FaceBox:
        def __init__(self, left, top, right, bottom):
            self.left = left
            self.top = top
            self.right = right
            self.bottom = bottom

    def __init__(self, id, name: HumanNameT, distance, face_box: FaceBox, portrait=None):
        """
        :type id: ID of detected human
        :type name: Name of detected human. Used in greeting message
        :type distance: Estimated distance from camera to human
        :type face_box: Rectangle coordinate of face in image frame
        :type portrait: Sliced image for human face
        """
        self.id = id
        self.name = name
        self.distance = distance
        self.face_box = face_box
        self.portrait = portrait
        self.fresh = True  # Is this human found in detected frame
        self.timestamp_in_range = None  # First detected timestamp
        self.last_timestamp_in_range = None  # Last detected timestamp

    def get(self, key, default=None):
        return getattr(self, key, default=default)

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        setattr(self, key, value)


class FaceRegisterRequest:
    def __init__(self, name, fullname: HumanNameT = None, instant_register=False):
        self.name = name
        if not fullname:
            fullname = name
        self.fullname = fullname
        self.instant_register = instant_register


class FaceRegisterError(Exception):
    def __init__(self, message='Error occurred'):
        self.message = message
