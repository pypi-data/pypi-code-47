from pyjstage.pyjstage import Pyjstage
from service import Service
from status import Status
from result import Result
from unittest import TestCase


class TestPyjstage(TestCase):
    def setUp(self):
        self.pyjstage = Pyjstage()

    def tearDown(self):
        pass

    @staticmethod
    def commons(ret: Result):
        assert ret.status == Status.OK.value
        assert ret.message is None
        assert ret.total_results > 0
        assert ret.start_index == 1

    def test_list(self):
        ret = self.pyjstage.list(issn='2186-6619')
        self.commons(ret)
        self.assertEqual(ret.link, 'http://api.jstage.jst.go.jp/searchapi/do?service=2&issn=2186-6619')
        self.assertEqual(ret.servicecd, Service.LIST.value)
        self.assertTrue(ret.items_per_page > 0)
        self.assertTrue(len(ret.entries) > 0)

    def test_search(self):
        ret = self.pyjstage.search(issn='2186-6619', count=1)
        self.commons(ret)
        self.assertEqual(ret.link, 'http://api.jstage.jst.go.jp/searchapi/do?service=3&issn=2186-6619&count=1')
        self.assertEqual(ret.servicecd, Service.SEARCH.value)
        self.assertEqual(ret.items_per_page, 1)
        self.assertEqual(len(ret.entries), 1)

    def test_build_query(self):
        query = self.pyjstage.build_query(
            service=Service.LIST.value,
            pubyearfrom=2017,
            pubyearto=2018,
            material='material',
            issn='issn',
            cdjournal='cdjournal',
            volorder='volorder'
        )
        self.assertEqual(
            query,
            'http://api.jstage.jst.go.jp/searchapi/do?service=2&pubyearfrom=2017&pubyearto=2018&material=material'
            '&issn=issn&cdjournal=cdjournal&volorder=volorder'
        )

        query = self.pyjstage.build_query(
            service=Service.SEARCH.value,
            pubyearfrom=2015,
            pubyearto=2019,
            material='material',
            article='article',
            author='author',
            affile='affile',
            keyword='keyword',
            abst='abst',
            text='text',
            issn='issn',
            cdjournal='cdjournal',
            sortfig='sortfig',
            vol='vol',
            no='no',
            start='start',
            count='count'
        )
        self.assertEqual(
            query,
            'http://api.jstage.jst.go.jp/searchapi/do?service=3&pubyearfrom=2015&pubyearto=2019&material=material'
            '&article=article&author=author&affile=affile&keyword=keyword&abst=abst&text=text&issn=issn'
            '&cdjournal=cdjournal&sortfig=sortfig&vol=vol&no=no&start=start&count=count'
        )
