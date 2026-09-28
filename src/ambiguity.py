import re


# Words and phrases that can make a message vague
VAGUE_WORDS = {
    "okay",
    "fine",
    "sure",
    "whatever",
    "maybe",
    "probably",
    "perhaps",
    "later",
    "soon",
    "interesting",
    "nice",
    "great"
}


def calculate_ambiguity(text):
    """
    Calculate a simple ambiguity score based on
    vague words, short messages, and uncertainty.
    """

    text_lower = text.lower().strip()

    words = re.findall(r"\b\w+\b", text_lower)

    if not words:
        return {
            "score": 0,
            "level": "Low",
            "reasons": []
        }

    score = 0
    reasons = []

    # 1. Check for vague words
    vague_found = [word for word in words if word in VAGUE_WORDS]

    if vague_found:
        score += 30
        reasons.append(
            f"Vague wording detected: {', '.join(vague_found)}"
        )

    # 2. Very short messages can depend heavily on context
    if len(words) <= 3:
        score += 25
        reasons.append(
            "The message is very short and may depend on context."
        )

    # 3. Question marks can indicate uncertainty
    if "?" in text:
        score += 15
        reasons.append(
            "The message contains a question or uncertainty."
        )

    # 4. Ellipsis can indicate incomplete meaning
    if "..." in text:
        score += 15
        reasons.append(
            "Ellipsis may indicate an incomplete or uncertain tone."
        )

    # 5. Keep score within 0-100
    score = min(score, 100)

    # Determine ambiguity level
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


# Test the ambiguity detector
if __name__ == "__main__":

    text = input("Enter a message: ")

    result = calculate_ambiguity(text)

    print("\n--- Ambiguity Analysis ---")
    print("Message:", text)
    print("Ambiguity Score:", result["score"], "/ 100")
    print("Ambiguity Level:", result["level"])

    if result["reasons"]:
        print("\nWhy?")

        for reason in result["reasons"]:
            print("-", reason)