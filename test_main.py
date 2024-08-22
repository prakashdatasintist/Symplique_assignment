from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_set_token():
    response = client.post("/set_token/", params={"token": "token1"})
    assert response.status_code == 200
    assert response.json() == {"message": "Token added to cache"}

def test_get_token():
    # Add a token first
    client.post("/set_token/", params={"token": "token2"})
    
    # Now test getting it
    response = client.get("/get_token/", params={"token": "token2"})
    assert response.status_code == 200
    assert response.json() == {"token": "token2"}

def test_get_token_not_found():
    response = client.get("/get_token/", params={"token": "nonexistent"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Token not found in cache"}

def test_fifo_eviction():
    # Add tokens to fill up the cache
    client.post("/set_token/", params={"token": "tokenA"})
    client.post("/set_token/", params={"token": "tokenB"})
    client.post("/set_token/", params={"token": "tokenC"})
    
    # Cache is full, adding another token should evict the first one
    client.post("/set_token/", params={"token": "tokenD"})
    
    # The oldest token ('tokenA') should have been evicted
    response = client.get("/get_token/", params={"token": "tokenA"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Token not found in cache"}
