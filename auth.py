from fastapi import APIRouter, HTTPException, security
from rest_framework import status

from database import session,ENGINE
from schemas import RegisterModel,LoginModel
from models import User
from werkzeug import security

auth_router = APIRouter(prefix="/auth", tags=["auth"])

session = session(bind=ENGINE)

@auth_router.get("/login")
async def login():
    return {"message": "login"}


@auth_router.post("/login")
async def login(user: LoginModel):
    username = session.query(User).filter(User.username == user.username).first()
    if username is None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username does not exist")

    user_check = session.query(User).filter(User.username == user.username).first()

    if security.check_password_hash(user_check.password, user.password):
        return HTTPException(status_code=status.HTTP_200_OK, detail="login successful")

    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password is incorrect")


@auth_router.get("/logout")
async def logout():
    return {"message": "logout"}

@auth_router.get("/register")
async def register():
    return {"message": "register"}


@auth_router.post("/register")
async def register(user: RegisterModel):
    username = session.query(User).filter(User.username == user.username).first()
    email = session.query(User).filter(User.email == user.email).first()
    if email or username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username or email already exists")


    new_user = User(
        id=user.id,
        firs_name=user.firs_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        password=security.generate_password_hash(user.password),
        is_staff=user.is_staff,
        is_active=user.is_active
    )
    session.add(new_user)
    session.commit()
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="user created")