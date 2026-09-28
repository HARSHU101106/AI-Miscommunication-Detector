
import re

# Lightweight sentiment vocabulary
POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "awesome",
    "happy", "love", "wonderful", "fantastic", "beautiful",
    "nice", "kind", "perfect", "excited", "glad",
    "thankful", "grateful", "appreciate", "enjoy",
    "success", "hopeful", "helpful", "supportive",
    "brilliant", "delightful", "pleased", "welcome"
}

NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "horrible", "sad",
    "angry", "hate", "disappointed", "upset", "annoyed",
    "frustrated", "worried", "fear", "scared", "sorry",
    "unfortunately", "wrong", "fail", "failure",
    "boring", "rude", "hurt", "confused", "stress",
    "stressful", "lonely", "regret", "useless", "poor"
}

NEGATIONS = {
    "not", "never", "no", "hardly", "isn't", "wasn't",
    "don't", "doesn't", "didn't", "can't", "couldn't",
    "won't", "wouldn't"
}

INTENSIFIERS = {
    "very", "really", "extremely", "absolutely",
    "so", "too", "incredibly"
}


def analyze_sentiment(text):
    """
    Analyze sentiment using lightweight word-based rules.

    Returns:
        label: POSITIVE, NEGATIVE, or NEUTRAL
        confidence: heuristic confidence score between 0 and 1
    """

    if not text or not text.strip():
        return {
            "label": "NEUTRAL",
            "confidence": 0.5
        }

    words = re.findall(r"\b[\w']+\b", text.lower())

    positive_score = 0
    negative_score = 0

    for i, word in enumerate(words):

        # Check for a negation in the preceding two words
        previous_words = words[max(0, i - 2):i]
        is_negated = any(w in NEGATIONS for w in previous_words)

        # Check for an intensifier immediately before the word
        is_intensified = (
            i > 0 and words[i - 1] in INTENSIFIERS
        )

        weight = 1.5 if is_intensified else 1.0

        if word in POSITIVE_WORDS:
            if is_negated:
                negative_score += weight
            else:
                positive_score += weight

        elif word in NEGATIVE_WORDS:
            if is_negated:
                positive_score += weight
            else:
                negative_score += weight

    total_score = positive_score + negative_score

    if total_score == 0:
        return {
            "label": "NEUTRAL",
            "confidence": 0.5
        }

    if positive_score > negative_score:
        label = "POSITIVE"
        confidence = 0.5 + (
            0.5 * positive_score / total_score
        )

    elif negative_score > positive_score:
        label = "NEGATIVE"
        confidence = 0.5 + (
            0.5 * negative_score / total_score
        )

    else:
        label = "NEUTRAL"
        confidence = 0.5

    return {
        "label": label,
        "confidence": round(confidence, 4)
    }


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