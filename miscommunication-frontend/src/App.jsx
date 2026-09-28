import { useState, useEffect, useRef } from "react";
import { AnimatePresence, motion } from "framer-motion";
import Navbar from "./components/Navbar"; import Hero from "./components/Hero";
import MessageAnalyzer from "./components/MessageAnalyzer"; import AnalysisResults from "./components/AnalysisResults";
import HowItWorks from "./components/HowItWorks"; import Footer from "./components/Footer";
import { analyzeMessage } from "./services/api";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [hadContext, setHadContext] = useState(false);
  const [toast, setToast] = useState("");
  const timer = useRef();
  const showToast = (m) => { setToast(m); clearTimeout(timer.current); timer.current = setTimeout(() => setToast(""), 2200); };

  const run = async ({ message, relationship, context }) => {
    setLoading(true); setError(""); setResult(null); setHadContext(!!context);
    setTimeout(() => document.getElementById("results")?.scrollIntoView({ behavior: "smooth" }), 100);
    try { setResult(await analyzeMessage(message, relationship, context)); }
    catch (e) { setError(e.message); }
    finally { setLoading(false); }
  };
  useEffect(() => () => clearTimeout(timer.current), []);

  return (<>
    <Navbar /><Hero />
    <MessageAnalyzer onAnalyze={run} loading={loading} error={error} hasResult={!!result} onReset={() => { setResult(null); setError(""); }} />
    <AnalysisResults loading={loading} result={result} hasContext={hadContext} onCopied={showToast} />
    <HowItWorks /><Footer />
    <AnimatePresence>{toast && <motion.div className="toast" role="status" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }}>{toast}</motion.div>}</AnimatePresence>
  </>);
}
