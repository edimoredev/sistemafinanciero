import pydantic as _pydantic
from typing import Optional


class AccountBase(_pydantic.BaseModel):
    id_user: str
    name_surname: str
    balance: float


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id_account: int
    id_user: str
    name_surname: str
    balance: float

    class Config:
        orm_mode = True


class UserAccount(_pydantic.BaseModel):
    id_card: str
    name_user: str
    account: AccountBase
