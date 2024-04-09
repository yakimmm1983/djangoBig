from pydantic import BaseModel

class UserModal(BaseModel):
    acces_token:str
    login:str
    full_name:str
    id:int
