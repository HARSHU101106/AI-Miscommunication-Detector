from .sentiment import analyze_sentiment
from .emotion import analyze_emotion
from .ambiguity import calculate_ambiguity
from .context import analyze_context
from .risk_score import calculate_risk
from .interpretation import generate_interpretations
from .rewriter import generate_rewrite


def analyze_message(message, relationship="Other", context=""):
    """
    Run the complete AI Miscommunication Detection pipeline.

    Parameters:
        message (str): User's message.
        relationship (str): Relationship with the recipient.
        context (str): Previous conversation context.

    Returns:
        dict: Complete analysis result.
    """

    # -----------------------------------------
    # 1. Sentiment
    # -----------------------------------------

    sentiment_result = analyze_sentiment(message)

    # -----------------------------------------
    # 2. Emotion
    # -----------------------------------------

    emotion_result = analyze_emotion(message)

    # -----------------------------------------
    # 3. Ambiguity
    # -----------------------------------------

    ambiguity_result = calculate_ambiguity(message)

    # -----------------------------------------
    # 4. Context
    # -----------------------------------------

    context_result = analyze_context(
        context,
        message,
        relationship
    )

    # -----------------------------------------
    # 5. Miscommunication Risk
    # -----------------------------------------

    risk_result = calculate_risk(
        sentiment_result,
        emotion_result,
        ambiguity_result,
        context_result
    )

    # -----------------------------------------
    # 6. Possible Interpretations
    # -----------------------------------------

    interpretations = generate_interpretations(
        message,
        sentiment_result,
        emotion_result,
        ambiguity_result,
        context
    )

    # -----------------------------------------
    # 7. Clearer Rewrite
    # -----------------------------------------

    rewritten_message = generate_rewrite(
        message,
        sentiment_result,
        emotion_result,
        ambiguity_result
    )

    # -----------------------------------------
    # 8. Return complete result
    # -----------------------------------------

    return {
        "message": message,
        "relationship": relationship,

        "sentiment": sentiment_result,

        "emotion": emotion_result,

        "ambiguity": ambiguity_result,

        "context": context_result,

        "risk": risk_result,

        "interpretations": interpretations,

        "rewritten_message": rewritten_message
    }


# -----------------------------------------
# Test the complete analyzer
# -----------------------------------------

if __name__ == "__main__":

    message = input("Enter your message: ")

    relationship = input(
        "Who are you talking to? "
    )

    context = input(
        "Previous conversation (optional): "
    )

    result = analyze_message(
        message,
        relationship,
        context
    )

    print("\n================================")
    print(" AI MISCOMMUNICATION ANALYSIS")
    print("================================")

    print("\nMessage:")
    print(result["message"])

    print("\nSentiment:")
    print(result["sentiment"])

    print("\nEmotion:")
    print(result["emotion"])

    print("\nAmbiguity:")
    print(result["ambiguity"])

    print("\nContext:")
    print(result["context"])

    print("\nRisk:")
    print(result["risk"])

    print("\nPossible Interpretations:")

    for i, interpretation in enumerate(
        result["interpretations"],
        start=1
    ):
        print(f"{i}. {interpretation}")

    print("\nClearer Message:")
    print(result["rewritten_message"])