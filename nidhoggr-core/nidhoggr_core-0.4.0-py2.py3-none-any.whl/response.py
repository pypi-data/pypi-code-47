from pydantic import BaseModel


class StatusResponse(BaseModel):
    status: bool = True

    class Config:
        allow_mutation = False


class ErrorResponse(BaseModel):
    reason: str

    class Config:
        allow_mutation = False
