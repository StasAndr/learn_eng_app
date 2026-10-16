from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DeckCreate(BaseModel):
    title: str


class DeckRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    created_at: datetime