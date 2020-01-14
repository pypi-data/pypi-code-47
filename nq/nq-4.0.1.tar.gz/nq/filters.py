class _ParameterStore:
    def __init__(self, key, value, depth, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs
        self.key = key
        self.value = value
        self.depth = depth
        for key, value in self.__kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, key):
        return self.__args[key]


def _forward_args_and_call(f1, f2, p):
    return (f.check_filter(p.key, p.value, p.depth) for f in [f1, f2])


class Filter:
    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.args = []
        self.kwargs = {}

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self

    def __and__(self, f):
        return Filter(
            lambda p: all(_forward_args_and_call(self, f, p)), f"{self.name} & {f.name}"
        )

    def __or__(self, f):
        return Filter(
            lambda p: any(_forward_args_and_call(self, f, p)), f"{self.name} | {f.name}"
        )

    def check_filter(self, key, value, depth):
        all_args = _ParameterStore(key, value, depth, *self.args, **self.kwargs)
        return self.func(all_args)

    def __repr__(self):
        return f"{self.name}({self.args}, {self.kwargs})"


def make_filter(func):
    def make_filter_wrapper(*fargs, **fkwargs):
        new_filter = Filter(func, func.__name__)
        new_filter(*fargs, **fkwargs)
        return new_filter

    return make_filter_wrapper


@make_filter
def get_all(box):
    return True


@make_filter
def get_index(box):
    return isinstance(box.key, int) and box.key == box[0]


@make_filter
def get_key(box):
    return box.key == box[0]


@make_filter
def get_range(box):
    return isinstance(box.key, int) and box[0] <= box.key < box[1]


@make_filter
def get_multiple(box):
    return box.key in box.args


@make_filter
def contains_attribute(box):
    return box[0] in box.value


@make_filter
def when_attribute(box):
    if not box[0] in box.value:
        return False
    if hasattr(box, "equals"):
        return box.value[box[0]] == box.equals
    elif hasattr(box, "greater_than"):
        return box.value[box[0]] > box.greater_than
    elif hasattr(box, "lesser_than"):
        return box.value[box[0]] < box.lesser_than
    elif hasattr(box, "check"):
        return box.check(box.value[box[0]])
