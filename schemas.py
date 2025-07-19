from pydantic import BaseModel
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str
    skills: str
    availability: str
    experience: int

class Task(BaseModel):
    title: str

class TaskResponse(BaseModel):
    id: int
    title: str
    assigned_to: Optional[int]
    status: str

class UserLogin(BaseModel):
    username: str
    password: str
