from pydantic import BaseModel


class BasePydanticModel(BaseModel):
    class Config:
        from_attributes = False
        validate_assignment = True

class UserBase(BasePydanticModel):
    uuid: str
    name: str
    time_created: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    pass

class UserPostBase(BasePydanticModel):
    uuid: str
    user_uuid: str
    post_9char: str
    text: str
    time_created: int

class UserPostCreate(UserPostBase):
    pass

class UserPost(UserPostBase):
    pass

