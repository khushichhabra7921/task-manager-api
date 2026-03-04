import os
import requests
from groq import Groq

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
PR_NUMBER = os.environ["PR_NUMBER"]
REPO = os.environ["REPO"]

# Get PR diff from GitHub
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.diff"
}
diff_url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"
response = requests.get(diff_url, headers=headers)
diff = response.text[:8000]  # limit size

# Send to Groq for review
client = Groq(api_key=GROQ_API_KEY)

prompt = f"""You are an expert software engineer doing a code review.
Review the following code diff and provide feedback on:
1. Bugs or logical errors
2. Security issues
3. Code quality and best practices
4. Performance concerns
5. Any quick wins or improvements

Be specific and constructive. Format your response with clear sections.

CODE DIFF:
{diff}"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=1000
)

review = response.choices[0].message.content

# Post review as PR comment
comment_url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
headers["Accept"] = "application/vnd.github.v3+json"
payload = {"body": f"## 🤖 AI Code Review\n\n{review}"}
requests.post(comment_url, json=payload, headers=headers)
print("AI review posted successfully!")
