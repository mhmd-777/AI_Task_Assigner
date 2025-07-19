# 🤖 Smart Resource Allocator

**Smart Resource Allocator** is a web-based system designed to assign tasks to the most suitable employees using either:
- ✅ Rule-Based Filtering
- 🧠 AI Agent Assistance (via GPT-4.1 Nano model)

It combines human logic and AI to ensure efficient resource allocation in teams and organizations.

---

## 🔧 Features

- 🔐 **Admin Login**
- 👥 **Employee Management**
  - Add, view, or delete employees
  - View assigned task status
- 📋 **Task Management**
  - Add, delete, and mark tasks as complete
  - View task-assignment status
- 🧠 **Task Assignment Modes**
  - **AI Agent**: Uses GPT-4 Nano to determine the best fit
  - **Rule-Based**: Matches based on skills and previous task history
- 📊 **Clear Visual Feedback**
  - Real-time updates to UI after actions (e.g., assignments, completions)
- 🌐 **Single Page Navigation** (Fully frontend-backend connected)

---

## 🚀 Technologies Used

| Layer         | Tools & Technologies                               |
|---------------|----------------------------------------------------|
| Frontend      | HTML, CSS, JavaScript (Vanilla), Fetch API         |
| Backend       | Python, FastAPI, Uvicorn, Pydantic, SQLite         |
| Database      | SQLite (via SQLAlchemy ORM)                        |
| AI Logic      | GPT-4.1 Nano model (simulated in `gpt_agent.py`)   |
| Rule Engine   | Custom filtering logic in `rule_engine.py`         |

---
