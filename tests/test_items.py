def test_create_item(client):
    response = client.post("/items", json={"name": "Hammer", "price": 9.99})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Hammer"
    assert data["price"] == 9.99
    assert "id" in data


def test_list_items(client):
    client.post("/items", json={"name": "Hammer", "price": 9.99})
    client.post("/items", json={"name": "Nail", "price": 0.10})
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_item(client):
    create = client.post("/items", json={"name": "Hammer", "price": 9.99})
    item_id = create.json()["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Hammer"


def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404


def test_update_item(client):
    create = client.post("/items", json={"name": "Hammer", "price": 9.99})
    item_id = create.json()["id"]
    response = client.put(
        f"/items/{item_id}", json={"name": "Sledgehammer", "price": 29.99}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Sledgehammer"


def test_delete_item(client):
    create = client.post("/items", json={"name": "Hammer", "price": 9.99})
    item_id = create.json()["id"]
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204
    assert client.get(f"/items/{item_id}").status_code == 404
