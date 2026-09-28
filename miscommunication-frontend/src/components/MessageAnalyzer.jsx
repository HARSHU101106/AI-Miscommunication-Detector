import { useState } from "react";
import { motion } from "framer-motion";
import { Loader2, Send, RotateCcw } from "lucide-react";
const REL = ["Friend", "Parent", "Teacher", "Professor", "HR / Interviewer", "Stranger", "Other"];
const MAX = 1000;
export default function MessageAnalyzer({ onAnalyze, loading, error, hasResult, onReset }) {
  const [relationship, setRel] = useState("Friend");
  const [context, setCtx] = useState("");
  const [message, setMsg] = useState("");
  const [vErr, setVErr] = useState("");
  const submit = () => {
    if (!message.trim()) return setVErr("Please type a message first — there's nothing to analyze yet.");
    setVErr(""); onAnalyze({ message: message.trim(), relationship, context: context.trim() });
  };
  const clear = () => { setMsg(""); setCtx(""); setVErr(""); onReset(); };
  return (
    <section id="analyzer"><div className="wrap" style={{ maxWidth: 780 }}>
      <h2>Analyze Your Message</h2>
      <p className="sub">Tell us who you're writing to, add optional context, and see how it might land.</p>
      <motion.div className="glass" initial={{ opacity: 0, y: 30 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}>
        <div className="field"><label htmlFor="rel">Relationship</label>
          <select id="rel" value={relationship} onChange={(e) => setRel(e.target.value)}>{REL.map((r) => <option key={r}>{r}</option>)}</select></div>
        <div className="field"><label htmlFor="ctx">Previous Conversation <span style={{ color: "var(--muted)", fontWeight: 400 }}>(optional)</span></label>
          <textarea id="ctx" value={context} maxLength={2000} onChange={(e) => setCtx(e.target.value)} placeholder="Add previous conversation or context..." /></div>
        <div className="field"><label htmlFor="msg">Your Message</label>
          <textarea id="msg" value={message} maxLength={MAX} onChange={(e) => { setMsg(e.target.value); setVErr(""); }} placeholder="Type the message you're thinking of sending..." aria-invalid={!!vErr} />
          <div className="row"><span className="err">{vErr}</span><span>{message.length}/{MAX}</span></div></div>
        {error && <p className="err" role="alert" style={{ marginBottom: 14 }}>⚠ {error}</p>}
        <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
          <motion.button className="btn" disabled={loading} onClick={submit} whileHover={{ scale: loading ? 1 : 1.03 }} whileTap={{ scale: 0.97 }} style={{ flex: 1, minWidth: 200 }}>
            {loading ? <><Loader2 className="spin" size={18} /> Analyzing with NLP models…</> : <><Send size={18} /> Analyze Message</>}
          </motion.button>
          {(hasResult || message || context) && <button className="btn ghost" onClick={clear} disabled={loading}><RotateCcw size={16} /> New Analysis</button>}
        </div>
      </motion.div>
    </div></section>
  );
}
