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
    age: Optional[int] = None

class CreatePetResponseModel(BaseModel):
    id: int

class PostPetImageModel(BaseModel):
    id: int
    pic: str

class PostPetImageResponseModel(BaseModel):
    link: str


class PatchPetUpdateModel(BaseModel):
    id: int
    name: Optional[str] = None
    type: Optional[str] = None
    age: Optional[int] = None

class PatchPetUpdateResponseModel(BaseModel):
    id: int