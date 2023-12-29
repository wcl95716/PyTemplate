from pydantic import BaseModel

from models.id.type import ID


class User(ID, BaseModel):
    name: str
    phone: str
    email: str
    avatar: str
    password: str
    pass
