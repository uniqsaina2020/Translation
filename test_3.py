from fastapi import FastAPI, Path, Query 
from typing import Optional

from pydantic import BaseModel #سنجش اعتبار اطلاعات

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int = Path(gt=0, lt=100)
    height : Optional[int] = 0
    # description: str | None = None
@app.post('/home/')
def index(prs:Person, car:str=Query('nothig', min_length=3, max_length=20)):
    return prs, car