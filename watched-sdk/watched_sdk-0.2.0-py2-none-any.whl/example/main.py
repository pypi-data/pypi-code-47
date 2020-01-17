import json
import logging
import re
import sys

import watched_sdk

logging.basicConfig(level=logging.INFO)

EXAMPLE_ITEMS = [
    {
        'type': 'movie',
        'ids': {
            'python.example': 'id1234'
        },
        'name': 'Example Item'
    }
]

EXAMPLE_SOURCES = {
    'id1234': [
        {
            'name': 'Example source',
            'url': 'http://exameple.com/source1.mp4'
        }
    ]
}


class ExampleAddon(watched_sdk.WorkerAddon):
    props = {
        'id': 'python.example',
        'name': 'Example Addon',
        'version': '1.0.0',
        'actions': ['directory', 'item', 'source'],
        'itemTypes': ['movie', 'series'],
    }

    def directory(self, ctx, **kwargs):
        return {
            'items': EXAMPLE_ITEMS,
            'hasMore': False
        }

    def item(self, ctx, ids, **kwargs):
        id = ids[self.id]
        for item in EXAMPLE_ITEMS:
            if item['ids'][self.id] == id:
                return item
        return None

    def source(self, ctx, ids, **kwargs):
        id = ids[self.id]
        return EXAMPLE_SOURCES.get(id, None)


if __name__ == '__main__':
    watched_sdk.main([ExampleAddon()], *sys.argv[1:])
