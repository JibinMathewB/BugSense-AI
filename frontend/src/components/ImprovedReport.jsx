import { useState } from "react";
import Icon from "./Icon";

function ImprovedReport({ report }) {
  const [copied, setCopied] = useState(false);
  if (!report) return null;

  const copyReport = async () => {
    try {
      await navigator.clipboard.writeText([report.title, report.summary].filter(Boolean).join("\n\n"));
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1800);
    } catch {
      setCopied(false);
    }
  };

  return (
    <section className="result-card improved-card">
      <div className="result-card-heading"><div><span className="section-kicker">AI ENHANCEMENT</span><h4>Improved report</h4></div><button className="copy-button" type="button" onClick={copyReport} title="Copy improved report" aria-label="Copy improved report"><Icon name={copied ? "check" : "copy"} size={15} /><span>{copied ? "Copied" : "Copy"}</span></button></div>
      <div className="report-content">
        {report.title && <div className="report-section"><span className="report-label">TITLE</span><p className="report-text">{report.title}</p></div>}
        {report.summary && <div className="report-section"><span className="report-label">SUMMARY</span><p className="report-text">{report.summary}</p></div>}
      </div>
    </section>
  );
}

export default ImprovedReport;