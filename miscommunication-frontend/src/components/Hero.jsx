import { motion } from "framer-motion";
import { Sparkles, MessageCircle, Smile, Frown, Zap } from "lucide-react";
const bubbles = [
  { t: "“Fine.”", x: "8%", y: "22%", I: MessageCircle }, { t: "Neutral 62%", x: "80%", y: "18%", I: Smile },
  { t: "“Sure, whatever.”", x: "74%", y: "70%", I: MessageCircle }, { t: "Risk: High", x: "10%", y: "72%", I: Zap },
  { t: "Sadness", x: "45%", y: "10%", I: Frown },
];
const dots = Array.from({ length: 24 }, (_, i) => ({ x: (i * 37) % 100, y: (i * 53) % 100, d: 3 + (i % 5) }));
export default function Hero() {
  return (
    <section id="home" className="hero">
      <motion.div className="orb" animate={{ scale: [1, 1.12, 1], opacity: [0.8, 1, 0.8] }} transition={{ duration: 6, repeat: Infinity }} />
      <svg style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0.25 }} aria-hidden="true">
        {dots.slice(0, 12).map((a, i) => <line key={i} x1={`${a.x}%`} y1={`${a.y}%`} x2={`${dots[i + 12].x}%`} y2={`${dots[i + 12].y}%`} stroke="#A78BFA" strokeWidth=".5" />)}
      </svg>
      {dots.map((d, i) => <motion.span key={i} className="dot" style={{ left: `${d.x}%`, top: `${d.y}%` }} animate={{ opacity: [0.2, 1, 0.2] }} transition={{ duration: d.d, repeat: Infinity }} />)}
      {bubbles.map((b, i) => (
        <motion.div key={i} className="float" style={{ left: b.x, top: b.y }} animate={{ y: [0, -12, 0] }} transition={{ duration: 4 + i, repeat: Infinity, ease: "easeInOut" }}>
          <b.I size={14} style={{ verticalAlign: -2, marginRight: 6 }} />{b.t}
        </motion.div>
      ))}
      <motion.div className="in wrap" initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }}>
        <span className="badge"><Sparkles size={14} /> AI-Powered Communication Intelligence</span>
        <h1>Understand What Your <span>Message Really Means.</span></h1>
        <p>AI-powered communication analysis that detects ambiguity, emotional tone, context dependency, and potential miscommunication before you hit send.</p>
        <motion.button className="btn" whileHover={{ scale: 1.04 }} whileTap={{ scale: 0.97 }} onClick={() => document.getElementById("analyzer")?.scrollIntoView({ behavior: "smooth" })}>Analyze a Message</motion.button>
      </motion.div>
    </section>
  );
}
