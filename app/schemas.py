from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    cost: float


class Item(ItemCreate):
    id: int
