from typing import *
from starlette.requests import Request
from starlette.responses import *
from royalnet.constellation import *
import logging


log = logging.getLogger(__name__)


class ApiDiscordPlayStar(PageStar):
    path = "/api/discord/play"

    async def page(self, request: Request) -> JSONResponse:
        url = request.query_params.get("url", "")
        user = request.query_params.get("user")
        try:
            guild_id: Optional[int] = int(request.query_params.get("guild_id", None))
        except (ValueError, TypeError):
            guild_id = None
        log.info(f"Received request to play {url} on guild_id {guild_id} via web")
        response = await self.interface.call_herald_event("discord", "discord_play",
                                                          url=url,
                                                          guild_id=guild_id,
                                                          user=user)
        return JSONResponse(response, headers={
            "Access-Control-Allow-Origin": "*",
        })
