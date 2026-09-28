import { motion } from "framer-motion";
import { MessageCircle, Brain, Eye, Users } from "lucide-react";
const icons = [MessageCircle, Brain, Eye, Users];
export default function Interpretations({ items }) {
  if (!items?.length) return null;
  return (
    <div style={{ marginTop: 64 }}>
      <h2>How Could They Interpret This?</h2><p className="sub">Different readers can take the same words in very different ways.</p>
      <div className="grid">
        {items.map((t, i) => { const I = icons[i % 4]; return (
          <motion.div key={i} className="glass" initial={{ opacity: 0, y: 30 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: i * 0.15 }} whileHover={{ y: -4 }}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 10 }}>
              <span style={{ color: "var(--p2)", fontWeight: 800, fontSize: "1.4rem" }}>{String(i + 1).padStart(2, "0")}</span><I size={22} color="var(--p2)" />
            </div>
            <p>{typeof t === "string" ? t : t.text || t.interpretation || JSON.stringify(t)}</p>
          </motion.div>); })}
      </div>
    </div>
  );
}
