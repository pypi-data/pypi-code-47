from rest_framework.request import Request as _Request


class Request(_Request):

    @property
    def user(self):
        return super(Request, self).user

    @user.setter
    def user(self, value):
        from orm88 import ORM88
        if value.is_authenticated:
            value = ORM88('auth.User').get(id=value.id)
            value.is_authenticated = True
        self._user = value
        self._request.user = value
