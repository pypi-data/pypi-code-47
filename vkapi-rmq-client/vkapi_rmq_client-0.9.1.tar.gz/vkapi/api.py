
class API:
    def __init__(self, session):
        """

        :param session: vkapi.session.VKRabbitMQSession instance
        """
        self._session = session

    @property
    def version(self):
        return self._session.api_version

    def __getattr__(self, method_name):
        return Request(session=self._session,
                       method_name=method_name)


class Request(object):
    __slots__ = ('_session', '_method_name', '_method_args', 'priority')

    def __init__(self, session, method_name):
        """
        :param session: vkapi.session.VKSession instance
        :param method_name: str: method name
        """
        self._session = session
        self._method_name = method_name
        self._method_args = None  # will be set with __call__ execution
        self.priority = None

    @property
    def method_name(self):
        return self._method_name

    @method_name.setter
    def method_name(self, val):
        raise AttributeError('method_name is immutable')

    @property
    def method_args(self):
        return self._method_args

    @method_args.setter
    def method_args(self, val):
        raise AttributeError('method_args is immutable')

    def __getattr__(self, method_name):
        self._method_name = f'{self._method_name}.{method_name}'
        return self

    def __call__(self, **method_args):
        self.priority = method_args.pop('req_priority', None)
        self._method_args = method_args
        return self._session.make_request(request=self)

    def __repr__(self):  # pragma: no cover
        return "%s(method='%s', args=%s)" % (
            self.__class__.__name__,
            self.method_name,
            self.method_args)
