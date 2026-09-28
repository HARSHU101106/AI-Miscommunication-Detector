from transformers import pipeline

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")


def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.
    Returns the sentiment label and confidence score.
    """

    result = sentiment_analyzer(text)[0]

    return {
        "label": result["label"],
        "confidence": result["score"]
    }


# Test the function
if __name__ == "__main__":

    text = input("Enter a message: ")

    result = analyze_sentiment(text)

    print("\n--- Sentiment Analysis ---")
    print("Message:", text)
    print("Sentiment:", result["label"])
    print(
        "Confidence:",
        round(result["confidence"] * 100, 2),
        "%"
    )