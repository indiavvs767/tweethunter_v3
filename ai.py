import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_dm(username, bio=""):
    prompt = f"""
    Write a friendly, professional Twitter DM.
    Keep it short (1–2 lines).
    Username: @{username}
    Bio: {bio}
    Tone: helpful, non-salesy, human.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()