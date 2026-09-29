import Icon from "../components/Icon";

function Reports({ analyses, onOpenAnalysis }) {
  return (
    <main className="route-page" aria-labelledby="reports-title">
      <div className="route-heading">
        <span className="section-kicker">BUGSENSE AI / REPORTS</span>
        <h1 id="reports-title">Reports</h1>
        <p>Completed analysis reports from this session.</p>
      </div>

      {analyses.length ? (
        <div className="route-record-list">
          {analyses.map((item, index) => {
            const improved = item.response.improved_report || {};
            const decision = item.response.decision || "analyzed";
            const decisionClass = decision === "duplicate" ? "is-duplicate" : decision === "possible_duplicate" ? "is-possible" : "is-new";

            return (
              <button className="route-record" key={item.id} type="button" onClick={() => onOpenAnalysis(item)}>
                <span className="history-index">{String(index + 1).padStart(2, "0")}</span>
                <span className="route-record-copy">
                  <span className="route-record-title">{item.title}</span>
                  {improved.summary && <span className="route-record-summary">{improved.summary}</span>}
                </span>
                <span className={`decision-tag ${decisionClass}`}>{decision.replaceAll("_", " ")}</span>
                <span className="route-record-confidence">{item.response.confidence || "—"} confidence</span>
                <Icon name="chevron" size={16} />
              </button>
            );
          })}
        </div>
      ) : (
        <div className="route-empty-state">
          <span className="route-empty-icon"><Icon name="reports" size={21} /></span>
          <h2>No reports available yet.</h2>
          <p>Reports will appear here after a bug analysis is completed.</p>
        </div>
      )}
    </main>
  );
}

export default Reports;