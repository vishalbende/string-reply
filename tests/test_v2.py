from fastapi.testclient import TestClient

from api.main import _get_app

client = TestClient(_get_app())


def test_string_reply_v2_rule_11():
    response = client.get("/v2/reply/11-kbzw9ru")
    assert response.status_code == 200
    assert response.json() == {
        "data": "kbzw9ru"
    }

def test_string_reply_v2_rule_12():
    response = client.get("/v2/reply/12-kbzw9ru")
    assert response.status_code == 200
    assert response.json() == {
        "data": "5a8973b3b1fafaeaadf10e195c6e1dd4"
    }

def test_string_reply_v2_rule_22():
    response = client.get("/v2/reply/22-kbzw9ru")
    assert response.status_code == 200
    assert response.json() == {
        "data": "e8501e64cf0a9fa45e3c25aa9e77ffd5"
    }

def test_string_reply_v2_rule_23():
    response = client.get("/v2/reply/23-kbzw9ru")
    assert response.status_code == 400
    assert response.json() == {
        "message": "Invalid input"
    }
