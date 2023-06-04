import app.adapters.database as _database
from app.models.user import User


class TransactionController():

    def __init__(self):
        self.__Session = _database.SessionLocal
        self._Base = self.__Session()
