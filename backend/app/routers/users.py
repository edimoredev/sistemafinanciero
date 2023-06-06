### Users DB API ###
from fastapi import APIRouter, HTTPException, status
from app.controller.user_controller import UserController
from app.schemas.user import UserCreateDb, _UserBase


userRouter = APIRouter(prefix="/users",
                       tags=["users"],
                       responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@userRouter.post("/", status_code=201, response_model=_UserBase)
async def create_user(user: UserCreateDb):
    idUser = UserController().get_user(user.id_card)
    if idUser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El usuario ya existe")
    UserController().insert_user(user)
    return user


# @userRouter.get("/")
# async def get_user_all():
#     user = UserController().get_all_users()
#     if not user:
#         raise HTTPException(status_code=404, detail="Users not found")
#     return user


# @userRouter.get("/{id_card}")
# async def get_user(id_card: str):
#     user = UserController().get_user(id_card)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     account = AccountController().get_account_idCard(id_card)
#     if not user:
#         raise HTTPException(status_code=404, detail="Account not found")

#     return result
