from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Worldbbbbbbaaxxxxayyy"}

def test_post():
    temp = {
        "cost": 100,
        "tax_rate": 0.1
    }
    data = json.dumps(temp)
    response = client.post("/", content=data)
    assert response.status_code == 200
    assert response.json() == {'price with tax': 110}
    assert response.json()["price with tax"] == 110

def test_get_items():
    response = client.get("/items/1234")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1234, "qaaaa": None}

def test_get_user_normal():
    res = client.get('/users/abcde12345', headers={"token": "correct_token"})
    assert res.status_code             == 200
    assert res.json()['id']            == 'abcde12345'
    assert res.json()['name']          == 'Yamada'
    assert res.json()['email_address'] == 'yamada@example.com'
    assert len(res.json())             == 3

def test_get_user_ng_token():
    res = client.get('/users/abcde12345', headers={"token": "ng_token"})
    assert res.status_code      == 400
    assert res.json()['detail'] == "token_verification_failed"

def test_get_user_not_found():
    res = client.get('/users/abcde33333', headers={"token": "correct_token"})
    assert res.status_code      == 404
    assert res.json()['detail'] == "user_not_found"

def test_post_create_user_normal():
    h_contents = {"token": "correct_token"}
    data = json.dumps({
        "id": "test",
        "name": "test_man",
        "email_address": "test_man@man.jp",
    })
    res = client.post('/users/', headers=h_contents, content=data)
    assert res.status_code             == 200
    assert res.json()['id']            == 'test'
    assert res.json()['name']          == 'test_man'
    assert res.json()['email_address'] == 'test_man@man.jp'
    assert len(res.json())             == 3

def test_post_create_user_duplicated():
    h_contents = {"token": "correct_token"}
    data = json.dumps({
        "id": "abcde12345", # ★
        "name": "test_man",
        "email_address": "test_man@man.jp",
    })
    res = client.post('/users/', headers=h_contents, content=data)
    assert res.status_code      == 404
    assert res.json()['detail'] == "user_id_duplicated"

def test_post_create_user_ng_token():
    h_contents = {"token": "ng_token"}
    data = json.dumps({
        "id": "test",
        "name": "test_man",
        "email_address": "test_man@man.jp",
    })
    res = client.post('/users/', headers=h_contents, content=data)
    assert res.status_code      == 400
    assert res.json()['detail'] == "token_verification_failed"
