from pydantic import BaseModel

class CreateUserBodyModel(BaseModel):
    email: str
    nickname: str
    password: str


class UpdateUserBodyModel(BaseModel):
    email: str
    nickname: str
    password: str


class CreateCarBodyModel(BaseModel):
    name: str
    number: str
    users_id: int


class UpdateCarBodyModel(BaseModel):
    name: str
    number: str
    users_id: int