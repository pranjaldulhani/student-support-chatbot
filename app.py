import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# API key terminal se leta hai (Step: $env:GEMINI_API_KEY="apni_key")
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-3.5-flash"

# Bot ko batate hain ki woh kaun hai aur kaise jawab dena hai
SYSTEM_PROMPT = (
    "You are a friendly Student Support Chatbot for college students. "
    "Help with admissions, fees, exams, timetable, scholarships, library, "
    "career guidance and general study questions. "
    "Reply in the same language the student uses (Hindi, Hinglish or English). "
    "Keep answers short, simple and clear."
)

# Chat session (pichhli baatein yaad rakhta hai)
chat = client.chats.create(
    model=MODEL,
    config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_message = request.json["message"]
    try:
        response = chat.send_message(user_message)
        reply = response.text
    except Exception as e:
        reply = "Maaf kijiye, abhi jawab nahi de paaya. Error: " + str(e)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)