# Student Support Chatbot

An AI-powered chatbot that helps college students with their questions about admissions, fees, exams, scholarships, library, career guidance and general study topics. It is built with Python, Flask and the Google Gemini API.

## Features

- Simple and clean chat interface in the browser
- Answers student questions using the Gemini AI model
- Replies in the same language the student uses (Hindi, Hinglish or English)
- Remembers the earlier messages in a chat, so follow-up questions work
- Shows a friendly message if the AI service is busy or unavailable

## Technologies Used

- Python 3
- Flask (web framework)
- HTML, CSS and JavaScript (chat interface)
- Google Gemini API (`google-genai` library)
- VS Code

## Project Structure

```
Student ChatBot/
├── app.py              # Flask server and chatbot logic
├── templates/
│   └── index.html      # Chat page (frontend)
├── .gitignore
└── README.md
```

## How to Run

1. Install Python 3 from python.org (tick "Add Python to PATH").

2. Install the required libraries:
   ```
   py -m pip install flask google-genai
   ```

3. Get a free API key from Google AI Studio: https://aistudio.google.com

4. Set the API key in the terminal (Windows PowerShell):
   ```
   $env:GEMINI_API_KEY="your_api_key_here"
   ```

5. Start the app:
   ```
   py app.py
   ```

6. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Example Questions

- How do I apply for a scholarship?
- MCA ke baad career options kya hain?
- How can I prepare for exams?
- Fees kaise bharte hain?

## Important Note

Never upload your API key to GitHub. This project reads the key from an environment variable (`GEMINI_API_KEY`), so the key is not stored in the code.

## Future Improvements

- Add a database of college-specific information (fees, timetable, notices)
- Add a login system for students
- Add voice input and output
- Deploy the chatbot online

## Author

Made by [Pranjal Dulhani] as a practical project for MCA.
