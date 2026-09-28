import { motion } from "framer-motion";
import { Split, Link2, Lightbulb } from "lucide-react";
import SentimentCard from "./SentimentCard"; import EmotionCard from "./EmotionCard"; import ScoreCard from "./ScoreCard";
import RiskCard from "./RiskCard"; import Interpretations from "./Interpretations"; import ClearerMessage from "./ClearerMessage";
export default function AnalysisResults({ loading, result, hasContext, onCopied }) {
  if (!loading && !result) return null;
  return (
    <section id="results" style={{ paddingTop: 0 }}><div className="wrap">
      <h2>Your Communication Analysis</h2>
      {loading ? (
        <div className="grid" style={{ marginTop: 32 }}>{[0, 1, 2, 3].map((i) => <div key={i} className="skel" />)}</div>
      ) : (
        <motion.div initial={{ opacity: 0, y: 40 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
          <div className="grid" style={{ marginTop: 32 }}>
            <RiskCard data={result.risk} />
            <SentimentCard data={result.sentiment} /><EmotionCard data={result.emotion} />
            <ScoreCard title="Ambiguity" icon={Split} data={result.ambiguity} />
            <ScoreCard title="Context Dependency" icon={Link2} data={result.context} />
          </div>
          <Interpretations items={result.interpretations} />
          <ClearerMessage text={result.rewritten_message} onCopied={onCopied} />
          {hasContext && result.context?.reasons?.length > 0 && (
            <motion.div className="glass" style={{ maxWidth: 720, margin: "48px auto 0" }} initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} viewport={{ once: true }}>
              <div className="ttl"><Lightbulb size={18} color="var(--p2)" /> Why Context Matters</div>
              <ul className="rs">{result.context.reasons.map((r, i) => <li key={i}>{r}</li>)}</ul>
            </motion.div>
          )}
        </motion.div>
      )}
    </div></section>
  );
}
