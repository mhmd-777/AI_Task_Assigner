from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Employee, Task as TaskModel
from schemas import EmployeeCreate, Task, UserLogin
from rule_engine import filter_employees
from gpt_agent import suggest_best_fit

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend"), name="static")


@app.get("/")
def serve_index():
    return FileResponse(os.path.join("../frontend", "login.html"))


@app.post("/login")
def login(user: UserLogin):
    if user.username == "admin" and user.password == "password":
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# === EMPLOYEE ROUTES ===

@app.get("/employees/")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


@app.post("/employees/")
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    new_emp = Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    return {"message": "Employee added"}


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}


@app.post("/employees/{employee_id}/clear-task")
def clear_employee_task(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp.assigned_task = "None"
    db.commit()
    return {"message": f"Task cleared for {emp.name}"}


# === TASK ROUTES ===

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(TaskModel).all()


@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()


@app.post("/tasks")
def create_task(task: Task, db: Session = Depends(get_db)):
    new_task = TaskModel(title=task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Deleted"}


@app.post("/tasks/{task_id}/complete")
def mark_complete(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.completed = True
    db.commit()
    return {"message": "Marked complete"}


# === TASK ASSIGNMENT (AI + RULE) ===

@app.post("/assign-task/ai")
def assign_task_ai(task: Task, db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    result = suggest_best_fit(task, employees)

    best_name = None
    best_id = None
    for emp in employees:
        if emp.name.lower() in result.lower():
            best_name = emp.name
            best_id = emp.id
            emp.assigned_task = task.title
            db.commit()
            break

    task_rec = db.query(TaskModel).filter(TaskModel.title == task.title).first()
    if task_rec and best_id:
        task_rec.assigned_to = best_id
        db.commit()

    return {"method": "AI Agent", "result": result, "assigned_to": best_name}


@app.post("/assign-task/rule")
def assign_task_rule(task: Task, db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    task_keywords = [kw.strip().lower() for kw in task.title.split()]

    best_match = None
    highest_score = 0

    for emp in employees:
        emp_skills = [s.strip().lower() for s in emp.skills.split(',')]
        match_score = sum(1 for kw in task_keywords if any(kw in skill for skill in emp_skills))

        if task.title.lower() in (emp.tasks_completed or "").lower():
            match_score += 2

        if match_score > highest_score:
            highest_score = match_score
            best_match = emp

    if best_match and highest_score > 0:
        best_match.assigned_task = task.title
        task_rec = db.query(TaskModel).filter(TaskModel.title == task.title).first()
        if task_rec:
            task_rec.assigned_to = best_match.id
        db.commit()
        return {
            "method": "Rule-Based",
            "best_fits": best_match.name,
            "match_score": highest_score
        }

    return {
        "method": "Rule-Based",
        "best_fits": "No matching employee found",
        "match_score": 0
    }
