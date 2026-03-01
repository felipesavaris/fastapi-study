from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchemaOut(BaseModel):
    id: int | None = None
    username: str
    email: EmailStr


class UserSchemaIn(UserSchemaOut):
    password: str
