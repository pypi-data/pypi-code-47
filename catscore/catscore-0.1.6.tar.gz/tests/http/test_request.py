import unittest
from catscore.http.request import CatsRequest


class TestCatsRequest(unittest.TestCase):

    def test_get(self):
        request:CatsRequest = CatsRequest()
        responseHtml = request.get(url="https://yahoo.co.jp", response_content_type="html")
        responseJson = request.get(url="https://api.rescala.jp/current_stock_info", response_content_type="json")
        print(responseJson)
        request.close()

if __name__ == "__main__":
    unittest.main()