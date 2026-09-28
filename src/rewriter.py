def generate_rewrite(text, sentiment_result, emotion_result, ambiguity_result):
    """
    Generate a clearer version of a potentially
    confusing message.
    """

    emotion = emotion_result["emotion"].lower()
    sentiment = sentiment_result["label"].upper()
    ambiguity = ambiguity_result["level"]

    # -----------------------------------------
    # Common ambiguous expressions
    # -----------------------------------------

    text_lower = text.lower().strip()

    if "whatever" in text_lower:
        return (
            "I may not completely agree with this, "
            "but I respect your decision."
        )

    if text_lower in ["okay", "ok", "fine"]:
        return (
            "I understand. I would like to discuss this "
            "a little more before making a decision."
        )

    if "maybe" in text_lower:
        return (
            "I'm not completely sure yet. "
            "Let me think about it and get back to you."
        )

    if "later" in text_lower:
        return (
            "I can't do this right now, but I can discuss it "
            "with you at a specific time later."
        )

    # -----------------------------------------
    # Negative + emotional messages
    # -----------------------------------------

    if sentiment == "NEGATIVE" and emotion in {
        "anger",
        "sadness",
        "disgust"
    }:
        return (
            "I'm feeling a little upset about this situation. "
            "I'd like to explain how I feel so we can understand "
            "each other better."
        )

    # -----------------------------------------
    # High ambiguity
    # -----------------------------------------

    if ambiguity == "High":
        return (
            "I want to make sure my message is clear. "
            "What I mean is that I would like to discuss "
            "this situation more clearly."
        )

    # -----------------------------------------
    # Default
    # -----------------------------------------

    return text


# -----------------------------------------
# Test the rewriter
# -----------------------------------------

if __name__ == "__main__":

    text = input("Enter a message: ")

    sentiment_result = {
        "label": "NEGATIVE",
        "confidence": 0.92
    }

    emotion_result = {
        "emotion": "anger",
        "confidence": 0.78
    }

    ambiguity_result = {
        "score": 70,
        "level": "High",
        "reasons": []
    }

    rewritten = generate_rewrite(
        text,
        sentiment_result,
        emotion_result,
        ambiguity_result
    )

    print("\n--- Suggested Clearer Message ---")
    print(rewritten)