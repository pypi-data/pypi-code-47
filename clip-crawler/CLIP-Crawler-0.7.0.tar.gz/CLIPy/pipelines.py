from sqlalchemy.orm import sessionmaker
from models import Deals, db_connect, create_deals_table

class StudentPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates students table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = Deals(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item