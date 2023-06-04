import app.adapters.database as _database
from app.models.typeTransaction import TypeTransaction


class TypeTransactionController():

    def __init__(self):
        self.__Session = _database.SessionLocal
        self._Base = self.__Session()

    def get_all_transactionType(self):
        transaction_type = self._Base.query(TypeTransaction).all()
        self._Base.close()
        return transaction_type

    def get_transactionType(self, name_typo):
        transaction_type = self._Base.query(TypeTransaction).filter(
            TypeTransaction.name_typeTransactions == name_typo).first()
        self._Base.close()
        return transaction_type

    def insert_transactionType(self, transactionType):
        new_transactionType = TypeTransaction(
            name_typeTransactions=transactionType.name_typeTransactions)

        self._Base.add(new_transactionType)
        self._Base.commit()
        self._Base.refresh(new_transactionType)
        self._Base.close()

        return new_transactionType
