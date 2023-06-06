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

    def put_account_balance(self, account):
        if account.id_type_transactions == 2:
            saldo = self._Base.query(Account).filter(
                Account.id_account == account.id_account).first()
            suma = saldo.balance + account.amount
            self._Base.query(Account).filter(
                Account.id_account == account.id_account).update({Account.balance: suma})
            self._Base.commit()
            self._Base.close()
            return True
        else:
            saldo = self._Base.query(Account).filter(
                Account.id_account == account.id_account).first()

            if saldo.balance >= account.amount:
                resta = saldo.balance - account.amount
                self._Base.query(Account).filter(
                    Account.id_account == account.id_account).update({Account.balance: resta})
                self._Base.commit()
                self._Base.close()
                return True
            else:
                return False

    def insert_account(self, account, numCuenta):
        new_account = Account(id_account=numCuenta,
                              id_user=account.id_user,
                              name_surname=account.name_surname.upper())

        self._Base.add(new_account)
        self._Base.commit()
        self._Base.refresh(new_account)
        self._Base.close()

        return new_account
