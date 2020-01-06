from typing import Optional

from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: bool = True
    reason: Optional[str] = None

    class Config:
        allow_mutation = False
