import streamlit as st

from src.sentiment import analyze_sentiment
from src.emotion import analyze_emotion
from src.ambiguity import calculate_ambiguity
from src.risk_score import calculate_risk
from src.rewriter import generate_rewrite


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Miscommunication Detector",
    page_icon="🧠",
    layout="centered"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🧠 AI Miscommunication Detector")

st.write(
    "Analyze your message for sentiment, emotion, "
    "ambiguity and potential miscommunication."
)


# --------------------------------------------------
# User inputs
# --------------------------------------------------

relationship = st.selectbox(
    "Who are you talking to?",
    [
        "Friend",
        "Parent",
        "Teacher",
        "Professor",
        "HR / Interviewer",
        "Stranger",
        "Other"
    ]
)

st.write("### Previous Conversation (Optional)")

context = st.text_area(
    "Enter previous message or conversation context",
    placeholder="Example: Are you coming to the event?"
)

st.write("### Your Message")

message = st.text_area(
    "Enter the message you want to analyze",
    placeholder="Example: Fine. Do whatever you want."
)


# --------------------------------------------------
# Analyze button
# --------------------------------------------------

if st.button("🔍 Analyze Message", use_container_width=True):

    if not message.strip():

        st.warning("Please enter a message first.")

    else:

        # ------------------------------------------
        # NLP analysis
        # ------------------------------------------

        sentiment_result = analyze_sentiment(message)

        emotion_result = analyze_emotion(message)

        ambiguity_result = calculate_ambiguity(message)

        risk_result = calculate_risk(
            sentiment_result,
            emotion_result,
            ambiguity_result
        )

        rewritten_message = generate_rewrite(
            message,
            sentiment_result,
            emotion_result,
            ambiguity_result
        )


        # ------------------------------------------
        # Results
        # ------------------------------------------

        st.divider()

        st.subheader("🧠 Analysis")


        # Sentiment
        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Sentiment",
                sentiment_result["label"]
            )

        with col2:

            st.metric(
                "Emotion",
                emotion_result["emotion"].upper()
            )


        # Confidence
        st.write("### Confidence")

        sentiment_confidence = (
            sentiment_result["confidence"] * 100
        )

        emotion_confidence = (
            emotion_result["confidence"] * 100
        )

        st.write(
            f"Sentiment: {sentiment_confidence:.2f}%"
        )

        st.progress(
            sentiment_result["confidence"]
        )

        st.write(
            f"Emotion: {emotion_confidence:.2f}%"
        )

        st.progress(
            emotion_result["confidence"]
        )


        # ------------------------------------------
        # Ambiguity
        # ------------------------------------------

        st.subheader("🔀 Ambiguity")

        st.metric(
            "Ambiguity Level",
            ambiguity_result["level"]
        )

        st.write(
            f"Ambiguity Score: "
            f"{ambiguity_result['score']} / 100"
        )

        if ambiguity_result["reasons"]:

            st.write("**Why?**")

            for reason in ambiguity_result["reasons"]:

                st.write("• " + reason)


        # ------------------------------------------
        # Risk
        # ------------------------------------------

        st.subheader("⚠️ Miscommunication Risk")

        risk_score = risk_result["score"]

        st.metric(
            "Risk Score",
            f"{risk_score} / 100"
        )

        st.write(
            f"Risk Level: **{risk_result['level']}**"
        )

        st.progress(
            risk_score / 100
        )

        if risk_result["reasons"]:

            st.write("**Risk factors:**")

            for reason in risk_result["reasons"]:

                st.write("• " + reason)


        # ------------------------------------------
        # Clearer message
        # ------------------------------------------

        st.subheader("✨ Suggested Clearer Message")

        st.info(rewritten_message)


        # ------------------------------------------
        # Context
        # ------------------------------------------

        if context.strip():

            st.subheader("💬 Conversation Context")

            st.write(context)

        st.caption(
            f"Analysis performed for conversation with: "
            f"{relationship}"
        )