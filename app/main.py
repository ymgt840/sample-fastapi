from typing import Union
from fastapi import FastAPI, Header, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel

# 正常トークン
correct_token = "correct token"

# ユーザデータ
dummy_user_data = {
    "abcde12345": {"id": "abcde12345", "name": "Yamada", "email_address": "yamada@example.com"},
    "fghij67890": {"id": "fghij67890", "name": "Tanaka", "email_address": "tanaka@example.com"},
}

class User(BaseModel):
    id: str
    name: str
    email_address: str

class TaxIn(BaseModel):
    cost: int
    tax_rate: float

app = FastAPI()

# ユーザー情報取得API
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str, token: str = Header(...)):
    # トークン不正時
    if token != correct_token:
        raise HTTPException(
            status_code=400, detail="token_verification_failed")
    # ユーザー非存在時
    if user_id not in dummy_user_db:
        raise HTTPException(status_code=404, detail="user_not_found")
    return dummy_user_db[user_id]


# ユーザー情報登録API
@app.post("/users/", response_model=User)
async def create_user(user: User, token: str = Header(...)):
    # トークン不正時
    if token != correct_token:
        raise HTTPException(
            status_code=400, detail="token_verification_failed")
    # ユーザーID重複時
    if user.id in dummy_user_db:
        raise HTTPException(status_code=400, detail="user_id_duplicated")
    dummy_user_db[user.id] = user
    return user



@app.get("/")
def read_root():
    return {"Hello": "Worldbbbbbbaaxxxxayyy"}

@app.post("/")
def calc(data: TaxIn):
    cost_in_tax = data.cost * (1 + data.tax_rate)
    return {'price with tax': cost_in_tax}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "qaaaa": q}


client = TestClient(app)
# テスト
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Worldbbbbbbaaxxxxayyy"}