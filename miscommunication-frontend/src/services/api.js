const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export async function analyzeMessage(message, relationship, context) {
  let res;
  try {
    res = await fetch(`${API_URL}/analyze`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, relationship, context }),
    });
  } catch {
    throw new Error(`Can't reach the backend at ${API_URL}. Is FastAPI running (and CORS enabled)?`);
  }
  if (!res.ok) {
    let detail = "";
    try { const j = await res.json(); detail = typeof j.detail === "string" ? j.detail : JSON.stringify(j.detail); } catch {}
    throw new Error(`Server error (${res.status}). ${detail}`.trim());
  }
  const data = await res.json().catch(() => null);
  if (!data || typeof data !== "object" || !Object.keys(data).length) throw new Error("The server returned an empty response.");
  return data;
}
