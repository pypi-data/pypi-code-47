import os
import requests
import json
import datetime
from datetime import datetime as dt, date
import logging

import nltk
from newspaper import Article
from dotenv import load_dotenv

from contendo_utils import * #ProUtils, BigqueryUtils, contendo_classfunction_logger, contendo_logging_setup, contendo_function_logger
from contendo_finance_insights import *

class GetStockNews:
    def __init__(self):
        stocknews_apikey=os.environ['STOCKNEWS_API_KEY']
        #self.stocknews_url_template = "https://stocknewsapi.com/api/v1?tickers={ticker}&items={nitems}&date={fromdate_MMDDYYYY}-today&sortby={sortby}&token={stocknews_apikey}".replace('{stocknews_apikey}', stocknews_apikey)
        self.stocknews_url_template = "https://stocknewsapi.com/api/v1?tickers={ticker}&items={nitems}&sortby={sortby}&token={stocknews_apikey}".replace('{stocknews_apikey}', stocknews_apikey)
        self.bqu = BigqueryUtils()
        self.learn=None
        #nltk.download('punkt')  # 1 time download of the sentence tokenizer

    @contendo_classfunction_logger
    def get_article_by_url(self, url:str) -> dict:
        _articleData=dict()
        # Do some NLP
        try:
            article = Article(url)
            article.download()  # Downloads the link’s HTML content
            article.parse()  # Parse the article
            article.nlp()  # Keyword extraction wrapper
            _articleData['text'] = article.text#.replace('\n', '\n')
            _articleData['summary'] = article.summary#.replace('\n', '\n')
            _articleData['title'] = article.title
            _articleData['authors'] = str(article.authors)[1:-1].replace("'","")
            _articleData['keywords'] = str(article.keywords)[1:-1].replace("'","")
            _articleData['publish_date'] = article.publish_date
            _articleData['tags'] = str(article.tags)[1:-1].replace("'","")
            _articleData['url'] = url
            try:
                if self.learn == None:
                    from fastai.text import load_learner
                    learn = load_learner('resource', 'final-finance-semantic-model')
                _articleData['text_sentiment'] = str(learn.predict(_articleData['text']))
                _articleData['summary_sentiment'] = str(learn.predict(_articleData['summary']))
            except Exception as e:
                logger.exception('Not able to do sentiment.')
                pass
        except Exception as e:
            logger.error('Error %s occured with URL %s', e, url)
            raise e

        return _articleData

    @contendo_classfunction_logger
    def get_stocknews_byticker(self, tickersList:list, nitems:int=50, daysback:int=30, sortby:str='trending'):
        assert(sortby in ['trending', 'algo'])

        tickers = str(tickersList).replace('[', '').replace(']', '').replace("'", '').replace(' ', '')
        urlInstructions={
            'ticker': tickers,
            'nitems': nitems,
            'fromdate_MMDDYYYY': (date.today() - datetime.timedelta(days=daysback)).strftime('%m%d%Y') ,
            'sortby': sortby,
            'today': date.today(),
        }
        outfileName = 'Finance/temp/{ticker}-{nitems}-{fromdate_MMDDYYYY}-{sortby}-{today}.json'.format(**urlInstructions)

        text = self.bqu.read_string_from_gcp(FINANCE_GCP_BUCKET, outfileName)
        if text is None:
            url = self.stocknews_url_template.format(**urlInstructions)
            print(url)
            response = requests.request("GET", url)
            text = response.text
            self.bqu.upload_string_to_gcp(response.text, FINANCE_GCP_BUCKET, outfileName)

        data = json.loads(text)

        if not 'data' in data:
            print ('Error getting news for tickers {}, return={}'.format(tickers, data))
            return {}
        newsDict = data['data']

        sentimentDict = {'Count': 0, 'Negative': 0, 'Positive': 0, 'Neutral': 0, 'Weighted': 0}
        sentimentWeight = {'Negative': -1, 'Positive': 1, 'Neutral': 0}
        count=0
        newsFeed = dict()
        startTime=dt.utcnow()
        for newsItem in newsDict:
            count+=1
            newItem = {key: newsItem[key] for key in ['title', 'text', 'sentiment', 'source_name', 'topics', 'news_url', 'image_url']}
            newItem['index'] = count
            itemDate = dt.strptime(newsItem['date'], '%a, %d %b %Y %H:%M:%S %z')
            delta = startTime.date() - itemDate.date()
            if delta.days <= 3 or count <= 3:
                newItem['date'] = str(itemDate.date())
                if False: # suspend getting the summary
                    article = Article(newItem['news_url'])
                    # Do some NLP
                    try:
                        article.download()  # Downloads the link’s HTML content
                        article.parse()  # Parse the article
                        article.nlp()  # Keyword extraction wrapper
                        newItem['Summary'] = article.summary.replace('\n', '\n')
                    except Exception as e:
                        print ('Error occured:', e)
                        newItem['Summary'] = "<...>"

                #print(newItem['Summary'])
                newsFeed[count] = newItem
            if delta.days<=3:
                deltaWeight=1
            elif delta.days<=7:
                deltaWeight=0.5
            elif delta.days<=14:
                deltaWeight=0.25
            elif delta.days<=30:
                deltaWeight=0.125
            else:
                deltaWeight=0.05

            sentiment = newsItem['sentiment']
            sentimentDict[sentiment]+=1
            sentimentDict['Count']+=1
            sentimentDict['Weighted'] += sentimentWeight[sentiment]*deltaWeight
        retDict = {
            'NumItems': len(newsFeed),
            'Sentiment': sentimentDict,
            'Newsfeed': newsFeed,
        }

        return retDict

@contendo_function_logger
def test():
    gsn = GetStockNews()
    articleData = gsn.get_article_by_url('https://finance.yahoo.com/news/morgan-stanley-ms-vs-top-170426521.html')
    # articleData = gsn.get_article_by_url('https://www.chicagotribune.com/business/ct-wall-street-trump-pence-donations-20160908-story.html')
    print_dict(articleData)


@contendo_function_logger
def get_all_ticker_news_test():
    startTime = dt.now()
    gsn = GetStockNews()
    # print(gsn.get_stocknews_byticker(['AMD']))
    gsd = GetStocksData()
    tickerlist = list(gsd.get_stock_fundamentals(index='SNP')['Symbol'])
    for ticker in tickerlist:
        logger.info('Gettingticker %s', ticker)
        gsn.get_stocknews_byticker([ticker], daysback=365)

if __name__ == '__main__':
    contendo_logging_setup(default_level=logging.DEBUG)
    load_dotenv(verbose=True)
    os.chdir('{}/tmp'.format(os.environ['HOME']))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}/sportsight-tests.json".format(os.environ["HOME"])
    test()