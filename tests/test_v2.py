from fastapi.testclient import TestClient

from api.main import _get_app
from string_reply.rules import Rules

client = TestClient(_get_app())

# single rule test
def test_rule_1():
    rule_obj = Rules()
    input_string = 'kbzw9ru'
    return_str = rule_obj.rule_1(input_string)
    assert return_str == 'ur9wzbk'


def test_rule_2():
    rule_obj = Rules()
    input_string = 'kbzw9ru'
    return_str = rule_obj.rule_2(input_string)
    assert return_str == '0fafeaae780954464c1b29f765861fad'
    

# Api tests
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

def test_string_reply_v2_rule_1111():
    """
    - test to run same rule for multiple times and not limited to 2 digits
    """
    response = client.get("/v2/reply/1111-kbzw9ru")
    assert response.status_code == 200
    assert response.json() == {
        "data": "kbzw9ru"
    }
    
    

    