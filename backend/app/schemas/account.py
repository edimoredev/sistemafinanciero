import pydantic as _pydantic


class AccountBase(_pydantic.BaseModel):
    id_user: str
    name_surname: str
    balance: float


class AccountCreate(AccountBase):
    pass


class Accoun(AccountBase):
    id_account: int
    id_user: str
    name_surname: str
    balance: float

    class Config:
        orm_mode = True
