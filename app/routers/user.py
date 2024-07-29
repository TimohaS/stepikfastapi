from fastapi import APIRouter, Cookie
from fastapi.responses import JSONResponse
from app.models.user import user, User, IsAdultUser, CreateUser, UserLogin, user_login, session_token_base


user_router = APIRouter(tags=["User"], prefix='/user',
                        default_response_class=JSONResponse)


@user_router.get('/users', response_model=User)
async def root(session_token: str | None = Cookie(default=None)):
    if session_token == session_token_base:
        return user
    else:
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})


@user_router.post('/user', response_model=IsAdultUser)
async def root(user: User):
    responce = IsAdultUser(**user.model_dump())
    responce.is_adult = True if user.age >= 18 else False

    return responce


@user_router.post('/create_user', response_model=CreateUser)
async def root(user: CreateUser):
    return user


@user_router.post('/login')
async def root(user: UserLogin):
    if user.login == user_login["username"] and user.password == user_login["password"]:
        response = JSONResponse(content={"message": "Authorized."})
        response.set_cookie(key="session_token", value='1234', max_age=60)

        return response
    else:
        return JSONResponse(content={"message": "Wrong password or email."})
