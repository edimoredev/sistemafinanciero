import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import app.adapters.database as _database
import datetime


class Transaction(_database.Base):
    """_summary_

    Args:
        _database (_type_): _description_
    """
    __tablename__ = 'transactions'
    id_transaction = _sql.Column(_sql.BigInteger, primary_key=True)

    # _Relationship to the table of accounts
    id_account = _sql.Column(_sql.BigInteger, _sql.ForeignKey(
        "accounts.id_account", ondelete="CASCADE"), nullable=False)
    account = _orm.relationship(
        'Account', backref=_orm.backref('transactions', lazy=True))

    # _Relationship to the table of TypeTransaction
    id_type_transactions = _sql.Column(_sql.BigInteger, _sql.ForeignKey(
        "typetransactions.id_typeTransactions", ondelete="CASCADE"), nullable=False)
    type_transaction = _orm.relationship(
        'TypeTransaction', backref=_orm.backref('transactions', lazy=True))

    amount = _sql.Column(_sql.Numeric(20, 2), nullable=False)
    date = _sql.Column(_sql.DateTime, default=datetime.datetime.now())

    def __str__(self):
        return self.id_cuenta
