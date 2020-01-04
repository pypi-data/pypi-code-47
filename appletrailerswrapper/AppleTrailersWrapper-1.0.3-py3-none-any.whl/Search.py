import requests


def Search(query: str):
    """
    Searches by given query

    :param query: string
    :return: dict
    :raises: Exception
    :Example JSON Response:
    .. highlight:: json
    .. code-block:: json

        {
           "error":false,
           "results":[
              {
                 "title":"The Divergent Series: Allegiant",
                 "releasedate":"Fri, 18 Mar 2016 00:00:00 -0700",
                 "studio":"Summit Entertainment",
                 "poster":"https:\/\/trailers.apple.com\/trailers\/summit\/thedivergentseriesallegiant\/images\/poster.jpg",
                 "moviesite":"http:\/\/www.thedivergentseries.movie\/#allegiant",
                 "location":"\/trailers\/summit\/thedivergentseriesallegiant\/",
                 "urltype":"html",
                 "director":"a:1:{i:0;s:16:\"Robert Schwentke\";}",
                 "rating":"PG-13",
                 "genre":[
                    "Action and Adventure"
                 ],
                 "actors":false,
                 "trailers":[
                    {
                       "type":"Clip 2",
                       "postdate":"Fri, 18 Mar 2016 00:00:00 -0700",
                       "exclusive":false,
                       "hd":true
                    },
                    {
                       "type":"Clip 1",
                       "postdate":"Tue, 15 Mar 2016 00:00:00 -0700",
                       "exclusive":false,
                       "hd":true
                    },
                    {
                       "type":"Trailer 3",
                       "postdate":"Fri, 29 Jan 2016 00:00:00 -0800",
                       "exclusive":false,
                       "hd":true
                    },
                    {
                       "type":"Trailer 2",
                       "postdate":"Mon, 16 Nov 2015 00:00:00 -0800",
                       "exclusive":false,
                       "hd":true
                    },
                    {
                       "type":"Trailer",
                       "postdate":"Mon, 16 Nov 2015 00:00:00 -0800",
                       "exclusive":false,
                       "hd":true
                    }
                 ]
              }
           ]
        }
    """
    try:
        results = requests.get(
            f"https://trailers.apple.com/trailers/home/scripts/quickfind.php?q={query.replace(' ', '%20')}")
        return results.json()
    except requests.exceptions.RequestException as e:
        raise e
