function ResultDisplay({ result }) {
  if (!result) return null;

  const decision = result.decision || "Analysis complete";
  const decisionClass = decision === "duplicate" ? "is-duplicate" : decision === "possible_duplicate" ? "is-possible" : "is-new";
  const topMatch = result.top_matches?.[0];
  const score = topMatch && Number.isFinite(Number(topMatch.score)) ? Number(topMatch.score).toFixed(3) : null;

  return (
    <section className="result-card decision-card">
      <div className="result-card-heading"><span className="section-kicker">DUPLICATE DETECTION</span><span className={`decision-tag ${decisionClass}`}>{decision.replaceAll("_", " ")}</span></div>
      <div className="decision-summary">
        <div className={`decision-indicator ${decisionClass}`}><span /></div>
        <div className="decision-copy"><h4>{decision === "duplicate" ? "Likely duplicate" : decision === "possible_duplicate" ? "Potential matching issue" : "No strong duplicate found"}</h4><p>Classification from the BugSense analysis engine</p></div>
      </div>
      <div className="result-metrics">
        <div className="metric-cell"><span className="metric-label">CONFIDENCE</span><strong className={`confidence-value ${decisionClass}`}>{result.confidence || "Not provided"}</strong></div>
        <div className="metric-cell"><span className="metric-label">TOP MATCH SCORE</span><strong className="mono-value">{score ?? "—"}</strong></div>
        <div className="metric-cell cluster-cell"><span className="metric-label">CLUSTER</span><strong className="mono-value">{result.cluster_id || "—"}</strong></div>
      </div>
      {topMatch && <div className="top-match-callout"><span className="match-bullet" /><span>Closest returned match</span><strong>Bug #{topMatch.bug_id}</strong></div>}
    </section>
  );
}

export default ResultDisplay;