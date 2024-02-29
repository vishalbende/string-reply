from fastapi.testclient import TestClient

from api.main import _get_app

client = TestClient(_get_app())

def test_string_reply_v1():
    response = client.get("/v1/reply/kbzw9ru")
    assert response.status_code == 200
    assert response.json() == {
        "data": "kbzw9ru"
    }
