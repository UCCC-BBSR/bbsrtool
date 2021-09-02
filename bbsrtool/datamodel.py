import pydantic
from typing import List
from enum import Enum

class ContactRole(Enum):
    PI = "PI"
    primary_contact = "Primary Contact"

class Person(pydantic.BaseModel):
    email: pydantic.EmailStr
    name: str

class PIPerson(Person):
    role: ContactRole=ContactRole.PI

class Project(pydantic.BaseModel):
    title: str
    description: str
    pi: PIPerson
    additional_contacts: List[Person]
