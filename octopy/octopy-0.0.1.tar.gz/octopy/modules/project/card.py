from octopy import request, model


class Card:

    """
    Official GITHUB documentation: https://developer.github.com/v3/projects/cards/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Project-Cards.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def all(self, column_id, page=1, **kwargs):
        """
        Returns all project cards.

        :param column_id: column's id
        :kwarg page: from which page, cards to be returned, default: 1
        :kwarg archived_state: Filters the project cards that are returned 
            by the card's state. Can be one of all, archived, 
            or not_archived. Default: not_archived
        """
        url = f"{self._url}/projects/columns/{column_id}/cards?page={page}"
        items = [
            model.create_class("Card", item)
            for item in request.get(url, headers=self._headers, params=kwargs)
        ]
        return items

    def get(self, card_id):
        """
        Returns a single card.

        :param card_id: card's id
        """
        url = f"{self._url}/projects/columns/cards/{card_id}"
        return model.create_class("Card", request.get(url, headers=self._headers))

    def create(self, column_id, **kwargs):
        """
        Creates a card.

        :param column_id: column's id
        :kwarg note: cord's note content
        :kwarg content_id: issue or pull request you want to associate with 
            given card
        :kwarg content_type: [required if content_id] type of content
        """
        url = f"{self._url}/projects/columns/{column_id}/cards"
        return model.create_class(
            "Card", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, card_id, **kwargs):
        """
        Updates a card.

        :param card_id: card's id
        :kwarg note: card's note content
        :kwarg archived: Use true to archive a project card. 
            Specify false if you need to restore a previously archived project card.
        """
        url = f"{self._url}/projects/columns/cards/{card_id}"
        return model.create_class(
            "Card", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, card_id):
        """
        Deletes a card.

        :param card_id: card's id
        """
        url = f"{self._url}/projects/columns/cards/{card_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def move(self, card_id, **kwargs):
        """
        Moves a card.

        :param card_id: card's id
        :kwarg position: [required] Can be one of top, 
            bottom, or after:<card_id>, 
            where <card_id> is the id value of a card in
             the same column, or in the new column specified by column_id.
        :kwarg column_id: The id value of a column in the same project.
        """
        url = f"{self._url}/projects/columns/cards/{card_id}/moves"
        return model.create_class(
            "Status", request.post(url, headers=self._headers, params=kwargs)
        )
