from fastapi import FastAPI, Body
from fastapi.responses import FileResponse, JSONResponse
import uvicorn


from app.models.feedback import Feeback, FeedbackResponce
from app.routers.product import product_router
from app.routers.user import user_router

app = FastAPI()

app.include_router(product_router)
app.include_router(user_router)


@app.get('/', response_class=FileResponse)
async def root():
    return FileResponse('./app/statics/html/index.html')


@app.post('/calculate', response_class=JSONResponse)
async def root(num1: int = Body(embed=True), num2: int = Body(embed=True)):
    return JSONResponse(f'result: {num1 + num2}')


@app.post('/feedback', response_model=FeedbackResponce)
async def root(feedback: Feeback):
    if feedback.message == None:
        return FeedbackResponce(message=f"Feedback is not received. Repeat, {feedback.name}!")
    else:
        return FeedbackResponce(message=f"Feedback is received. Thank you, {feedback.name}!")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
