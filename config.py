from fastapi import FastAPI
from auth import auth_router

app = FastAPI()
app.include_router(auth_router)


@app.get("/")
async def landing():
    return {
        "message": "Hello World!"
    }

@app.get("/test/{id}")
async def landing(id: int):
    return {
        "message": f"user {id}"
    }

@app.post("/test")
async def test():
    return {
        "message": "test post!"
    }

