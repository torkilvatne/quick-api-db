from typing import List, Optional

from pydantic import BaseModel


#class MarkBase(BaseModel):
#    id:int
#    mark:int
#    subject:str
#
#class Mark(MarkBase):
#    owner_id: int
#
#    class Config:
#        orm_mode = True

class StudentBase(BaseModel):
    id:int
    first_name:str
    last_name:str
    city:str
    phone:str
    gender:str
    email:str
    address:str
    postcode:int

class Student(StudentBase):
    #marks: List[Mark] = []

    class Config:
        orm_mode = True