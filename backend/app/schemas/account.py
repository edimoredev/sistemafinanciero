import pydantic as _pydantic


class AccountBase(_pydantic.BaseModel):
    id_account: int
    name_surname: str
    balance: float


class AccountCreate(AccountBase):
    pass


class Accoun(AccountBase):
    id_account: int
    id_user: str

    class Config:
        orm_mode = True
