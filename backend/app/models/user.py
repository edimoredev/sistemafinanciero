import sqlalchemy as _sql
import passlib.hash as _hash
import app.adapters.database as _database


class User(_database.Base):
    """Clase usuario, encargado de crear el modelo usuario con sus atributos

    Args:

    """
    __tablename__ = 'users'
    id_card = _sql.Column(_sql.String(50), primary_key=True)
    name_user = _sql.Column(_sql.String, unique=True, index=True)
    hash_password = _sql.Column(_sql.String)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hash_password)

    def __str__(self):
        return self.name_user
