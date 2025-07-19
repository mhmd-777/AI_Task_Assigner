import os
import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def suggest_best_fit(task, candidates):
    prompt = f"""
You are a helpful AI HR agent. Assign a task to the best-fit employee based on their skills, experience, and availability.

Task: {task.title}

Candidates:
{[(e.name, e.skills, e.experience, e.availability) for e in candidates]}

Return the name of the best-fit employee and a short reason.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": "You are a helpful HR assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error calling AI Agent: {str(e)}"
