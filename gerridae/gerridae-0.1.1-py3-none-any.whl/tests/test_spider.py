"""
test the integer field
"""

from gerridae import Item, TextField, Spider
from gerridae.log import get_logger

logger = get_logger(__name__)


class GerridaeItem(Item):
    command = TextField(css_select='#pip-command')


class GerridaeSpider(Spider):
    start_urls = 'https://pypi.org/project/gerridae/'

    def parse(self, response):
        result = GerridaeItem.get_item(html=response.text)
        return result


def test_spider():
    result = GerridaeSpider.start()
    logger.info(result)
    assert 'pip install gerridae' == result.command
