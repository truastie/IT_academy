from typing import Optional
from pydantic import BaseModel


class PetResponseModel(BaseModel):
    id: int

class LoginResponseModel(BaseModel):
    token: Optional[str] = None
    email: str
    id: int

class LoginModel(BaseModel):
    email: Optional[str]
    password: Optional[str]

# class InnerModel(BaseModel):
#     a: str
#
#
# class OuterResponseModel(BaseModel):
#     detail:Optional[InnerModel]

# a= {
#     detail: {
#         a:str
#     }
# }

class RegisterModel(BaseModel):
    email: Optional[str]
    password: Optional[str]
    confirm_password: Optional[str]

class RegisterResponseModel(BaseModel):
    token: Optional[str] = None
    email: str
    id: int


class DeletePetModel(BaseModel):
    id: Optional[int] = None

class DeleteResponsePetModel(BaseModel):
    id: Optional[int] = None

class CreatePetModel(BaseModel):
    name: str
    type: str
    age: int

class CreatePetResponseModel(BaseModel):
    id: int
    name: str
    type: str
    age: int

class PostPetImageModel(BaseModel):
    id: int
    pic: str

class PostPetImageResponseModel(BaseModel):
    link: str


class PatchPetUpdateModel(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

class PatchPetUpdateResponseModel(BaseModel):
    id: Optional[int] = None