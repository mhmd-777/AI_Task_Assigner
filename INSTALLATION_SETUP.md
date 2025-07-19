

⚙️ INSTALLATION \& SETUP GUIDE – SMART RESOURCE ALLOCATOR



Welcome to the Smart Resource Allocator! This document contains step-by-step instructions to help you install, configure, and run the project on your local machine.



&nbsp;PROJECT STRUCTURE

--------------------

AI\_TASK\_ASSIGNER/

├── backend/

│   ├── main.py

│   ├── seed\_employees.py

│   ├── database.py

│   ├── models.py

│   ├── schemas.py

│   ├── rule\_engine.py

│   ├── gpt\_agent.py

│   ├── requirements.txt

├── frontend/

│   ├── login.html

│   ├── index.html

│   ├── employees.html

│   ├── tasks.html

│   ├── styles.css

|   └──scripts/

|       ├── common.js

**|**       ├── employees.js

|       └── tasks.js

|    

└── INSTALLATION\_SETUP.txt



🔧 SETUP INSTRUCTIONS

----------------------



1️⃣ Clone the Repository

------------------------

git clone https://github.com/your-username/AI\_TASK\_ASSIGNER.git



cd AI\_TASK\_ASSIGNER



2️⃣ Create a Virtual Environment

--------------------------------

python -m venv .venv



Activate it:

\- On Windows:

&nbsp; .venv\\Scripts\\activate

\- On Mac/Linux:

&nbsp; source .venv/bin/activate



3️⃣ Install Backend Dependencies

--------------------------------

cd backend

pip install -r requirements.txt



4️⃣ Seed the Employee Database

------------------------------

python seed\_employees.py



5️⃣ Start the FastAPI Server

----------------------------

uvicorn main:app --reload



Visit: http://127.0.0.1:8000/



6️⃣ Open the App in Your Browser

--------------------------------

Login with:

Username: admin

Password: password



7️⃣ View API Docs

-----------------

http://127.0.0.1:8000/docs



🧠 OPTIONAL: AI AGENT CONFIGURATION

----------------------------------

1\. Create a .env file in /backend

2\. Add:

OPENAI\_API\_KEY=your\_openai\_api\_key\_here







✅ YOU’RE DONE!

--------------

You now have a full-stack Smart Resource Allocator app running.





