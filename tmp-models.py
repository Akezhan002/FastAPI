from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    user_name: str
    user_age: int
