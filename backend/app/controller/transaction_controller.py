import app.adapters.database as _database
from app.models.transaction import Transaction


class TransactionController():

    def __init__(self):
        self.__Session = _database.SessionLocal
        self._Base = self.__Session()

    def get_all_transaction(self):
        transaction = self._Base.query(Transaction).all()
        self._Base.close()
        return transaction

    def get_transaction(self, id_transaction):
        transaction = self._Base.query(Transaction).filter(
            Transaction.id_transaction == id_transaction).first()
        self._Base.close()
        return transaction

    def insert_transaction(self, transaction):
        new_transaction = Transaction(id_account=transaction.id_account,
                                      id_typeTransactions=transaction.id_typeTransactions,
                                      amount=transaction.amount)

        self._Base.add(new_transaction)
        self._Base.commit()
        self._Base.refresh(new_transaction)
        self._Base.close()

        return new_transaction
