from twitter_ads_v2.base import Base


class Client(Base):
    """
    The Ads API Client class which functions as a container for basic
    API consumer information.
    """

    def __init__(
        self,
        account_id,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
        **kwargs
    ):
        """
        Creates a new Ads API client instance.

        ..seealso:: :doc:`/examples/quick_start.py`
        """
        self._account_id = account_id
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token = access_token
        self._access_token_secret = access_token_secret
        self._options = kwargs.get('options', {})

    def __repr__(self):
        return '<{name} object at {mem} consumer_key={key}>'.format(
            name=self.__class__.__name__,
            mem=hex(id(self)),
            key=getattr(self, 'consumer_key')
        )

    @property
    def options(self):
        """Returns the options value."""
        return self._options

    @property
    def account_id(self):
        """Returns the account_id."""
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Set the account_id."""
        self._account_id = account_id

    @property
    def consumer_key(self):
        """Returns the consumer_key value."""
        return self._consumer_key

    @property
    def consumer_secret(self):
        """Returns the consumer_secret value."""
        return self._consumer_secret

    @property
    def access_token(self):
        """Returns the access_token value."""
        return self._access_token

    @property
    def access_token_secret(self):
        """Returns the access_token_secret value."""
        return self._access_token_secret

    def sandbox():
        """Enables and disables sandbox mode."""
        def fget(self):
            return self._options.get('sandbox', None)

        def fset(self, value):
            self._options['sandbox'] = value

        return locals()

    sandbox = property(**sandbox())

    def trace():
        """Enables and disables request tracing."""
        def fget(self):
            return self._options.get('trace', None)

        def fset(self, value):
            self._options['trace'] = value

        return locals()

    trace = property(**trace())
