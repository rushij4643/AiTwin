# 🤖 AI Digital Twin

An AI-powered Digital Twin that represents me professionally and answers questions about my background, skills, education, projects, and experience.

Built using **Google Gemini 3.1 Flash Lite**, **Gradio**, and the **OpenAI-compatible Gemini API**, this project allows recruiters, employers, and visitors to interact with an AI version of me through a web interface.

---

## 🚀 Features

- 🤖 Powered by **Google Gemini 3.1 Flash Lite**
- 💬 Interactive chatbot built with Gradio
- 📄 Uses my LinkedIn profile and personal summary as knowledge
- 🧠 Answers questions about:
  - Education
  - Skills
  - Projects
  - Experience
  - Career goals
- 📧 Automatically records visitor email addresses
- 📲 Sends Pushover notifications when someone wants to connect
- ❓ Records unknown questions for future improvements
- 🌐 Deployable on Render

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- OpenAI Compatible API
- Gradio
- PyPDF
- python-dotenv
- Requests

---

## 📂 Project Structure

```
Digital-Twin/
│
├── app.py
├── context.py
├── tools.py
├── styles.py
├── requirements.txt
├── linkedin.pdf
├── summary.txt
├── emails.txt
├── .env
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file with:

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

PUSHOVER_USER=YOUR_PUSHOVER_USER
PUSHOVER_TOKEN=YOUR_PUSHOVER_TOKEN
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

Move into the project

```bash
cd your-repository
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

The application will launch in your browser.

---

## 🌐 Render Deployment

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
python app.py
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| GOOGLE_API_KEY | Google Gemini API Key |
| PUSHOVER_USER | Pushover User Key |
| PUSHOVER_TOKEN | Pushover API Token |
| GRADIO_SERVER_NAME | 0.0.0.0 |
| GRADIO_SERVER_PORT | 10000 |

---

## 💡 How It Works

1. Loads my LinkedIn profile (`linkedin.pdf`)
2. Loads my personal summary (`summary.txt`)
3. Builds a system prompt representing my professional profile
4. Uses Gemini 3.1 Flash Lite to answer user questions
5. Records visitor emails to `emails.txt`
6. Sends Pushover notifications for new contacts
7. Logs unknown questions for future improvements

---

## 📌 Example Questions

- Tell me about yourself.
- What technologies do you know?
- Tell me about your projects.
- What programming languages do you use?
- How can I contact you?
- What are your career goals?

---

## 📈 Future Improvements

- Persistent database for visitor details
- Resume upload support
- Portfolio integration
- Voice interaction
- Multi-language support
- RAG-based knowledge retrieval
- Analytics dashboard

---

## 👨‍💻 Author

**Rushi Jadhav**

B.Tech Information Technology Student

Interested in:

- Artificial Intelligence
- Agentic AI
- Software Development
- Java
- Data Structures & Algorithms
- Cloud Computing

---

## 📄 License

This project is intended for educational and portfolio purposes.
