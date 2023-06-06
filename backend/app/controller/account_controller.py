import app.adapters.database as _database
from app.models.account import Account
from app.models.user import User


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

    def get_account_user(self, name_user):
        accountUser = self._Base.query(Account).join(
            User).filter(User.name_user == name_user).first()
        self._Base.close()
        return accountUser

    def insert_account(self, account, numCuenta):
        new_account = Account(id_account=numCuenta,
                              id_user=account.id_user,
                              name_surname=account.name_surname.upper())

        self._Base.add(new_account)
        self._Base.commit()
        self._Base.refresh(new_account)
        self._Base.close()

        return new_account
