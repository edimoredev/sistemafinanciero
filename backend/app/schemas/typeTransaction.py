import pydantic as _pydantic


class _TypeTransactionBase(_pydantic.BaseModel):
    name_typeTransactions: str
    status: bool


class TypeTransactionCreate(_TypeTransactionBase):
    pass


class TypeTransaction(_TypeTransactionBase):
    id_typeTransactions: int
    name_typeTransactions: str
    status: bool
