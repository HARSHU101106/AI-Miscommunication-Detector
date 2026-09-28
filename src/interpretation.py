import re


def generate_interpretations(
    text,
    sentiment_result,
    emotion_result,
    ambiguity_result,
    context=""
):
    """
    Generate possible interpretations of a message.

    The goal is to show how the same message could be
    understood differently by another person.
    """

    text_lower = text.lower().strip()

    interpretations = []

    sentiment = sentiment_result["label"].upper()
    emotion = emotion_result["emotion"].lower()
    ambiguity = ambiguity_result["level"]

    # ------------------------------------------------
    # Common short / ambiguous responses
    # ------------------------------------------------

    if text_lower in {"fine", "okay", "ok"}:

        interpretations = [
            "The person may genuinely agree or accept the situation.",
            "The person may be unhappy but may not want to argue.",
            "The person may be trying to end the conversation."
        ]

    elif "whatever" in text_lower:

        interpretations = [
            "The person may be saying that they do not want to continue the discussion.",
            "The person may feel frustrated or ignored.",
            "The person may be expressing that they will accept the other person's decision."
        ]

    elif "maybe" in text_lower:

        interpretations = [
            "The person may be uncertain about the decision.",
            "The person may not want to give a definite answer yet.",
            "The person may be politely avoiding a direct commitment."
        ]

    elif "sure" in text_lower:

        interpretations = [
            "The person may genuinely agree with the request.",
            "The person may be agreeing reluctantly.",
            "The person may be using a short response because they do not want to explain further."
        ]

    # ------------------------------------------------
    # Negative + emotional messages
    # ------------------------------------------------

    elif sentiment == "NEGATIVE" and emotion in {
        "anger",
        "sadness",
        "disgust"
    }:

        interpretations = [
            "The person may be emotionally affected by the situation.",
            "The message may be interpreted as frustration or disappointment.",
            "The other person may perceive the message as more negative than intended."
        ]

    # ------------------------------------------------
    # High ambiguity
    # ------------------------------------------------

    elif ambiguity == "High":

        interpretations = [
            "The message may have multiple possible meanings.",
            "The recipient may need additional context to understand the intended meaning.",
            "The recipient could interpret the message differently depending on the situation."
        ]

    # ------------------------------------------------
    # Medium ambiguity
    # ------------------------------------------------

    elif ambiguity == "Medium":

        interpretations = [
            "The intended meaning is somewhat clear but may depend on context.",
            "The recipient could interpret the tone differently.",
            "Additional explanation could reduce the possibility of misunderstanding."
        ]

    # ------------------------------------------------
    # Context-dependent messages
    # ------------------------------------------------

    elif context.strip():

        interpretations = [
            "The message may be interpreted differently depending on the previous conversation.",
            "The recipient may use the previous conversation to infer the intended meaning.",
            "A little more explanation could make the intended meaning clearer."
        ]

    # ------------------------------------------------
    # Default
    # ------------------------------------------------

    else:

        interpretations = [
            "The message appears relatively clear.",
            "The recipient may interpret the message according to its literal meaning.",
            "The surrounding situation could still influence how the message is understood."
        ]

    return interpretations


# ------------------------------------------------
# Test the interpretation generator
# ------------------------------------------------

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

    context = (
        "Are you coming to the event tomorrow? "
        "We need to book the tickets today."
    )

    result = generate_interpretations(
        text,
        sentiment_result,
        emotion_result,
        ambiguity_result,
        context
    )

    print("\n--- Possible Interpretations ---")

    for i, interpretation in enumerate(result, start=1):

        print(f"{i}. {interpretation}")