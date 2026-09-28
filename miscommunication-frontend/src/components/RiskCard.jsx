import { useEffect } from "react";
import { motion, useMotionValue, useTransform, animate } from "framer-motion";
import { ShieldAlert } from "lucide-react";
import { levelOf, color } from "./util";
export default function RiskCard({ data }) {
  const score = Math.round(data?.score ?? 0); const lv = levelOf(score, data?.level);
  const v = useMotionValue(0); const R = 80, C = 2 * Math.PI * R;
  const offset = useTransform(v, (x) => C - (x / 100) * C); const text = useTransform(v, (x) => Math.round(x));
  useEffect(() => { const c = animate(v, score, { duration: 1.6, ease: "easeOut" }); return c.stop; }, [score]);
  return (
    <motion.div className="glass risk">
      <div className="ttl" style={{ justifyContent: "center" }}><ShieldAlert size={20} color="var(--p2)" /> Miscommunication Risk</div>
      <div style={{ position: "relative", width: 200, height: 200, margin: "12px auto" }}>
        <svg viewBox="0 0 200 200" width="200" height="200" style={{ transform: "rotate(-90deg)", filter: `drop-shadow(0 0 10px ${color(lv)})` }}>
          <circle cx="100" cy="100" r={R} fill="none" stroke="rgba(255,255,255,.08)" strokeWidth="14" />
          <motion.circle cx="100" cy="100" r={R} fill="none" stroke={color(lv)} strokeWidth="14" strokeLinecap="round" strokeDasharray={C} style={{ strokeDashoffset: offset }} />
        </svg>
        <div style={{ position: "absolute", inset: 0, display: "grid", placeItems: "center" }}>
          <div><motion.span className="big" style={{ fontSize: "3rem" }}>{text}</motion.span><span style={{ color: "var(--muted)" }}> / 100</span></div>
        </div>
      </div>
      <span className="tag" style={{ color: color(lv), fontSize: "1rem", padding: "4px 18px" }}>{data?.level ?? lv} risk</span>
      {data?.reasons?.length > 0 && <ul className="rs" style={{ maxWidth: 520, margin: "16px auto 0", textAlign: "left" }}>{data.reasons.map((r, i) => <li key={i}>{r}</li>)}</ul>}
    </motion.div>
  );
}
