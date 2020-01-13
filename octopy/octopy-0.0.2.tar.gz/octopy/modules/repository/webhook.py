from octopy import request, model


class Webhook:

    """
    Official GITHUB documentation: https://developer.github.com/v3/repos/hooks/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Repository-Hook
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, owner, repo, page=1):
        """
        Returns all hooks for a repisitory.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page hooks to be retuend; default: 1
        """
        url = f"{self._url}/repos/{owner}/{repo}/hooks?page={page}"
        items = [
            model.create_class("Webhook", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, owner, repo, hook_id):
        """
        Returns a single hook.

        :param owner: owner's name
        :param repo: repo's name
        :param hook_id: hook's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}"
        return model.create_class("Webhook", request.get(url, headers=self._headers))

    def create(self, owner, repo, **kwargs):
        """
        Creates a hook.

        :param owner: owner's name
        :param repo: repo's name
        :kwarg name: Use web to create a webhook. 
            Default: web. This parameter only accepts the value web.
        :kwarg config: [required] key/value pairs to provide settins for this hook
            :kwarg url: [required] url to which the payloads will be delivered
            :kwarg content_type: media type used to serialize the payloads
            :kwarg secret: If provided, the secret will be used 
                as the key to generate the HMAC hex digest 
                value in the X-Hub-Signature header.
            :kwarg insecure_ssl: Determines whether 
                the SSL certificate of the host for url 
                will be verified when delivering payloads.
        :kwarg events: determines what events the hook is triggered for; default: ["push"]
        :kwarg active: determines if notifications are sent when the webhook is triggered; default: true
        """
        url = f"{self._url}/repos/{owner}/{repo}/hooks"
        return model.create_class(
            "Webhook", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, owner, repo, hook_id, **kwargs):
        """
        Updates a hook.

        :param owner: owner's name
        :param repo: repo's name
        :param hook_id: hook's id
        :kwarg config:
            :kwarg url:
            :kwarg content_type:
            :kwarg secret:
            :kwarg insecure_ssl:
        :kwarg events:
        :kwarg add_events:
        :kwarg remove_events:
        :kwarg active:
        """
        url = f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}"
        return model.create_class(
            "Webhook", request.patch(url, headers=self._headers, params=kwargs)
        )

    def test(self, owner, repo, hook_id):
        """
        Triggers a hook with the latest push to the current repository.

        :param owner: owner's name
        :param repo: repo's name
        :param hook_id: hook's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}/tests"
        return model.create_class("Status", request.post(url, headers=self._headers))

    def ping(self, owner, repo, hook_id):
        """
        Triggers a ping event to be send to a hook.

        :param owner: owner's name
        :param repo: repo's name
        :param hook_id: hook's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}/pings"
        return model.create_class("Status", request.post(url, headers=self._headers))

    def remove(self, owner, repo, hook_id):
        """
        Deletes a hook.

        :param owner: owner's name
        :param repo: repo's name
        :param hook_id: hook's id
        """
        url = f"{self._url}/repos/{owner}/{repo}/hooks/{hook_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))
