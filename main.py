from fastapi import FastAPI, Body
from fastapi.responses import FileResponse, JSONResponse
import uvicorn

from app.models.user import user, User, IsAdultUser
from app.models.feedback import Feeback, FeedbackResponce

app = FastAPI()


@app.get('/', response_class=FileResponse)
async def root():
    return FileResponse('./app/statics/html/index.html')


@app.post('/calculate', response_class=JSONResponse)
async def root(num1: int = Body(embed=True), num2: int = Body(embed=True)):
    return JSONResponse(f'result: {num1 + num2}')


@app.get('/users', response_model=User)
async def root():
    return user


@app.post('/user', response_model=IsAdultUser)
async def root(user: User):
    responce = IsAdultUser(**user.model_dump())
    responce.is_adult = True if user.age >= 18 else False

    return responce


@app.post('/feedback', response_model=FeedbackResponce)
async def root(feedback: Feeback):
    if feedback.message == None:
        return FeedbackResponce(message=f"Feedback is not received. Repeat, {feedback.name}!")
    else:
        return FeedbackResponce(message=f"Feedback is received. Thank you, {feedback.name}!")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
