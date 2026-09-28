import { useState } from "react";
import { Menu, X } from "lucide-react";
const links = [["Home", "home"], ["Analyze", "analyzer"], ["How It Works", "how"], ["About", "about"]];
export default function Navbar() {
  const [open, setOpen] = useState(false);
  const go = (id) => { setOpen(false); document.getElementById(id)?.scrollIntoView({ behavior: "smooth" }); };
  return (
    <nav><div className="wrap nav">
      <a className="logo" href="#home" onClick={(e) => { e.preventDefault(); go("home"); }}>🧠 Miscommunication AI</a>
      <button className="menu" aria-label="Toggle menu" onClick={() => setOpen(!open)}>{open ? <X /> : <Menu />}</button>
      <div className={`links ${open ? "open" : ""}`}>
        {links.map(([t, id]) => <a key={id} href={`#${id}`} onClick={(e) => { e.preventDefault(); go(id); }}>{t}</a>)}
        <button className="btn" style={{ minHeight: 40, padding: "0 18px" }} onClick={() => go("analyzer")}>Analyze Now</button>
      </div>
    </div></nav>
  );
}
