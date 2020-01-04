import json
from datetime import datetime

from sqlalchemy import sql, create_engine, MetaData
from sqlalchemy.pool import NullPool
from sqlalchemy.dialects.postgresql import JSONB

from config import url
from .enums import *
from .utils import *

__version__ = "0.0.1"

__all__ = [
    'dynamo_streams_event_handler'
]


def dynamo_streams_event_handler(dynamo_stream_event, context):
    """Entry point for AWS Lambda"""

    conn = None
    try:
        metadata = MetaData()
        engine = create_engine(url, poolclass=NullPool)
        metadata.reflect(engine)
        conn = engine.connect()

        return process_stream_records(conn, dynamo_stream_event['Records'], metadata)
    finally:
        if conn is not None: conn.close()


def process_stream_records(conn, records, metadata):

    count = 0
    for record in records:

        table_name = parse_arn(record['eventSourceARN'])['table']
        table = metadata.tables[table_name]

        event_type = record['eventName']

        if event_type == EventType.insert:
            handle_insert(conn, record, table)
        elif event_type == EventType.modify:
            handle_modify(conn, record, table)
        elif event_type == EventType.remove:
            handle_remove(conn, record, table)
        else:
            raise RuntimeError("Unhandled event type")

        print(record['eventID'])
        print(record['eventName'])
        print("DynamoDB Record: " + json.dumps(record['dynamodb'], indent=2))
        count += 1

    return ('Successfully processed {} records.'.format(count))


def handle_insert(conn, record, table):

    keys = image_as_item(record['dynamodb']['Keys'])
    item = image_as_item(record['dynamodb']['NewImage'])

    item_row, item_state =  get_item(conn, keys, item, table)

    if item_state == ItemState.new:
        return
    elif item_state == ItemState.does_not_exist:
        raise RuntimeError('New item was not created')

    print('Item already exists...')


def handle_modify(conn, record, table):
    """Update the json portion of the item in the db if exists, if it does
    not exist create the row for the item"""

    # TODO: Add check on modtime for updates and dont thrash if under
    # some interval

    keys = image_as_item(record['dynamodb']['Keys'])
    item = image_as_item(record['dynamodb']['NewImage'])

    item_row, item_state = get_item(conn, keys, item, table)

    if item_state == ItemState.new:
        print('Fresh item created on modify, we missed the last update?')
        return

    elif item_state == ItemState.does_not_exist:

        raise RuntimeError('Invalid state')


    primary_key = primary_key_stmt(keys, table)
    update = table.update().where(primary_key).values(item=item, mod_time=datetime.now())
    conn.execute(update)

    print('Item updated')


def handle_remove(conn, record, table):
    """Process a streams request to remove an item from the db"""

    keys = image_as_item(record['dynamodb']['Keys'])
    item = {}

    item_row, item_state = get_item(conn, keys, item, table, create_missing=False)

    if item_state == ItemState.does_not_exist:
        print('Item already deleted')
    elif item_state == ItemState.new:
        raise RuntimeError('A new item was created in the remove handler')

    primary_key = primary_key_stmt(keys, table)
    delete = table.delete().where(primary_key)
    conn.execute(delete)
    conn.execute('COMMIT')


def get_item(conn, keys, item, table, create_missing=True):
    """Get item from db with optional create"""

    primary_key = primary_key_stmt(keys, table)

    select_existing_entry = table.select().where(primary_key)
    row = conn.execute(select_existing_entry).fetchone();

    if row is not None:
        print('exising item')
        return dict(row), ItemState.exists

    elif create_missing == False:
        return None, ItemState.does_not_exist


    result = {}
    result.update(keys)
    result['item'] = dict(item)

    insert_values = dict(result)
    insert_values['item'] = insert_values['item']

    now = datetime.now()
    insert_values['mod_time'] = now
    insert_values['create_time'] = now

    #: Add try catch
    insert = table.insert().values(insert_values)
    conn.execute(insert)

    print('new item')
    return result, ItemState.new
