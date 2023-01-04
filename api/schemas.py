from pydantic import BaseModel


class AmericaBase(BaseModel):
    pass



class AmericaCreate(AmericaBase):
    owner_id: int


class America(AmericaBase):
    id: int
    america_name: str
    class Config:
        orm_mode = True


class JapanBase(BaseModel):
    pass

class JapanCreate(JapanBase):
    owner_id: int


class Japan(JapanBase):
    id: int
    japan_name: str
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    america: list[America]
    japan: list[Japan]
    class Config:
        orm_mode = True


class UserEdit(UserBase):
    pass