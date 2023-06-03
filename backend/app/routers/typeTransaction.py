### TransactionType DB API ###
from fastapi import APIRouter, HTTPException, status
from app.controller.typeTransaction_controller import TypeTransactionController
from app.schemas.typeTransaction import TypeTransactionCreate


typeTransactionRouter = APIRouter(prefix="/typeTransactions",
                                  tags=["typeTransactions"],
                                  responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@typeTransactionRouter.post("/")
async def create_transactionType(transactionType: TypeTransactionCreate):
    transaction_type = TypeTransactionController().get_transactionType(
        transactionType.name_typeTransactions)
    if transaction_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El tipo de transacción ya existe")

    new_transactionType = TypeTransactionController(
    ).insert_transactionType(transactionType)
    return new_transactionType
