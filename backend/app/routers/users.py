### Users DB API ###
from fastapi import APIRouter, HTTPException, status
from app.controller.user_controller import UserController
from app.schemas.user import UserCreate

userRouter = APIRouter(prefix="/users",
                       tags=["users"],
                       responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@userRouter.post("/", status_code=201)
async def create_user(user: UserCreate):
    idUser = UserController().get_user(user.id_card)
    if idUser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El usuario ya existe")
    new_user = UserController().insert_user(user)
    return new_user


# @userRouter.get("/")
# async def get_user_all():
#     user = UserController().get_all_users()
#     if not user:
#         raise HTTPException(status_code=404, detail="Users not found")
#     return user


@userRouter.get("/")
async def get_user(id_card: str):
    user = UserController().get_user(id_card)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
