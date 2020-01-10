from octopy import request, model


class Column:

    """
    Official GITHUB documentation: https://developer.github.com/v3/projects/columns/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Project-Columns.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers.copy()
        self._headers["Accept"] = "application/vnd.github.inertia-preview+json"

    def all(self, project_id, page=1):
        """
        Returns all columns of a project.

        :param project_id: project's id
        :kwarg page: from which page, columns to be returned, default: 1
        """
        url = f"{self._url}/projects/{project_id}/columns?page={page}"
        items = [
            model.create_class("ProjectColumn", item)
            for item in request.get(url, headers=self._headers)
        ]
        return items

    def get(self, column_id):
        """
        Returns a single column.

        :param column_id: column's id
        """
        url = f"{self._url}/projects/columns/{column_id}"
        return model.create_class(
            "ProjectColumn", request.get(url, headers=self._headers)
        )

    def create(self, project_id, **kwargs):
        """
        Creates a column.

        :param project_id: project's id
        :kwarg name: [required] column's name
        """
        url = f"{self._url}/projects/{project_id}/columns"
        return model.create_class(
            "ProjectColumn", request.post(url, headers=self._headers, params=kwargs)
        )

    def update(self, column_id, **kwargs):
        """
        Updates a column.

        :param column_id: column's id
        :kwarg name: [required] column's name
        """
        url = f"{self._url}/projects/columns/{column_id}"
        return model.create_class(
            "ProjectColumn", request.patch(url, headers=self._headers, params=kwargs)
        )

    def remove(self, column_id):
        """
        Deletes a column.

        :param column_id: column's id
        """
        url = f"{self._url}/projects/columns/{column_id}"
        return model.create_class("Status", request.delete(url, headers=self._headers))

    def move(self, column_id, **kwargs):
        """
        Moves a column.

        :param column_id: column's id
        :kwarg position: [required]
            Can be one of first, last, or after:<column_id>, 
            where <column_id> is the id value of a column in the same project.
        """
        url = f"{self._url}/projects/columns/{column_id}/moves"
        return model.create_class(
            "Status", request.post(url, headers=self._headers, params=kwargs)
        )
