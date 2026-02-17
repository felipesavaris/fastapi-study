from http import HTTPStatus

from fastapi import FastAPI

from fastapi_study.schemas import Message

app = FastAPI(title='FastAPI Study', version='0.0.1')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return Message(message='Hello World')
