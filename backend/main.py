from fastapi import FastAPI
from app.routers import users, typeTransaction
import app.adapters.database as _database

app = FastAPI()


app.include_router(users.userRouter)
app.include_router(typeTransaction.typeTransactionRouter)

_database.Base.metadata.create_all(_database.engine)
