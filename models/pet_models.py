from typing import Optional

from pydantic import BaseModel


class PetResponseModel(BaseModel):
    id: int


class LoginResponseModel(BaseModel):
    token: Optional[str]
    email: str
    id: int

class LoginModel(BaseModel):
    email: Optional[str]
    password: Optional[str]

class InnerModel(BaseModel):
    a: str


class OuterResponseModel(BaseModel):
    detail:Optional[InnerModel]

# a= {
#     detail: {
#         a:str
#     }
# }