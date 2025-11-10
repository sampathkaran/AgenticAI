from pydantic import BaseModel, ValidationError, Field
from datetime import datetime

class User(BaseModel):
    uid: int
    username: str
    email: str
    bio: str = ""
    is_active: bool = True
u1= User(uid=123, username="sam", email="sam@gmail.com")
print(u1.model_dump())
print(u1.model_dump_json(indent=2 ))


class BlogPost(BaseModel):
    title: str
    content: str 
    view_count: int = 0
    is_published: bool = False

    tags: list[str] = Field(default_factory=list)

