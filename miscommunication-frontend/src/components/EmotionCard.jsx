import { motion } from "framer-motion";
import { Smile, Frown, Angry, Meh, Heart, Ghost, Laugh } from "lucide-react";
import { pct } from "./util";
const icons = { joy: Laugh, happy: Laugh, sadness: Frown, sad: Frown, anger: Angry, angry: Angry, fear: Ghost, love: Heart, surprise: Smile, neutral: Meh };
export default function EmotionCard({ data }) {
  const name = data?.emotion ?? "—"; const Icon = icons[String(name).toLowerCase()] || Meh; const p = pct(data?.confidence ?? 0);
  return (
    <motion.div className="glass" whileHover={{ y: -4 }}>
      <div className="ttl"><Icon size={18} color="var(--p2)" /> Emotion</div>
      <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
        <motion.div animate={{ scale: [1, 1.12, 1] }} transition={{ duration: 2.5, repeat: Infinity }} style={{ padding: 12, borderRadius: 16, background: "rgba(139,92,246,.18)" }}><Icon size={30} color="var(--p2)" /></motion.div>
        <div><div className="big" style={{ textTransform: "capitalize" }}>{name}</div><span style={{ color: "var(--muted)" }}>{p}% confidence</span></div>
      </div>
      <div className="bar"><motion.div initial={{ width: 0 }} animate={{ width: `${p}%` }} transition={{ duration: 1 }} style={{ background: "var(--p2)" }} /></div>
    </motion.div>
  );
}
