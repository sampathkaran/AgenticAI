from pydantic import BaseModel

class Details(BaseModel):
    name : str
    age: int
    email : str


user1 = Details(name="sam", age=37, email="sampathkar@gmail.com")
print(user1)

user2 = Details(name = "idhal", age= on1, email= none)
print(user2)
