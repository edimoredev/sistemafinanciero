from fastapi import APIRouter, HTTPException, status
from app.controller.transaction_controller import TransactionController
from app.controller.account_controller import AccountController
from app.schemas.transaction import TransactionCreate


transactionRouter = APIRouter(prefix="/transactions",
                              tags=["transactions"],
                              responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@transactionRouter.post("/", status_code=201)
async def create_transactionType(transaction: TransactionCreate):
    new_transaction = TransactionController(
    ).insert_transaction(transaction)
    return new_transaction

# @transactionRouter.get("/")
# async def get_transactionType_all():
#     transaction = TransactionController().get_all_transaction()
#     if not transaction:
#         raise HTTPException(
#             status_code=404, detail="transaction not found")
#     return transaction
