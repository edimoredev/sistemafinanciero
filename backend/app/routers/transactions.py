from fastapi import APIRouter, HTTPException, status
from app.controller.transaction_controller import TransactionController
from app.schemas.transaction import TransactionCreate


transactionRouter = APIRouter(prefix="/transactions",
                              tags=["transactions"],
                              responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@transactionRouter.post("/")
async def create_transactionType(transaction: TransactionCreate):
    transaction_type = TypeTransactionController().get_transactionType(
        transaction.name_typeTransactions)
    if transaction_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El tipo de transacción ya existe")

    new_transactionType = TypeTransactionController(
    ).insert_transactionType(transactionType)
    return new_transactionType
