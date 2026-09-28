from transformers import pipeline

# Load emotion detection model
emotion_analyzer = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)


def analyze_emotion(text):
    """
    Detect the emotion expressed in the text.
    Returns the emotion and confidence score.
    """

    result = emotion_analyzer(text)[0]

    return {
        "emotion": result["label"],
        "confidence": result["score"]
    }


# Test the emotion analyzer
if __name__ == "__main__":

    text = input("Enter a message: ")

    result = analyze_emotion(text)

    print("\n--- Emotion Analysis ---")
    print("Message:", text)
    print("Emotion:", result["emotion"])
    print(
        "Confidence:",
        round(result["confidence"] * 100, 2),
        "%"
    )