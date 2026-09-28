export const levelOf = (score, level) => {
  const l = String(level || "").toLowerCase();
  if (l.includes("high")) return "high";
  if (l.includes("med") || l.includes("mod")) return "medium";
  if (l.includes("low")) return "low";
  return score >= 67 ? "high" : score >= 34 ? "medium" : "low";
};
export const color = (lv) => `var(--${lv})`;
export const pct = (c) => Math.round((c <= 1 ? c * 100 : c));
