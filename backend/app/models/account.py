import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import app.adapters.database as _database


class Account(_database.Base):
    """_summary_

    Args:
        _database (_type_): _description_
    """
    __tablename__ = 'accounts'
    id_account = _sql.Column(_sql.BigInteger, primary_key=True)

    id_user = _sql.Column(_sql.String(50), _sql.ForeignKey(
        "users.id_cedula", ondelete="CASCADE"), nullable=False)
    user = _orm.relationship(
        'User', backref=_orm.backref('accounts', lazy=True))

    name_surname = _sql.Column(_sql.String(50), nullable=False)
    balance = _sql.Column(_sql.BigInteger)

    def __str__(self):
        return self.name_surname
