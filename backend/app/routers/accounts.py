from fastapi import APIRouter, HTTPException, status
from app.controller.account_controller import AccountController
from app.controller.user_controller import UserController
from app.schemas.account import AccountCreate
import random as _random


accountRouter = APIRouter(prefix="/accounts",
                          tags=["accounts"],
                          responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@accountRouter.post("/", status_code=201)
async def create_account(account: AccountCreate):
    user = UserController().get_user(account.id_user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El usuario no existe, para crear la cuenta, debe crear un usuario")

    # genera un numero aleatorio de 10 digitos para asignarlo al usuario
    numCuenta = _random.randint(6000000000, 10000000000)

    idAccount = AccountController().get_account(numCuenta)
    if idAccount:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="La cuenta ya existe")

    new_account = AccountController().insert_account(account, numCuenta)
    return new_account


# @accountRouter.get("/")
# async def get_account_all():
#     accounts = AccountController().get_all_account()
#     if not accounts:
#         raise HTTPException(
#             status_code=404, detail="Accounts not found")
#     return accounts

@accountRouter.get("/{user_name}")
async def get_account_all(user_name: str):
    accounts = AccountController().get_account_user(user_name.upper())
    if not accounts:
        raise HTTPException(
            status_code=404, detail="Accounts not found")
    return accounts
