import re


def analyze_context(context, message, relationship):
    """
    Analyze whether the meaning of a message may depend
    on previous conversation and relationship.
    """

    context = context.strip()
    message = message.strip()

    reasons = []
    score = 0

    # -----------------------------------------
    # No context provided
    # -----------------------------------------

    if not context:
        return {
            "score": 0,
            "level": "Unknown",
            "reasons": [
                "No previous conversation was provided."
            ]
        }

    # -----------------------------------------
    # Compare message length with context
    # -----------------------------------------

    message_words = re.findall(r"\b\w+\b", message)
    context_words = re.findall(r"\b\w+\b", context)

    if len(message_words) <= 3 and len(context_words) >= 5:
        score += 30

        reasons.append(
            "The short message may depend on the previous conversation."
        )

    # -----------------------------------------
    # Detect context-dependent words
    # -----------------------------------------

    context_dependent_words = {
        "okay",
        "fine",
        "that",
        "this",
        "it",
        "there",
        "later",
        "sure",
        "whatever",
        "yes",
        "no"
    }

    found_words = [
        word
        for word in message_words
        if word.lower() in context_dependent_words
    ]

    if found_words:

        score += 25

        reasons.append(
            "The message contains context-dependent wording: "
            + ", ".join(found_words)
        )

    # -----------------------------------------
    # Relationship factor
    # -----------------------------------------

    if relationship in {
        "HR / Interviewer",
        "Teacher",
        "Professor",
        "Stranger"
    }:

        score += 10

        reasons.append(
            "The relationship may require clearer communication."
        )

    # -----------------------------------------
    # Limit score
    # -----------------------------------------

    score = min(score, 100)

    # -----------------------------------------
    # Determine level
    # -----------------------------------------

    if score >= 60:
        level = "High"

    elif score >= 30:
        level = "Medium"

    else:
        level = "Low"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }


# -----------------------------------------
# Test
# -----------------------------------------

if __name__ == "__main__":

    context = input("Previous conversation: ")

    message = input("Your message: ")

    relationship = input("Relationship: ")

    result = analyze_context(
        context,
        message,
        relationship
    )

    print("\n--- Context Analysis ---")

    print("Context Score:", result["score"], "/ 100")
    print("Context Level:", result["level"])

    print("\nReasons:")

    for reason in result["reasons"]:
        print("-", reason)