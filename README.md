# 🧠 AI Miscommunication Detector

### Beyond the Words — Understand What Your Messages Really Mean

An AI-powered communication analysis tool designed to identify potential misunderstandings in text messages by analyzing sentiment, emotions, ambiguity, and context.

The application helps users understand how their messages might be interpreted, identify possible communication risks, and express themselves more clearly through AI-assisted message rewriting.

---

## 📌 Project Overview

Miscommunication is a common challenge in digital conversations. A short message can sometimes convey unintended emotions, create confusion, or lead to misunderstandings.

The **AI Miscommunication Detector** addresses this problem by combining Natural Language Processing (NLP), pretrained language models, and rule-based analysis to examine the meaning and tone of a message.

Rather than simply analyzing words, the system considers multiple factors to provide an explainable interpretation of potential communication issues.

---

## ✨ Key Features

- **Sentiment Analysis:** Identifies the overall emotional polarity of a message.
- **Emotion Detection:** Detects emotions such as joy, sadness, anger, fear, surprise, and neutral expression.
- **Ambiguity Detection:** Identifies vague or unclear expressions that may lead to different interpretations.
- **Context Analysis:** Considers relationship and conversational context to understand how a message may be perceived.
- **Miscommunication Risk Score:** Generates a heuristic score based on multiple analysis components.
- **Possible Interpretations:** Provides alternative ways a message might be understood.
- **AI-Assisted Message Rewriting:** Suggests clearer and more considerate alternatives to reduce potential misunderstandings.
- **Interactive Web Interface:** Presents analysis results through a user-friendly React application.
- **REST API:** Uses FastAPI to connect the frontend with the Python analysis engine.

---

## 🛠️ Tech Stack

| Category             | Technologies                                    |
| -------------------- | ----------------------------------------------- |
| Programming Language | Python                                          |
| Frontend             | React.js, Vite, CSS                             |
| Backend              | FastAPI                                         |
| NLP                  | Hugging Face Transformers                       |
| Machine Learning     | Pretrained Language Models                      |
| Sentiment Analysis   | NLP-based sentiment classification              |
| Emotion Detection    | `j-hartmann/emotion-english-distilroberta-base` |
| API Communication    | REST API, JSON                                  |
| Development Tools    | VS Code, Git, GitHub                            |

---

## 🏗️ Project Architecture

```text
AI-Miscommunication-Detector/
│
├── src/
│   ├── analyzer.py
│   ├── sentiment.py
│   ├── emotion.py
│   ├── ambiguity.py
│   ├── context.py
│   ├── risk_score.py
│   ├── interpretation.py
│   ├── rewriter.py
│   └── __init__.py
│
├── miscommunication-frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── data/
├── models/
├── api.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### How It Works

1. The user enters a message and provides relevant conversational details.
2. The React frontend sends the input to the FastAPI backend.
3. The Python analysis engine processes the message through different modules.
4. Sentiment, emotion, ambiguity, and context are evaluated.
5. The system calculates a miscommunication risk score.
6. Possible interpretations and a clearer rewritten message are generated.
7. The results are returned to the frontend and displayed to the user.

---

## ⚙️ Installation and Setup

### Prerequisites

Make sure the following tools are installed:

- Python
- Node.js and npm
- Git
- Visual Studio Code

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Miscommunication-Detector.git
```

Navigate to the project directory:

```bash
cd AI-Miscommunication-Detector
```

### 2. Set Up the Python Backend

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows using Git Bash:

```bash
source venv/Scripts/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI Server

From the project root directory, run:

```bash
uvicorn api:app --reload --port 8000
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

### 4. Access API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

Use the documentation to explore and test the available endpoints.

### 5. Set Up the React Frontend

Open a second terminal and navigate to the frontend directory:

```bash
cd miscommunication-frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:5173
```

**Note:** The frontend's API URL should point to the running backend. For local development, the expected URL is `http://127.0.0.1:8000`.

---

## 🔌 API Endpoints

| Method | Endpoint   | Description                                |
| ------ | ---------- | ------------------------------------------ |
| GET    | `/`        | Checks whether the backend is running      |
| POST   | `/analyze` | Analyzes a message and returns the results |

### Example Request

```json
{
  "message": "Fine.",
  "relationship": "Friend",
  "context": "Are you coming to the event tomorrow? We need to book the tickets today."
}
```

### Example Response Structure

The analysis endpoint returns information such as:

- Sentiment analysis
- Detected emotions
- Ambiguity score
- Context analysis
- Miscommunication risk score
- Possible interpretations
- Suggested rewritten message

The exact response depends on the input message and analysis results.

---

## 🧪 Example Use Case

**Original Message:**

> Fine.

**Potential Issue:**

Although the message is short and appears neutral, its meaning can vary depending on the relationship, context, and previous conversation.

**What the Detector Does:**

- Analyzes the sentiment and emotional signals.
- Examines the ambiguity of the expression.
- Considers the conversational context.
- Identifies possible interpretations.
- Suggests a clearer alternative when appropriate.

This helps users consider how their words might be perceived before sending a message.

---

## 🎯 Project Objectives

- Reduce potential misunderstandings in digital communication.
- Explore practical applications of NLP and pretrained language models.
- Combine machine learning with rule-based analysis.
- Improve awareness of emotional tone and ambiguous expressions.
- Demonstrate the integration of a Python AI backend with a modern web frontend.
- Build an explainable and accessible AI-powered communication assistant.

---

## 🚀 Future Enhancements

- Multilingual miscommunication detection.
- Improved ambiguity detection using transformer-based models.
- Personalized communication suggestions.
- Conversation history and trend analysis.
- Support for longer conversations.
- More advanced context-aware rewriting.
- Deployment with a publicly accessible API and frontend.
- Evaluation using a labeled miscommunication dataset.

---

## ⚠️ Limitations

The miscommunication risk score is a heuristic indicator, not a scientifically calibrated probability of misunderstanding. Emotion and sentiment predictions may also be imperfect, particularly when messages contain sarcasm, cultural references, or insufficient context.

The tool is intended to support communication awareness rather than determine a person's actual intentions.

---

## 👩‍💻 Developed By

**Harshini S**

B.Sc. Computer Science with Artificial Intelligence
SDNB Vaishnav College for Women, Chennai

BS in Data Science and Applications
IIT Madras

---

## 📄 License

This project is developed for educational and portfolio purposes. A license can be added to define the terms under which others may use, modify, or distribute the project.

---

⭐ If you find this project interesting, consider starring the repository!
