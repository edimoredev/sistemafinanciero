import pydantic as _pydantic
import datetime as _dt


class _TransactionBase(_pydantic.BaseModel):
    id_account: int
    id_typeTransactions: int
    amount: int


class TransactionCreate(_TransactionBase):
    pass


class Transaction(_TransactionBase):
    id_transaction: int
    date: _dt.datetime
