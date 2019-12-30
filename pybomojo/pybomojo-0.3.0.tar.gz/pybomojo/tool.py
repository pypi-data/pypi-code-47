import json
import sys

from . import get_movie_id, get_box_office

search_term = sys.argv.pop()
movie_id = get_movie_id(search_term)
box_office = get_box_office(movie_id)
json.dump(box_office, sys.stdout)
