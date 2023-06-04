from fastapi import FastAPI
from app.routers import users, typeTransaction, account
import app.adapters.database as _database

app = FastAPI()


app.include_router(users.userRouter)
app.include_router(typeTransaction.typeTransactionRouter)
app.include_router(account.accountRouter)
# app.include_router(transactions.transactionRouter)

_database.Base.metadata.create_all(_database.engine)
