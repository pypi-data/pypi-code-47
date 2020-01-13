from octopy import request, model


class Email:

    """
    Official GITHUB documentation: 
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Users.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def mine(self, public=False, page=1):
        """
        Returns currently authenticated user's email.

        :kwarg public: if set to true, it will return only publicly visible emails.
        :kwarg page: from which page emails to be returned
        """
        url = f"{self._url}/user{'/public_emails' if public else '/emails'}?page={page}"
        items = [
            model.create_class("Email", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def create(self, **kwargs):
        """
        Adds another email.

        :kwarg emails: list with emails to be added.
        """
        url = f"{self._url}/user/emails"
        items = [
            model.create_class("Email", item)
            for item in request.post(url, headers=self._headers, params=kwargs)
        ]
        return items

    def remove(self, **kwargs):
        """
        Removes (an email|emails) from currently authenticated user.

        :kwarg emails: list with emails to be removed
        """
        url = f"{self._url}/user/emails"
        return model.create_class(
            "Status", request.delete(url, headers=self._headers, params=kwargs)
        )

    def toggle(self, **kwargs):
        """
        Toggles primary email visibility.

        :kwarg email: [required] specifies the email, which visibility needs a change
        :kwarg visibility: [required] specifies the type of visibility; can be public,
            or private
        """
        url = f"{self._url}/user/email/visibility"
        return model.create_class(
            "Email", request.patch(url, headers=self._headers, params=kwargs)
        )
