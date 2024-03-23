from fastapi import FastAPI
import uvicorn
from chapter7.pycode import UserCreate

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Available APIs: create_user"}


@app.post("/create_user/")
async def create_user(user_data: UserCreate):
    user_id = user_data.user_id
    return {"message": "Received parameters succesfully", "user_id": user_id}


@app.get("/user/{value}")
async def get_user(value: int):
    user_id = value
    return {"message": "Received parameters succesfully", "user_id": user_id}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
