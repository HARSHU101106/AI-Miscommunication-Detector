# 🧠 AI Miscommunication Detector

### Beyond the Words — Understand What Your Messages Really Mean

An NLP-based communication analysis tool that identifies potential misunderstandings in text messages by analyzing sentiment, emotion, ambiguity, and conversational context.

The application helps users understand how their messages might be interpreted, spot possible communication risks, and express themselves more clearly through suggested rewrites. Every score comes with human-readable reasons, so the analysis is **explainable rather than a black box**.

---

## 📌 Project Overview

Miscommunication is a common challenge in digital conversations. A short message such as "Fine." or "Sure" can convey unintended emotions, create confusion, or lead to misunderstanding, depending on who sends it and what came before.

The **AI Miscommunication Detector** addresses this by running every message through a multi-stage, rule-based NLP pipeline. Rather than judging words alone, it considers the message, the relationship between sender and recipient, and the previous conversation, then combines these signals into a single risk assessment.

---

## ✨ Key Features

- **Sentiment Analysis:** Classifies the overall polarity of a message (positive, negative, neutral) using a lexicon with negation and intensifier handling.
- **Emotion Detection:** Detects joy, sadness, anger, fear, surprise, disgust, or neutral expression using emotion vocabularies.
- **Ambiguity Detection:** Flags vague wording, very short messages, questions, and ellipses that can lead to multiple interpretations.
- **Context Analysis:** Considers the previous conversation and the relationship (friend, teacher, HR, stranger, etc.) to judge how much the meaning depends on context.
- **Miscommunication Risk Score:** A weighted heuristic score from 0 to 100 with a Low / Medium / High level and the reasons behind it.
- **Possible Interpretations:** Shows alternative ways the recipient might understand the message.
- **Clearer Message Suggestion:** Offers a more explicit rewrite for common ambiguous expressions.
- **Interactive Web Interface:** A React application that presents each result as its own animated card.
- **REST API:** A FastAPI backend that connects the frontend to the Python analysis engine.

---

## 🛠️ Tech Stack

| Category | Technologies |
| -------- | ------------ |
| Language | Python 3 |
| Backend | FastAPI, Uvicorn, Pydantic |
| NLP approach | Rule-based / lexicon-based analysis (no external model downloads) |
| Frontend | React 18, Vite 5, Framer Motion, Lucide React, CSS |
| API communication | REST, JSON, CORS |
| Deployment | Frontend configured for Vercel |
| Development tools | VS Code, Git, GitHub |

> **Design note:** The analysis modules are intentionally transparent heuristics. This keeps the app lightweight, fast, and fully explainable. Replacing the sentiment and emotion modules with transformer models is listed under [Future Enhancements](#-future-enhancements).

---

## 🏗️ Project Architecture

```text
AI-Miscommunication-Detector/
│
├── src/
│   ├── analyzer.py          # Orchestrates the full pipeline
│   ├── sentiment.py         # Lexicon-based sentiment with negation/intensifiers
│   ├── emotion.py           # Emotion vocabulary matching
│   ├── ambiguity.py         # Ambiguity score and reasons
│   ├── context.py           # Context and relationship analysis
│   ├── risk_score.py        # Weighted miscommunication risk score
│   ├── interpretation.py    # Possible interpretations
│   ├── rewriter.py          # Clearer message suggestions
│   └── __init__.py
│
├── miscommunication-frontend/
│   ├── src/
│   │   ├── components/      # Hero, MessageAnalyzer, AnalysisResults, cards, etc.
│   │   ├── services/api.js  # Backend API client
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── data/
├── models/
├── api.py                   # FastAPI application
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 How It Works

1. The user enters a message, selects their relationship with the recipient, and optionally adds the previous conversation.
2. The React frontend sends this to the FastAPI backend (`POST /analyze`).
3. `analyzer.py` runs the message through the pipeline below.
4. The combined result is returned as JSON and displayed as result cards.

### The Analysis Pipeline

| Stage | Module | What it does |
| ----- | ------ | ------------ |
| 1. Sentiment | `sentiment.py` | Counts positive and negative words. Words after a negation (within two words) flip polarity; intensifiers such as "very" add weight. |
| 2. Emotion | `emotion.py` | Matches words against six emotion vocabularies. Ties or no matches return `neutral`. |
| 3. Ambiguity | `ambiguity.py` | +30 for vague words, +25 for messages of three words or fewer, +15 for a question mark, +15 for an ellipsis (max 100). |
| 4. Context | `context.py` | +30 when a short message follows a longer conversation, +25 for context-dependent words (e.g. "it", "that", "fine"), +10 for formal relationships. Returns "Unknown" when no context is given. |
| 5. Risk | `risk_score.py` | Negative sentiment (+20), high-risk emotion (+20; surprise +10), 30% of the ambiguity score, 30% of the context score. |
| 6. Interpretations | `interpretation.py` | Selects likely interpretations based on common phrases, sentiment, emotion, and ambiguity level. |
| 7. Rewrite | `rewriter.py` | Suggests a clearer version for common ambiguous expressions and emotional messages. |

### Risk Levels

| Score | Level |
| ----- | ----- |
| 0 – 39 | Low |
| 40 – 69 | Medium |
| 70 – 100 | High |

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.9 or newer
- Node.js and npm
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/HARSHU101106/AI-Miscommunication-Detector.git
cd AI-Miscommunication-Detector
```

### 2. Set Up the Python Backend

Create and activate a virtual environment.

Windows (Git Bash):

```bash
python -m venv venv
source venv/Scripts/activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI Server

From the project root:

```bash
uvicorn api:app --reload --port 8000
```

The backend runs at `http://127.0.0.1:8000`.

### 4. Explore the API Docs

FastAPI provides interactive Swagger documentation at:

```text
http://127.0.0.1:8000/docs
```

### 5. Set Up the React Frontend

In a second terminal:

```bash
cd miscommunication-frontend
npm install
npm run dev
```

Open the URL shown in the terminal, usually `http://localhost:5173`.

### 6. Configure the API URL (optional)

By default the frontend calls `http://127.0.0.1:8000`. To point it at a deployed backend, create `miscommunication-frontend/.env`:

```text
VITE_API_URL=https://your-backend-url.example.com
```

### Run the Pipeline from the Command Line

You can also test the engine without the web app:

```bash
python -m src.analyzer
```

Each module in `src/` also has its own test block, for example `python -m src.ambiguity`.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/` | Health check: confirms the backend is running |
| POST | `/analyze` | Analyzes a message and returns the full result |

### Request Body

| Field | Type | Required | Description |
| ----- | ---- | -------- | ----------- |
| `message` | string | Yes | The message to analyze |
| `relationship` | string | No (default `"Other"`) | Friend, Parent, Teacher, Professor, HR / Interviewer, Stranger, Other |
| `context` | string | No (default `""`) | Previous conversation |

### Example Request

```json
{
  "message": "Whatever",
  "relationship": "Friend",
  "context": "Are you coming to the event tomorrow? We need to book the tickets today."
}
```

### Example Response

```json
{
  "message": "Whatever",
  "relationship": "Friend",
  "sentiment": { "label": "NEUTRAL", "confidence": 0.5 },
  "emotion": { "emotion": "neutral", "confidence": 0.5 },
  "ambiguity": {
    "score": 55,
    "level": "Medium",
    "reasons": [
      "Vague wording detected: whatever",
      "The message is very short and may depend on context."
    ]
  },
  "context": {
    "score": 55,
    "level": "Medium",
    "reasons": [
      "The short message may depend on the previous conversation.",
      "The message contains context-dependent wording: Whatever"
    ]
  },
  "risk": {
    "score": 32,
    "level": "Low",
    "reasons": [
      "Moderate ambiguity detected.",
      "The previous conversation may affect interpretation."
    ]
  },
  "interpretations": [
    "The person may be saying that they do not want to continue the discussion.",
    "The person may feel frustrated or ignored.",
    "The person may be expressing that they will accept the other person's decision."
  ],
  "rewritten_message": "I may not completely agree with this, but I respect your decision."
}
```

---

## 🧪 Example Use Case

**Original message:** "Whatever"

**Potential issue:** Although short and apparently neutral, the message could mean agreement, frustration, or withdrawal depending on the relationship and the earlier conversation.

**What the detector does:**

- Finds no strong sentiment or emotion words.
- Flags the vague wording and very short length (ambiguity: Medium).
- Notes that the message depends on the previous conversation (context: Medium).
- Lists three plausible interpretations from the recipient's side.
- Suggests a clearer alternative the sender could use instead.

---

## 🎯 Project Objectives

- Reduce potential misunderstandings in digital communication.
- Explore practical NLP techniques for tone, ambiguity, and context analysis.
- Build an explainable system where every score has visible reasons.
- Demonstrate integration of a Python backend with a modern React frontend.

---

## ⚠️ Limitations

- The risk score is a **heuristic indicator**, not a scientifically calibrated probability of misunderstanding.
- Sentiment and emotion detection rely on fixed vocabularies, so messages without recognized keywords default to neutral, and sarcasm, slang, and cultural references are not captured.
- Some interpretation and rewrite rules match specific phrases and may not trigger for unusual wording or punctuation.
- Rewrites are templates, not personalized to the sender's actual intent.
- English only.

The tool is intended to support communication awareness, not to determine a person's actual intentions.

---

## 🚀 Future Enhancements

- Replace the lexicon-based sentiment and emotion modules with transformer models (for example, a Hugging Face emotion classifier such as `j-hartmann/emotion-english-distilroberta-base`).
- Normalize punctuation and casing before phrase matching.
- Evaluate the risk score against a labeled miscommunication dataset and calibrate the weights.
- Context-aware rewriting using a language model.
- Multilingual support.
- Conversation history and trend analysis.
- Public deployment of the backend and frontend.

---

## 👩‍💻 Developed By

**Harshini S**

B.Sc. Computer Science with Artificial Intelligence, SDNB Vaishnav College for Women, Chennai
BS in Data Science and Applications, IIT Madras

---

## 📄 License

This project is developed for educational and portfolio purposes. A license can be added to define the terms under which others may use, modify, or distribute it.
