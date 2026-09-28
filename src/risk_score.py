def calculate_risk(
    sentiment_result,
    emotion_result,
    ambiguity_result,
    context_result
):
    """
    Calculate the overall miscommunication risk using
    sentiment, emotion, ambiguity, and conversation context.
    """

    score = 0
    reasons = []

    # --------------------------------
    # 1. Sentiment contribution
    # --------------------------------

    if sentiment_result["label"] == "NEGATIVE":

        score += 20

        reasons.append(
            "Negative sentiment detected."
        )

    # --------------------------------
    # 2. Emotion contribution
    # --------------------------------

    emotion = emotion_result["emotion"].lower()

    high_risk_emotions = {
        "anger",
        "fear",
        "sadness",
        "disgust"
    }

    medium_risk_emotions = {
        "surprise"
    }

    if emotion in high_risk_emotions:

        score += 20

        reasons.append(
            f"Emotion detected: {emotion}."
        )

    elif emotion in medium_risk_emotions:

        score += 10

        reasons.append(
            f"Emotion detected: {emotion}."
        )

    # --------------------------------
    # 3. Ambiguity contribution
    # --------------------------------

    ambiguity_score = ambiguity_result["score"]

    ambiguity_contribution = int(
        ambiguity_score * 0.30
    )

    score += ambiguity_contribution

    if ambiguity_result["level"] == "High":

        reasons.append(
            "High ambiguity detected."
        )

    elif ambiguity_result["level"] == "Medium":

        reasons.append(
            "Moderate ambiguity detected."
        )

    # --------------------------------
    # 4. Context contribution
    # --------------------------------

    context_score = context_result["score"]

    context_contribution = int(
        context_score * 0.30
    )

    score += context_contribution

    if context_result["level"] == "High":

        reasons.append(
            "The message depends strongly on conversation context."
        )

    elif context_result["level"] == "Medium":

        reasons.append(
            "The previous conversation may affect interpretation."
        )

    # --------------------------------
    # 5. Keep score between 0 and 100
    # --------------------------------

    score = min(score, 100)

    # --------------------------------
    # 6. Determine risk level
    # --------------------------------

    if score >= 70:

        level = "High"

    elif score >= 40:

        level = "Medium"

    else:

        level = "Low"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }


# --------------------------------
# Test the risk calculator
# --------------------------------

if __name__ == "__main__":

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

    context_result = {
        "score": 55,
        "level": "Medium",
        "reasons": []
    }

    result = calculate_risk(
        sentiment_result,
        emotion_result,
        ambiguity_result,
        context_result
    )

    print("\n--- Miscommunication Risk ---")

    print(
        "Risk Score:",
        result["score"],
        "/ 100"
    )

    print(
        "Risk Level:",
        result["level"]
    )

    print("\nReasons:")

    for reason in result["reasons"]:

        print("-", reason)