from fastapi import FastAPI
from app.routers import users, typeTransactions, accounts, transactions
import app.adapters.database as _database

app = FastAPI()


app.include_router(users.userRouter)
app.include_router(typeTransactions.typeTransactionRouter)
app.include_router(accounts.accountRouter)
app.include_router(transactions.transactionRouter)

_database.Base.metadata.create_all(_database.engine)
