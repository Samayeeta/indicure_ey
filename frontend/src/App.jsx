import { useEffect, useMemo, useRef, useState } from "react";
import "./App.css";

function Dropdown({ value, onChange, options, placeholder = "Select…" }) {
  const [open, setOpen] = useState(false);
  const [dir, setDir] = useState("down"); 
  const rootRef = useRef(null);
  const btnRef = useRef(null);

  useEffect(() => {
    function onDocClick(e) {
      if (!rootRef.current) return;
      if (!rootRef.current.contains(e.target)) setOpen(false);
    }
    function onKey(e) {
      if (e.key === "Escape") setOpen(false);
    }
    document.addEventListener("mousedown", onDocClick);
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("mousedown", onDocClick);
      document.removeEventListener("keydown", onKey);
    };
  }, []);

  useEffect(() => {
    if (!open || !btnRef.current) return;

    const rect = btnRef.current.getBoundingClientRect();
    const menuMax = 240; 
    const spaceBelow = window.innerHeight - rect.bottom;
    const spaceAbove = rect.top;

    if (spaceBelow < menuMax && spaceAbove > spaceBelow) setDir("up");
    else setDir("down");
  }, [open]);

  return (
    <div className="dd" ref={rootRef}>
      <button
        ref={btnRef}
        type="button"
        className="dd-btn"
        onClick={() => setOpen((v) => !v)}
        aria-haspopup="listbox"
        aria-expanded={open}
      >
        <span className={`dd-value ${value ? "" : "placeholder"}`}>
          {value || placeholder}
        </span>
        <span className={`dd-caret ${open ? "open" : ""}`}>▾</span>
      </button>

      {open && (
        <div className={`dd-menu ${dir === "up" ? "up" : "down"}`} role="listbox">
          {options.map((opt) => (
            <button
              key={opt}
              type="button"
              className={`dd-item ${opt === value ? "active" : ""}`}
              onClick={() => {
                onChange(opt);
                setOpen(false);
              }}
            >
              {opt}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

export default function App() {
  const [view, setView] = useState("input"); 
  const [activeTab, setActiveTab] = useState("summary");


  const [analysisMode, setAnalysisMode] = useState("General");
  const [geography, setGeography] = useState("India");


  const [agentStatus, setAgentStatus] = useState({
    orchestration: "pending",
    clinical: "pending",
    web: "pending",
    patent: "pending",
    market: "pending",
    internal: "pending",
  });

  const modeOptions = useMemo(() => ["General", "Clinical", "Patent", "Market"], []);
  const geoOptions = useMemo(() => ["India"], []);

  const downloadPdf = async () => {
    try {
      const qs = new URLSearchParams({
        mode: analysisMode, 
        geo: geography, 
      });


      const res = await fetch(
  `http://127.0.0.1:8000/api/report/pdf?${qs.toString()}`,
  {
    method: "GET",
  }
);

      if (!res.ok) {
        const txt = await res.text();
        throw new Error(`PDF request failed (${res.status}): ${txt}`);
      }

      const blob = await res.blob();

      if (!blob || blob.size < 500) {
        throw new Error("PDF response looks empty or too small.");
      }

      const url = window.URL.createObjectURL(blob);

      const a = document.createElement("a");
      a.href = url;
      a.download = `IndiCure_Ranolazine_HFpEF_${geography}_${analysisMode}.pdf`;
      document.body.appendChild(a);
      a.click();
      a.remove();

      window.URL.revokeObjectURL(url);
    } catch (e) {
      console.error(e);
      alert("Could not generate PDF. Check backend logs and browser console.");
    }
  };

  const runAnalysis = () => {
    setAgentStatus({
      orchestration: "pending",
      clinical: "pending",
      web: "pending",
      patent: "pending",
      market: "pending",
      internal: "pending",
    });

    setView("processing");

    const sequence = ["orchestration", "clinical", "web", "patent", "market", "internal"];

    sequence.forEach((agent, index) => {
      setTimeout(() => {
        setAgentStatus((prev) => ({ ...prev, [agent]: "running" }));
      }, index * 500);

      setTimeout(() => {
        setAgentStatus((prev) => ({ ...prev, [agent]: "done" }));
      }, index * 500 + 400);
    });

    setTimeout(() => setView("results"), 3500);
  };

  return (
    <div className="app-root">
      <header className="hero">
        <h1>IndiCure AI</h1>
        <p>
          Agentic AI system for drug repurposing analysis
          <span className="muted"> (Demo: Ranolazine → HFpEF, India)</span>
        </p>
      </header>

      {/* QUERY INPUT */}
      {view === "input" && (
        <section className="card input-card">
          <h2>Molecule-level Query</h2>

          <textarea
            defaultValue="Assess repurposing potential of Ranolazine for Heart Failure with Preserved Ejection Fraction (HFpEF) in the Indian population. Provide mechanistic rationale, clinical evidence, unmet need, and next steps."
          />

          <div className="controls">
            <div>
              <label>Analysis Mode</label>
              <Dropdown value={analysisMode} onChange={setAnalysisMode} options={modeOptions} />
            </div>

            <div>
              <label>Geography</label>
              <Dropdown value={geography} onChange={setGeography} options={geoOptions} />
            </div>
          </div>

          <div className="actions">
            <button className="primary" onClick={runAnalysis}>
              Run Analysis
            </button>
          </div>
        </section>
      )}

      {/* PROCESSING */}
      {view === "processing" && (
        <section className="card processing-card">
          <h2>Agent Execution</h2>

          <ul className="agent-list">
            <AgentRow name="Master Orchestration Agent" status={agentStatus.orchestration} />
            <AgentRow name="Clinical Trials Agent" status={agentStatus.clinical} />
            <AgentRow name="Web Intelligence Agent" status={agentStatus.web} />
            <AgentRow name="Patent Landscape Agent" status={agentStatus.patent} />
            <AgentRow name="IQVIA Insights Agent" status={agentStatus.market} />
            <AgentRow name="Internal Knowledge Agent" status={agentStatus.internal} />
          </ul>

          <p className="muted">Executing agents sequentially and synthesizing evidence…</p>
        </section>
      )}

      {/* RESULTS */}
      {view === "results" && (
        <section className="results">
          <div className="results-header">
            <h2>Results Dashboard</h2>
            <div className="results-actions">
              {/* ✅ Use the reusable downloader */}
              <button className="secondary" onClick={downloadPdf}>
                Download PDF
              </button>

              <button className="primary" onClick={() => setView("input")}>
                New Query
              </button>
            </div>
          </div>

          <div className="metrics">
            <div className="metric ok">
              Clinical Signal<br />
              <span>Positive</span>
            </div>
            <div className="metric ok">
              Safety<br />
              <span>Favorable</span>
            </div>
            <div className="metric ok">
              Patent Risk<br />
              <span>Low</span>
            </div>
            <div className="metric warn">
              India Unmet Need<br />
              <span>High</span>
            </div>
          </div>

          <div className="tabs">
            {["summary", "evidence", "feasibility", "recommendation"].map((t) => (
              <button
                key={t}
                className={activeTab === t ? "active" : ""}
                onClick={() => setActiveTab(t)}
              >
                {t.charAt(0).toUpperCase() + t.slice(1)}
              </button>
            ))}
          </div>

          <div className="card">
            {activeTab === "summary" && (
              <>
                <h3>Executive Summary</h3>
                <p>
                  Ranolazine, currently approved for chronic angina, demonstrates strong
                  mechanistic and clinical potential for repurposing in HFpEF — a major,
                  undertreated cardiac condition in India. Clinical evidence shows
                  significant improvement in diastolic parameters without hemodynamic
                  compromise.
                </p>
                <p className="muted">
                  Mode: {analysisMode} • Geography: {geography}
                </p>
              </>
            )}

            {activeTab === "evidence" && (
              <>
                <h3>Clinical & Mechanistic Evidence</h3>
                <ul>
                  <li>↑ LVEDV (p &lt; 0.001)</li>
                  <li>↓ E/E′ (p = 0.05)</li>
                  <li>No BP / HR / QT risk</li>
                  <li>Late Na⁺ current inhibition → ↓ Ca²⁺ overload</li>
                </ul>
              </>
            )}

            {activeTab === "feasibility" && (
              <>
                <h3>Feasibility</h3>
                <ul>
                  <li>Off-patent / low FTO risk</li>
                  <li>Oral, affordable therapy</li>
                  <li>Supplemental indication pathway</li>
                </ul>
              </>
            )}

            {activeTab === "recommendation" && (
              <>
                <h3>Recommendation</h3>
                <p>
                  Proceed with targeted Phase II/III Indian clinical trials evaluating
                  Ranolazine as adjunct therapy for HFpEF, focusing on diastolic endpoints
                  and hospitalization reduction.
                </p>
              </>
            )}
          </div>
        </section>
      )}
    </div>
  );
}

function AgentRow({ name, status }) {
  return (
    <li className="agent-row">
      <span>{name}</span>
      {status === "pending" && <span className="tag pending">Queued</span>}
      {status === "running" && <span className="tag running">Running</span>}
      {status === "done" && <span className="tag done">Completed</span>}
    </li>
  );
}