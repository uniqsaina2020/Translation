from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel #سنجش اعتبار اطلاعات

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int
    height : Optional[int] = 0
    # description: str | None = None
@app.post('/home/')
def index(prs:Person):
    return prs.name