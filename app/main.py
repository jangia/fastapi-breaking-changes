from fastapi import FastAPI, HTTPException

from app.schemas import Item, ItemCreate

app = FastAPI(title="Items API")

items: dict[int, Item] = {}
next_id = 1


@app.get("/items", response_model=list[Item])
def list_items():
    return list(items.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global next_id
    item = Item(id=next_id, **payload.model_dump())
    items[next_id] = item
    next_id += 1
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    item = Item(id=item_id, **payload.model_dump())
    items[item_id] = item
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
