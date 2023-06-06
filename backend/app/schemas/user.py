import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    id_card: str
    name_user: str

    class Config:
        orm_mode = True


class UserCreateDb(_UserBase):
    hash_password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    pass
