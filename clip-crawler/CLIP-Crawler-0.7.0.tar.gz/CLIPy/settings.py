BOT_NAME = 'CLIPy'

SPIDER_MODULES = ['CLIPy.spiders']


DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'YOUR_USERNAME',
    'password': 'YOUR_PASSWORD',
    'database': 'scrape'
}

ITEM_PIPELINES = ['scraper_app.pipelines.StudentPipeline']