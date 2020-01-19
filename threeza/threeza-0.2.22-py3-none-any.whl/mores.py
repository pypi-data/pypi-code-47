
from .web_utils import get_url

def author_has_approved_pipe_page(algo_name,name):
	""" Does author approve of a page that invokes their algorithm ? """

	assert "/" in algo_name, "Expecting full algorithm name including username (e.g.  threezatests/double)"
	details_url = "https://algorithmia.com/webapi/algorithms/"+algo_name
    try:
        details = json.loads(get_url(details_url))
    except Exception as e:
        return False

    if "summary" in details["algorithm"]:
        if name in details["algorithm"]["summary"]:
            return True
    return False
