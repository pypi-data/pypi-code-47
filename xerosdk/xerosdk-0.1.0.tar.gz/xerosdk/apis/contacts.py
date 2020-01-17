"""
Xero Contacts API
"""

from .api_base import ApiBase


class Contacts(ApiBase):
    """
    Class for Contacts API
    """

    GET_CONTACTS = "/api.xro/2.0/contacts"

    def get_all(self):
        """
        Get all contacts

        Returns:
            List of all contacts
        """

        return self._get_request(Contacts.GET_CONTACTS)
