from elasticsearch_async import AsyncElasticsearch
from elasticsearch import exceptions
from datetime import datetime
from aiologs import LoggerConfig
import asyncio

_mappingDef = {
    "mappings": {
        "properties": {
            "project": {
                "type": "keyword"
            },
            "module": {
                "type": "keyword"
            },
            "category": {
                "type": "keyword"
            },
            "sub_category": {
                "type": "keyword"
            },
            "logLevel": {
                "type": "keyword"
            },
            "env": {
                "type": "keyword"
            },
            "ip": {
                "type": "keyword"
            }
        }
    }
}


async def addlogs(data):
    """
    192.168.88.103
    """
    assert len(LoggerConfig.targetDB) > 0
    client = AsyncElasticsearch(hosts=LoggerConfig.targetDB)
    index = f'aiologs-{datetime.now().strftime("%Y.%m.%d")}'
    if not await client.indices.exists(index=index):
        try:
            await client.indices.create(body=_mappingDef, index=index)
        except exceptions.RequestError as e:
            if not (e.status_code == 400
                    and e.error == "resource_already_exists_exception"):
                raise e

    task = []
    for item in data:
        task.append(client.index(index=index, id=None, body=item))
    await asyncio.gather(*task)
