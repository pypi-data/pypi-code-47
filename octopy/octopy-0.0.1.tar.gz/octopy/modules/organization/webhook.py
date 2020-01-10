from octopy import request, model


class Webhook:

    """
    Official GITHUB documentation: https://developer.github.com/v3/orgs/members/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Organizations-Members.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, org, page=1):
        """
        Returns all hooks for an org.

        :param org: org's name
        :kwarg page: from which page hooks to be returned, default: 1
        """
        url = f"{self._url}/orgs/{org}/hooks?page={page}"
        items = [
            model.create_class("Hook", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, org, hook_id):
        """
        Get a single hook.

        :param org: org's name
        :param hook_id: hook's id
        """
        url = f"{self._url}/orgs/{org}/hooks/{hook_id}"
        return model.create_class("Hook", request.get(url, headers=self._headers))

    def create(self, org, **kwargs):
        """
        Creates a hook.

        :param org: org's name
        :kwarg name: [required] must be passed as `web`.
        :kwarg config: provides settings for this webhook
            :kwarg url: [required] url to which payloads will be delivered
            :kwarg content_type: media type used to serialize payloads
            :kwarg secret: If provided, the secret will be used as 
                the key to generate the HMAC 
                hex digest value in the X-Hub-Signature header.
            :kwarg insecure_ssl: Determines whether the SSL certificate of 
                the host for url will be verified when delivering 
                payloads. Supported values include 0 
                (verification is performed) and 1 
                (verification is not performed). 
                The default is 0. We strongly recommend not 
                setting this to 1 as you are subject to man-in-the-middle 
                and other attacks.
        :kwarg events: determines what events this hook is triggered for
        :kwarg active: determines if notifications are sent when the webhook is triggered.
            Default: true
        """
        url = f"{self._url}/orgs/{org}/hooks"
        return model.create_class(
            "Hook", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, org, hook_id, **kwargs):
        """
        Updates a hook.

        :param org: org's name
        :param hook_id: hook's id
        :kwarg config: provides settings for this webhook
            :kwarg url: [required] url to which payloads will be delivered
            :kwarg content_type: media type used to serialize payloads
            :kwarg secret: If provided, the secret will be used as 
                the key to generate the HMAC 
                hex digest value in the X-Hub-Signature header.
            :kwarg insecure_ssl: Determines whether the SSL certificate of 
                the host for url will be verified when delivering 
                payloads. Supported values include 0 
                (verification is performed) and 1 
                (verification is not performed). 
                The default is 0. We strongly recommend not 
                setting this to 1 as you are subject to man-in-the-middle 
                and other attacks.
        :kwarg events: determines what events this hook is triggered for
        :kwarg active: determines if notifications are sent when the webhook is triggered.
            Default: true
        """
        url = f"{self._url}/orgs/{org}/hooks/{hook_id}"
        return model.create_class(
            "Hook", request.patch(url, headers=self._headers, params=kwargs)
        )

    def ping(self, org, hook_id):
        """
        Triggers a ping event.

        :param org: org's name
        :param hook_id: hook's id
        """
        url = f"{self._url}/orgs/{org}/hooks/{hook_id}/pings"
        return model.create_class("Status", request.post(url, headers=self._headers))

    def remove(self, org, hook_id):
        """
        Removes a hook.

        :param org: org's name
        :param hook_id: hook's id
        """
        url = f"{self._url}/orgs/{org}/hooks/{hook_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
