import app.adapters.database as _database
from app.models.user import User
import passlib.hash as _hash


class UserController():

    def __init__(self):
        self.__Session = _database.SessionLocal
        self._Base = self.__Session()

    def get_all_users(self):
        users = self._Base.query(User).all()
        self._Base.close()
        return list(users)

    def get_user(self, id_card):
        user = self._Base.query(User).filter(User.id_card == id_card).first()
        self._Base.close()
        return user

    def get_name_user(self, name_user):
        user = self._Base.query(User).filter(
            User.name_user == name_user).first()
        self._Base.close()
        return user

    def insert_user(self, user):
        new_user = User(id_card=user.id_card,
                        name_user=user.name_user.upper(),
                        hash_password=_hash.bcrypt.hash(user.hash_password))

        self._Base.add(new_user)
        self._Base.commit()
        self._Base.refresh(new_user)
        self._Base.close()

        return new_user
