from django.utils.http import urlencode


# region btc-simple-wizard URL encoding features

def add_extra_params_to_url(url: str, extra_params: dict) -> str:
    """
    Prepares url with extra parameters
    """

    encoded_redirect_params = urlencode(extra_params, doseq=True)
    url = f'{url}?{encoded_redirect_params}'

    return url

# endregion
