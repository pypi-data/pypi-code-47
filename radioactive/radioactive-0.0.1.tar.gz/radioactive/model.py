import collections


class Dict:

    def __init__(self, *args, **kwargs):
        if args:
            assert len(args) == 1
            data = dict(args[0])
            data.update(kwargs)
        else:
            data = kwargs
        self._data = data
        self._listeners = collections.defaultdict(set)

    def subscribe(self, key, listener):
        self._listeners[key].add(listener)

    def unsubscribe(self, key, listener):
        self._listeners[key].remove(listener)

    def emit(self, key, value):
        for listener in self._listeners.get(key, ()):
            try:
                listener(self, key, value)
            except Exception as error:
                print(f'Error in listener: {error!r}')

    def __setitem__(self, key, value):
        self._data[key] = value
        self.emit(key, value)

    def update(self, other):
        self._data.update(other)
        for key, value in other.items():
            self.emit(key, value)

    def __getitem__(self, key):
        return self._data[key]

    def get(self, key, default=None):
        return self._data.get(key, default)

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()


def demo():
    state = Dict(name='foo', version='1.2.3')

    CB = []
    def cb(model, key, value):
        print(f'model[{key}] = {value}')
        CB.append(1)
    state.observe('name', cb)

    state['name'] = 'bar'
    assert len(CB) == 1


if __name__ == '__main__':
    demo()

