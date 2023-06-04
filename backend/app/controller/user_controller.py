import app.adapters.database as _database
from app.models.user import User


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

    def insert_user(self, user):
        print(user)
        new_user = User(id_card=user.id_card,
                        name_user=user.name_user,
                        hash_password=user.hash_password)

        self._Base.add(new_user)
        self._Base.commit()
        self._Base.refresh(new_user)
        self._Base.close()

        return new_user
