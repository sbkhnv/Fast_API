from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
     name: str
     description: str = None
     price: float
     tax: float = None
     tags: list[str] = []

