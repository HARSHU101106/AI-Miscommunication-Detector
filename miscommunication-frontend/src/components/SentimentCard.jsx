import { motion } from "framer-motion";
import { Gauge } from "lucide-react";
import { pct } from "./util";
export default function SentimentCard({ data }) {
  const p = pct(data?.confidence ?? 0);
  return (
    <motion.div className="glass" whileHover={{ y: -4 }}>
      <div className="ttl"><Gauge size={18} color="var(--p2)" /> Sentiment</div>
      <div className="big" style={{ textTransform: "capitalize" }}>{data?.label ?? "—"}</div>
      <div className="bar"><motion.div initial={{ width: 0 }} animate={{ width: `${p}%` }} transition={{ duration: 1 }} style={{ background: "linear-gradient(90deg,var(--p),var(--p2))" }} /></div>
      <span style={{ color: "var(--muted)" }}>{p}% confidence</span>
    </motion.div>
  );
}
