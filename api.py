from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.analyzer import analyze_message


# -----------------------------------------
# Create FastAPI application
# -----------------------------------------

app = FastAPI(
    title="AI Miscommunication Detector API",
    description="NLP API for detecting potential miscommunication",
    version="1.0.0"
)
# -----------------------------------------
# CORS configuration
# -----------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# -----------------------------------------
# Request model
# -----------------------------------------

class MessageRequest(BaseModel):

    message: str

    relationship: str = "Other"

    context: str = ""


# -----------------------------------------
# Root endpoint
# -----------------------------------------

@app.get("/")
def home():

    return {
        "message": "AI Miscommunication Detector API is running!",
        "status": "success"
    }


# -----------------------------------------
# Analysis endpoint
# -----------------------------------------

@app.post("/analyze")
def analyze(request: MessageRequest):

    result = analyze_message(
        message=request.message,
        relationship=request.relationship,
        context=request.context
    )

    return result