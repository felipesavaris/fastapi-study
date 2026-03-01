from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_study.schemas import Message, UserList, UserSchemaIn, UserSchemaOut

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


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def retrieve_users():
    return UserList(users=memory_database)


@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserSchemaOut)
def update_user(user_id: int, user: UserSchemaIn):
    if not memory_database:
        return HTMLResponse(content='No users found', status_code=HTTPStatus.NOT_FOUND)

    for index, user_in_db in enumerate(memory_database):
        if user_in_db.id == user_id:
            updated_user = UserSchemaOut(id=user_id, **user.model_dump(exclude={'id'}))
            memory_database[index] = updated_user
            return updated_user

    return HTMLResponse(content='User not found', status_code=HTTPStatus.NOT_FOUND)


@app.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):
    if not memory_database:
        return HTMLResponse(content='No users found', status_code=HTTPStatus.NOT_FOUND)

    for index, user_in_db in enumerate(memory_database):
        if user_in_db.id == user_id:
            del memory_database[index]
            return None

    return HTMLResponse(content='User not found', status_code=HTTPStatus.NOT_FOUND)
