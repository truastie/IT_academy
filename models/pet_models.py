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
    email: Optional[str] = None
    password: Optional[str] = None
    confirm_password: Optional[str] = None

class RegisterResponseModel(BaseModel):
    token: Optional[str] = None
    email: Optional[str] = None
    id: Optional[int] = None


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


class PostPetImageModel(BaseModel):
    id: int
    pic: str

class PostPetImageResponseModel(BaseModel):
    link: str


class PatchPetUpdateModel(BaseModel):
    id: int
    name: str
    type: str
    age: int
    gender: str

class PatchPetUpdateResponseModel(BaseModel):
    id: int