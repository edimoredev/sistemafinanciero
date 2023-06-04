import app.adapters.database as _database
from app.models.account import Account


class AccountController():

    def __init__(self):
        self.__Session = _database.SessionLocal
        self._Base = self.__Session()

    def get_all_account(self):
        account = self._Base.query(Account).all()
        self._Base.close()
        return list(account)

    def get_account(self, id_account):
        account = self._Base.query(Account).filter(
            Account.id_account == id_account).first()
        self._Base.close()
        return account

    def insert_account(self, account, numCuenta):
        print(account.id_user)

        new_account = Account(id_account=numCuenta,
                              id_user=account.id_user,
                              name_surname=account.name_surname)

        self._Base.add(new_account)
        self._Base.commit()
        self._Base.refresh(new_account)
        self._Base.close()

        return new_account
