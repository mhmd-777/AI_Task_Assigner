def filter_employees(employees, task_title):
    # Simple rule: Assign to available employees with matching skills
    task_keywords = task_title.lower().split()
    
    return [
        emp for emp in employees
        if (any(keyword in emp.skills.lower() for keyword in task_keywords)
            and emp.availability.lower() == "full-time")
    ]