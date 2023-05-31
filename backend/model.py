from pydantic import BaseModel
from datetime import datetime

class exerciseSchema(BaseModel):
    username: str
    description: str
    duration: int
    date: datetime.date

class userSchema(BaseModel):
    username: str