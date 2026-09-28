import { motion } from "framer-motion";
import { Copy, Quote } from "lucide-react";
export default function ClearerMessage({ text, onCopied }) {
  if (!text) return null;
  const copy = async () => {
    try { await navigator.clipboard.writeText(text); onCopied("Copied!"); } catch { onCopied("Couldn't copy — select the text manually."); }
  };
  return (
    <div style={{ marginTop: 64 }}>
      <h2>Say It More Clearly</h2>
      <motion.div className="glass" style={{ maxWidth: 720, margin: "24px auto 0", borderColor: "rgba(139,92,246,.5)", boxShadow: "0 0 50px rgba(139,92,246,.18)" }} initial={{ opacity: 0, scale: 0.96 }} whileInView={{ opacity: 1, scale: 1 }} viewport={{ once: true }}>
        <Quote size={26} color="var(--p2)" />
        <p className="quote">{text}</p>
        <div style={{ textAlign: "center" }}><button className="btn" onClick={copy}><Copy size={16} /> Copy Message</button></div>
      </motion.div>
    </div>
  );
}
