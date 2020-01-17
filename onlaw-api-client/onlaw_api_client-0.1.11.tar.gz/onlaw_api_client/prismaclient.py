import logging
import jwt
import aiohttp

import os
import sys

this_file_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.join(this_file_path, '../..')
sys.path.append(root_path)

from onlaw_api_client.client import Onlaw


class PrismaClient:
    """thin wrapper around onlaw client"""

    def __init__(self, endpoint: str):
        self.logger = logging.getLogger(__name__)
        self.endpoint: str = endpoint
        self.onlaw_client: Onlaw = Onlaw(endpoint=endpoint,
                                         client_id='blank',
                                         client_secret='blank')

    async def execute(self, query: str):
        token: str = PrismaClient._get_prisma_token()

        async with aiohttp.ClientSession() as session:
            res = await self.onlaw_client.execute(query, session, token=token, endpoint=self.endpoint)

        return res

    @classmethod
    def _get_prisma_token(cls, PRISMA_SECRET: str = None):
        if PRISMA_SECRET is None:
            try:
                PRISMA_SECRET = os.environ['PRISMA_SECRET']
            except KeyError:
                err_str = 'Environment variable "PRISMA_SECRET" not found. To set do e.g.: export PRISMA_SECRET=<your prisma secret>\n....exiting\n'
                raise KeyError(err_str)

        prisma_token = jwt.encode({}, PRISMA_SECRET, algorithm='HS256').decode('utf-8')

        return prisma_token
