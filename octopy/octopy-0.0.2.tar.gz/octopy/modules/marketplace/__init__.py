from octopy import request, model


class MarketPlace:

    """
    Official GITHUB documentation: https://developer.github.com/v3/apps/marketplace/#list-all-github-accounts-user-or-organization-on-a-specific-plan
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/MarketPlace.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def plans(self, page=1, stubbed=False):
        """
        Returns all plans for your marketplace listing.

        :kwarg page: from which page, results to be returned.
        :kwarg stubbed: specifies the endpoint
        """
        url = f"{self._url}/marketplace_listing/{'stubbed/plans' if stubbed else 'plans'}?page={page}"
        items = [
            model.create_class("Plan", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def accounts(self, plan_id, stubbed=False, page=1, **kwargs):
        """
        Returns all accounts for a specific plan.

        :param plan_id: plan's id
        :kwarg stubbed: if set to true, it will set the endpoint to stubbed
        :kwarg page: from which page, results to be returned
        :kwarg sort: specifies the filed, by which the final result to be sorted
        :kwarg direction: specifies the type of sort, in `asc`, or `desc`
        """
        url = f"{self._url}/marketplace_listing/{'stubbed/plans' if stubbed else 'plans'}/{plan_id}/accounts?page={page}"
        items = [
            model.create_class("Account", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def associated(self, account_id, stubbed=False):
        """
        Checks if a github account is associated with any marketplace listing.

        :param account_id: account's id
        :kwarg stubbed: if set to true, it will set the endpoint to stubbed
        """
        url = f"{self._url}/marketplace_listing/{'stubbed/accounts' if stubbed else 'accounts'}/{account_id}"
        return model.create_class("Associated", request.get(url, headers=self._headers))

    def purchases(self, page=1, stubbed=False):
        """
        Returns all user's marketplace purchases.

        :kwarg page: from which page results to be returned.
        :kwarg stubbed: if set to true, it will set the endpoint to stubbed
        """
        url = f"{self._url}/user/marketplace_purchases{'/stubbed' if stubbed else ''}?page={page}"
        items = [
            model.create_class("Purschase", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items
