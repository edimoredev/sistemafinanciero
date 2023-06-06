import app.adapters.database as _database
from app.models.transaction import Transaction
from app.models.account import Account


class TransactionController():

    def __init__(self):
        self.__Session = _database.SessionLocal
        self._Base = self.__Session()

    def get_all_transaction(self):
        transaction = self._Base.query(Transaction).all()
        self._Base.close()
        return transaction

    def put_transactionSaldo(self, transaction):
        if transaction.id_type_transactions == 2:
            saldo = self._Base.query(Account).filter(
                Account.id_account == transaction.id_account).first()
            suma = saldo.balance + transaction.amount
            self._Base.query(Account).filter(
                Account.id_account == transaction.id_account).update({Account.balance: suma})
            self._Base.commit()
            self._Base.close()
            return True
        else:
            saldo = self._Base.query(Account).filter(
                Account.id_account == transaction.id_account).first()

            if saldo.balance >= transaction.amount:
                resta = saldo.balance - transaction.amount
                self._Base.query(Account).filter(
                    Account.id_account == transaction.id_account).update({Account.balance: resta})
                self._Base.commit()
                self._Base.close()
                return True
            else:
                return False

    def insert_transaction(self, transaction):
        new_transaction = Transaction(id_account=transaction.id_account,
                                      id_type_transactions=transaction.id_type_transactions,
                                      amount=transaction.amount)

        self._Base.add(new_transaction)
        self._Base.commit()
        self._Base.refresh(new_transaction)
        self._Base.close()

        return new_transaction
