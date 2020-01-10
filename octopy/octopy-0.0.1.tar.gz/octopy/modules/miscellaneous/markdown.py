from octopy import request, model


class Markdown:

    """
    Official GITHUB documentation: https://developer.github.com/v3/markdown/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Miscellaneous-Markdown.md
    """

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def render(self, raw=False, **kwargs):
        """
        Renders an arbirtrary Markdown.

        :kwarg raw:
        :kwarg text: [required] markdown's text for render
        :kwarg mode: rendering mode - can be `markdown`, or `gfm`
        :kwarg context: if `mode` is set to `gfm` set this kwarg to the repository
            context
        """
        url = f"{self._url}/markdown{'/raw' if raw else ''}"
        return model.create_class(
            "Status", request.post(url, headers=self._headers, params=kwargs)
        )
