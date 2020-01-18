from threeza.location import assert_algorithmia_web
from threeza.errors import LocationError

def test_location():
    try:
        assert_algorithmia_web()
        assert False
    except LocationError as e:
        pass
