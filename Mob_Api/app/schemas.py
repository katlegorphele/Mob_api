from pydantic import BaseModel

class Mob_Agent(BaseModel):
    name_sur: str
    email: str
    password: str

    class Config:
        orm_mode = True

class Show_Mob_Agent(BaseModel):
    name_sur: str
    email: str

    class Config:
        orm_mode = True

class Show_Mob_Spectator(BaseModel):
    name_sur: str
    email: str

    class Config:
        orm_mode = True


class Mob_Spectator(BaseModel):
    name_sur: str
    email: str
    password: str

    class Config:
        orm_mode = True