from database import Base
from sqlalchemy import Boolean, Column, Integer, String, Text, ForeignKey, DateTime
from datetime import datetime

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    skills = Column(Text)
    availability = Column(String)
    experience = Column(Integer)
    assigned_task = Column(String, default="None")
    tasks_completed = Column(Text, default="")  # comma-separated task titles

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    assigned_to = Column(Integer, nullable=True)
    completed = Column(Boolean, default=False)