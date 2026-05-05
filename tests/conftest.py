import pytest
from fastapi.testclient import TestClient

from app.main import app, items


@pytest.fixture
def client():
    items.clear()
    with TestClient(app) as c:
        yield c
