from typing import List

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        from_attributes = True


class Blog(BaseModel):
    title: str
    body: str
    user_id: int

    class Config():
        from_attributes = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        from_attributes = True


class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: ShowUser

    class Config():
        from_attributes = True


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
