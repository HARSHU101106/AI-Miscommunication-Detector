import { motion } from "framer-motion";
const stages = [
  "Your Message",
  "Sentiment",
  "Emotion",
  "Ambiguity",
  "Context",
  "Risk Assessment",
  "Possible Interpretations",
  "Clearer Message",
];
const tech = [
  "Python",
  "FastAPI",
  "Hugging Face Transformers",
  "NLP",
  "Sentiment Analysis",
  "Emotion Detection",
  "Rule-based Ambiguity Detection",
  "Context Analysis",
  "Miscommunication Risk Scoring",
  "Message Rewriting",
];
export default function HowItWorks() {
  return (
    <>
      <section id="how">
        <div className="wrap">
          <h2>How It Works</h2>
          <p className="sub">
            Every message travels through an eight-stage analysis pipeline.
          </p>
          <div className="pipe">
            <div
              style={{
                position: "absolute",
                left: "50%",
                top: 0,
                bottom: 0,
                width: 2,
                background: "rgba(255,255,255,.08)",
              }}
            />
            <motion.div
              style={{
                position: "absolute",
                left: "50%",
                width: 2,
                height: 60,
                background:
                  "linear-gradient(transparent,var(--p2),transparent)",
                boxShadow: "0 0 12px var(--p)",
              }}
              animate={{ top: ["0%", "92%"] }}
              transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
            />
            {stages.map((s, i) => (
              <motion.div
                key={s}
                className="stage"
                style={{ position: "relative", background: "var(--bg2)" }}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.08 }}
                whileHover={{ borderColor: "var(--p)", scale: 1.03 }}
              >
                <span
                  style={{
                    color: "var(--p2)",
                    marginRight: 10,
                    fontWeight: 700,
                  }}
                >
                  {i + 1}
                </span>
                {s}
              </motion.div>
            ))}
          </div>
        </div>
      </section>
      <section id="about">
        <div className="wrap">
          <h2>Beyond The Words...</h2>
          <p className="sub">
            Built with AI and Advanced language models to uncover hidden
            emotions, identify ambiguity, and help you communicate with clarity.
          </p>
          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              gap: 12,
              justifyContent: "center",
            }}
          >
            {tech.map((t) => (
              <motion.span
                key={t}
                className="badge"
                whileHover={{ scale: 1.06 }}
              >
                {t}
              </motion.span>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
