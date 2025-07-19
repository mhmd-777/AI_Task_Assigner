from database import SessionLocal, engine
from models import Employee
from sqlalchemy.orm import Session

# Create tables if they don't exist
Employee.__table__.create(bind=engine, checkfirst=True)

# Start DB session
db: Session = SessionLocal()

# Sample employee data (30+ diverse profiles)
sample_employees = [
    {"name": "Alice Johnson", "skills": "Python, SQL, Machine Learning", "availability": "full-time", "experience": 5},
    {"name": "Bob Smith", "skills": "HTML, CSS, JavaScript", "availability": "part-time", "experience": 3},
    {"name": "Charlie Brown", "skills": "C++, Embedded Systems, Microcontrollers", "availability": "full-time", "experience": 4},
    {"name": "Diana Prince", "skills": "Project Management, Agile, Communication", "availability": "full-time", "experience": 7},
    {"name": "Ethan Hunt", "skills": "Python, Flask, REST APIs", "availability": "contract", "experience": 2},
    {"name": "Fiona Gallagher", "skills": "SQL, Power BI, Data Analysis", "availability": "full-time", "experience": 6},
    {"name": "George Michael", "skills": "React, JavaScript, TypeScript", "availability": "freelance", "experience": 3},
    {"name": "Hannah Baker", "skills": "UI/UX, Figma, Adobe XD", "availability": "part-time", "experience": 2},
    {"name": "Ivan Petrov", "skills": "Python, TensorFlow, Deep Learning", "availability": "full-time", "experience": 5},
    {"name": "Julia Roberts", "skills": "Java, Spring Boot, REST APIs", "availability": "contract", "experience": 4},
    {"name": "Kevin Malone", "skills": "Excel, Accounting, Data Entry", "availability": "part-time", "experience": 8},
    {"name": "Liam Neeson", "skills": "Cybersecurity, Penetration Testing, Networking", "availability": "freelance", "experience": 9},
    {"name": "Maria Garcia", "skills": "PHP, Laravel, MySQL", "availability": "full-time", "experience": 5},
    {"name": "Noah Davis", "skills": "Python, Django, PostgreSQL", "availability": "part-time", "experience": 4},
    {"name": "Olivia Benson", "skills": "Law, Investigation, Conflict Resolution", "availability": "contract", "experience": 10},
    {"name": "Paul Walker", "skills": "Cloud, AWS, DevOps", "availability": "full-time", "experience": 6},
    {"name": "Quincy Adams", "skills": "Node.js, Express, MongoDB", "availability": "freelance", "experience": 3},
    {"name": "Rachel Green", "skills": "Retail, Customer Service, Communication", "availability": "part-time", "experience": 2},
    {"name": "Steve Rogers", "skills": "Leadership, Strategy, Public Speaking", "availability": "full-time", "experience": 12},
    {"name": "Tina Fey", "skills": "Writing, Editing, Journalism", "availability": "contract", "experience": 7},
    {"name": "Uma Thurman", "skills": "Graphic Design, Photoshop, Illustrator", "availability": "freelance", "experience": 5},
    {"name": "Victor Hugo", "skills": "C#, .NET, SQL Server", "availability": "full-time", "experience": 6},
    {"name": "Wanda Maximoff", "skills": "React, Redux, GraphQL", "availability": "part-time", "experience": 4},
    {"name": "Xander Cage", "skills": "Extreme Sports, Filmmaking, Editing", "availability": "contract", "experience": 3},
    {"name": "Yara Shahidi", "skills": "Event Planning, Marketing, Social Media", "availability": "full-time", "experience": 2},
    {"name": "Zack Snyder", "skills": "Film Direction, Editing, Storyboarding", "availability": "freelance", "experience": 10},
    {"name": "Abby Miller", "skills": "Python, SQL, Data Science", "availability": "full-time", "experience": 4},
    {"name": "Ben Hardy", "skills": "Machine Learning, NLP, AI", "availability": "part-time", "experience": 5},
    {"name": "Carmen Sandiego", "skills": "Strategy, Planning, Intelligence", "availability": "contract", "experience": 8},
    {"name": "Doug Funny", "skills": "Sketching, Animation, Creativity", "availability": "freelance", "experience": 2}
]

# Insert only if table is empty
if db.query(Employee).count() == 0:
    for emp in sample_employees:
        new_emp = Employee(
            name=emp["name"],
            skills=emp["skills"],
            availability=emp["availability"],
            experience=emp["experience"],
            assigned_task="None",
            tasks_completed=""
        )
        db.add(new_emp)
    db.commit()
    print(f"✅ {len(sample_employees)} employees seeded successfully.")
else:
    print("ℹ️ Database already contains employees. No action taken.")

db.close()
