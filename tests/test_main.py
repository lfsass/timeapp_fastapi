from fastapi.testclient import TestClient
from datetime import datetime

from ..app.main import app

client = TestClient(app)

def test_read_main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"now": now}
