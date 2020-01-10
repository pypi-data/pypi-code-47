from octopy import request, model


class Notification:

    """
    Official documentation in Github: https://developer.github.com/v3/activity/notifications/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/ActivityNotifications.md
    """

    def __init__(self, url, headers, **kwargs):
        self._url = url
        self._headers = headers

    def all(self, page=1, **kwargs):
        """
        Returns latest notifications of the current user.

        :kwarg page: from which page results to be returned.
        :kwarg all: shows notifications as read if set to true, the default value is false
        :kwarg participating: shows notifications in which the current user is directly participating, or mentioned,
            if the value is set to true, default is fale
        :kwarg since: shows those notifications updated after the given time, the format is YYYY-MM-DDTHH:MM:SSZ.
        :kwarg before: shows only notifications updated before the given time.
        """
        url = f"{self._url}/notifications?page={page}"
        items = [
            model.create_class("Notification", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def repository(self, owner, repo, page=1, **kwargs):
        """
        Returns all notifications in a repository.
    
        :param owner: owner's name
        :param repo: repo's name
        :kwarg page: from which page results to be returned.
        :kwarg all: shows notifications as read if set to true, the default value is false
        :kwarg participating: shows notifications in which the current user is directly participating, or mentioned,
            if the value is set to true, default is fale
        :kwarg since: shows those notifications updated after the given time, the format is YYYY-MM-DDTHH:MM:SSZ.
        :kwarg before: shows only notifications updated before the given time.
        """
        url = f"{self._url}/repos/{owner}/{repo}/notifications?page={page}"
        items = [
            model.create_class("RepositoryNotification", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def mark_as_read(self, **kwargs):
        """
        Marks notifications as read. 
        From Github's documentation: If the number of notifications is too large to complete 
        in one request, you will receive a 202 Accepted
         status and GitHub will run an asynchronous process 
         to mark notifications as "read." To check whether any 
         "unread" notifications remain, you can use the 
         List your notifications endpoint and pass the query parameter all=false.

        :kwarg owner: if you want to mark notifications from given repository as read, you must set owner, and
            repo as arguments.
        :kwarg repo:
        :kwarg last_read_at: Describes the last point that notifications were checked. 
        """
        if kwargs.get("owner"):
            owner = kwargs.get("owner")
            repo = kwargs.get("repo")
            del kwargs["owner"]
            del kwargs["repo"]
            url = f"{self._url}/repos/{owner}/{repo}/notifications"
        else:
            url = f"{self._url}/notifications"

        return model.create_class(
            "Status", request.put(url, headers=self._headers, params=kwargs)
        )

    def thread(self, thread_id):
        """
        Returns a single thread, specified by the given id.

        :param thread_id: thread's id
        """
        url = f"{self._url}/notifications/threads/{thread_id}"
        return create_class("Thread", request.get(url, headers=self._headers))

    def mark_thread(self, thread_id):
        """
        Mark a thread as read.

        :param thread_id: thread's id
        """
        url = f"{self._url}/notifications/threads/{thread_id}"
        return model.create_class("Status", request.patch(url, headers=self._headers))

    def subscribed(self, thread_id):
        """
        Gets a thread subscription.

        :param thread_id: thread's id
        """
        url = f"{self._url}/notifications/threads/{thread_id}"
        item = model.create_class(
            "Subscription", request.get(url, headers=self._headers)
        )
        return item

    def subscribe(self, thread_id, **kwargs):
        """
        Subscribes/unsubscribes the current user from a conversation.

        :param thread_id: thread's id
        :kwarg ignored: if set to true, will block you from all notifications from this thread.
        """
        url = f"{self._url}/notifications/threads/{thread_id}/subscription"
        return model.create_class(
            "Status", request.put(url, headers=self._headers, params=kwargs)
        )

    def unsubcribe(self, thread_id):
        """
        Mutes notifications from given thread, until you comment or someone mentions you.
        
        :param thread_id: thread's id
        """
        url = f"{self._url}/notifications/threads/{thread_id}/subscription"
        return model.create_class("Status", request.delete(url, headers=self._headers))
