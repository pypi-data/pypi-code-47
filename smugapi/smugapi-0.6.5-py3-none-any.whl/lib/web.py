

from webpreview import web_preview


def fetch_preview(url, timeout=2):
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
            }

    title, description, image = web_preview(
            url,
            timeout=timeout,
            headers=headers )

    return dict(
        title = title,
        descr = description,
        img = image
        )


