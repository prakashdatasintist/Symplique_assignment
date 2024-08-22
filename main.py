from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

class AuthTokenCache:
    def __init__(self, max_size: int):
        self.cache = []
        self.max_size = max_size

    def get_token(self, token: str) -> Optional[str]:
        if token in self.cache:
            return token
        return None

    def set_token(self, token: str):
        if len(self.cache) >= self.max_size:
            self.cache.pop(0)  # FIFO Eviction
        self.cache.append(token)

# Initialize the cache with a size limit (e.g., 3 tokens)
auth_token_cache = AuthTokenCache(max_size=3)

@app.post("/set_token/")
def set_token(token: str):
    auth_token_cache.set_token(token)
    return {"message": "Token added to cache"}

@app.get("/get_token/")
def get_token(token: str):
    result = auth_token_cache.get_token(token)
    if result:
        return {"token": result}
    raise HTTPException(status_code=404, detail="Token not found in cache")
