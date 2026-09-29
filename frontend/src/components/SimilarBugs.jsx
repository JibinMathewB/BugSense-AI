function SimilarBugs({ bugs }) {
  if (!bugs || bugs.length === 0) return null;

  return (
    <section className="result-card matches-card">
      <div className="result-card-heading"><div><span className="section-kicker">SEMANTIC SEARCH</span><h4>Similar issues</h4></div><span className="result-count">{bugs.length.toString().padStart(2, "0")} MATCHES</span></div>
      <div className="match-list">
        {bugs.map((bug, index) => (
          <div className="match-row" key={`${bug.bug_id}-${index}`}>
            <span className="match-rank">{String(index + 1).padStart(2, "0")}</span>
            <span className="match-icon"><IconFallback /></span>
            <span className="match-id">Bug #{bug.bug_id}</span>
            <span className="match-score-label">Returned score</span>
            <strong className="match-score">{Number.isFinite(Number(bug.score)) ? Number(bug.score).toFixed(3) : "—"}</strong>
          </div>
        ))}
      </div>
    </section>
  );
}

function IconFallback() {
  return <svg aria-hidden="true" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d="M4 5h16v14H4zM8 9h8M8 13h5" /></svg>;
}

export default SimilarBugs;