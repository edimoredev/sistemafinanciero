import sqlalchemy as _sql
import app.adapters.database as _database


class TypeTransaction(_database.Base):
    """_summary_

    Args:
        _database (_type_): _description_
    """
    __tablename__ = 'typetransactions'

    id_typeTransactions = _sql.Column(_sql.BigInteger, primary_key=True)
    name_typeTransactions = _sql.Column(_sql.String(50), nullable=False)
    status = _sql.Column(_sql.Boolean, default=True, nullable=False)

    def __str__(self):
        return self.name_typeTransactions
