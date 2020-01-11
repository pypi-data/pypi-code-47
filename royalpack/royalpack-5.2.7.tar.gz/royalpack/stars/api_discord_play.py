from typing import *
from starlette.requests import Request
from starlette.responses import *
from royalnet.constellation import *
from royalnet.utils import *


class ApiDiscordPlayStar(PageStar):
    path = "/api/discord/play"

    async def page(self, request: Request) -> JSONResponse:
        url = request.query_params.get("url", "")
        try:
            guild_id: Optional[int] = int(request.path_params.get("guild_id", None))
        except (ValueError, TypeError):
            guild_id = None
        response = await self.interface.call_herald_event("discord", "discord_play", url=url, guild_id=guild_id)
        return JSONResponse(response, headers={
            "Access-Control-Allow-Origin": self.interface.config['Funkwhale']['instance_url'],
        })
