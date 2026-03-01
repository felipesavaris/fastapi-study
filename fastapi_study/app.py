from http import HTTPStatus

from fastapi import FastAPI

from fastapi_study.schemas import Message, UserSchemaIn, UserSchemaOut

app = FastAPI(title='FastAPI Study', version='0.0.1')

memory_database: list = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return Message(message='Hello World')


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserSchemaOut)
def create_user(user: UserSchemaIn):
    user_withn_id = UserSchemaOut(id=len(memory_database) + 1, **user.model_dump(exclude={'id'}))
    memory_database.append(user_withn_id)

    # return UserSchemaOut(**user.model_dump())
    return user_withn_id
