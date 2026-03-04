from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def prioritize_tasks(tasks: list) -> str:
    if not tasks:
        return "No tasks to prioritize."
    
    task_list = "\n".join([
        f"- ID {t.id}: '{t.title}' | Status: {t.status} | Due: {t.due_date} | Description: {t.description or 'None'}"
        for t in tasks
    ])
    
    prompt = f"""You are a productivity assistant. Analyze these tasks and provide a smart priority order.

Tasks:
{task_list}

Respond in this exact format:
PRIORITY ORDER:
1. [Task ID] - [Title] - [One line reason why this is most urgent]
2. [Task ID] - [Title] - [reason]
(continue for all tasks)

SUMMARY:
[2-3 sentences of overall advice for the user]"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    return response.choices[0].message.content