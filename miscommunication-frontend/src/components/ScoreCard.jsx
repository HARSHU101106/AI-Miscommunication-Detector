import { motion } from "framer-motion";
import { levelOf, color } from "./util";
// Reusable card for Ambiguity and Context Dependency
export default function ScoreCard({ title, icon: Icon, data }) {
  const s = Math.round(data?.score ?? 0); const lv = levelOf(s, data?.level);
  return (
    <motion.div className="glass" whileHover={{ y: -4 }}>
      <div className="ttl"><Icon size={18} color="var(--p2)" /> {title}</div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
        <span className="big">{s}<small style={{ fontSize: "1rem", color: "var(--muted)" }}> / 100</small></span>
        <span className="tag" style={{ color: color(lv) }}>{data?.level ?? lv}</span>
      </div>
      <div className="bar"><motion.div initial={{ width: 0 }} animate={{ width: `${s}%` }} transition={{ duration: 1 }} style={{ background: color(lv) }} /></div>
      {data?.reasons?.length > 0 && <ul className="rs">{data.reasons.map((r, i) => <li key={i}>{r}</li>)}</ul>}
    </motion.div>
  );
}
