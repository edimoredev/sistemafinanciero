### Users DB API ###
from fastapi import APIRouter, HTTPException, status
from app.controller.user_controller import UserController
from app.schemas.user import UserCreate
# from db.models.user import User
# from db.schemas.user import user_schema, users_schema
# from db.client import db_client
# from bson import ObjectId


userRouter = APIRouter(prefix="/users",
                       tags=["users"],
                       responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@userRouter.post("/")
async def create_user(user: UserCreate):
    user = UserController().get_user(user.id_card)
    if user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El usuario ya existe")
    new_user = UserController().insert_user(user)
    return new_user


@userRouter.get("/")
async def get_user_all():
    user = UserController().get_all_users()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
