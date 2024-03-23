from pydantic import BaseModel


def convertToList(arr):
    arr_list = list(arr)
    return arr_list


def hello(name):
    return "Hello: " + str(name)


class UserCreate(BaseModel):
    user_id: int
