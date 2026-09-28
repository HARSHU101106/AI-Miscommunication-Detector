
import re

# Lightweight emotion vocabulary
EMOTION_WORDS = {
    "joy": {
        "happy", "joy", "excited", "delighted", "cheerful",
        "wonderful", "love", "enjoy", "pleased", "glad",
        "grateful", "thankful", "thrilled", "smile",
        "laugh", "celebrate", "proud", "hopeful"
    },

    "sadness": {
        "sad", "unhappy", "lonely", "cry", "crying",
        "heartbroken", "grief", "miss", "disappointed",
        "depressed", "miserable", "hopeless", "upset",
        "hurt", "regret", "lost"
    },

    "anger": {
        "angry", "furious", "annoyed", "irritated",
        "frustrated", "rage", "hate", "mad", "outraged",
        "resentful", "irritating", "unfair"
    },

    "fear": {
        "afraid", "scared", "fear", "nervous", "anxious",
        "worried", "terrified", "panic", "uncertain",
        "unsafe", "threatened", "frightened"
    },

    "surprise": {
        "surprised", "shocked", "astonished", "unexpected",
        "amazed", "wow", "unbelievable", "suddenly",
        "incredible", "astonishing"
    },

    "disgust": {
        "disgusted", "gross", "revolting", "nasty",
        "repulsive", "sickening", "disturbing",
        "dislike", "awful"
    }
}


def analyze_emotion(text):
    """
    Detect emotion using lightweight word-based rules.

    Returns:
        emotion: detected emotion or neutral
        confidence: heuristic confidence score between 0 and 1
    """

    if not text or not text.strip():
        return {
            "emotion": "neutral",
            "confidence": 0.5
        }

    words = re.findall(r"\b[\w']+\b", text.lower())

    emotion_scores = {
        emotion: 0
        for emotion in EMOTION_WORDS
    }

    for word in words:
        for emotion, vocabulary in EMOTION_WORDS.items():
            if word in vocabulary:
                emotion_scores[emotion] += 1

    highest_score = max(emotion_scores.values())

    if highest_score == 0:
        return {
            "emotion": "neutral",
            "confidence": 0.5
        }

    # Find all emotions tied for the highest score
    top_emotions = [
        emotion
        for emotion, score in emotion_scores.items()
        if score == highest_score
    ]

    if len(top_emotions) > 1:
        return {
            "emotion": "neutral",
            "confidence": 0.5
        }

    detected_emotion = top_emotions[0]

    total_matches = sum(emotion_scores.values())

    confidence = 0.5 + (
        0.5 * highest_score / total_matches
    )

    return {
        "emotion": detected_emotion,
        "confidence": round(confidence, 4)
    }


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