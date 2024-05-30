import os
from fastapi import APIRouter, HTTPException, security, status, Response, Security
from database import session,ENGINE
from schemas import RegisterModel,LoginModel
from fastapi.encoders import jsonable_encoder
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer
from dotenv import load_dotenv
from models import User
from werkzeug import security
load_dotenv()
access_security = JwtAccessBearer(secret_key=os.getenv("secret_key"),auto_error=True)
auth_router = APIRouter(prefix="/auth")

session = session(bind=ENGINE)

@auth_router.get("/")
async def auth():
    return {"message": "auth page"}

@auth_router.get("/login")
async def login():
    return {"message": "login"}


@auth_router.post("/login")
async def login(user: LoginModel, response: Response):
    check_user = session.query(User).filter(User.username == user.username).first()

    if check_user and security.check_password_hash(check_user.password, user.password):
        subject = {"username": user.username, "password": user.password, "role": "user"}
        access_token = access_security.create_access_token(subject=subject)
        access_security.set_access_cookie(response, access_token)
        return {"access_token": access_token}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"username yoki password xato")


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


@auth_router.get("/list")
async def users_data(status_code=status.HTTP_200_OK):
    users = session.query(User).all()
    context = [
        {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "username": user.username,
            "is_staff": user.is_staff,
            "is_active": user.is_active,
            # "password": user.password,
        }
        for user in users
    ]
    return jsonable_encoder(context)


@auth_router.get("/me")
async def me(credentials: JwtAuthorizationCredentials = Security(access_security)):
    return {"username": credentials["username"],"password": credentials["password"],"role": credentials["role"]}