import Icon from "../components/Icon";

function HistoryPage({ analyses, onOpenAnalysis }) {
  return (
    <main className="route-page" aria-labelledby="history-title">
      <div className="route-heading">
        <span className="section-kicker">BUGSENSE AI / SESSION LOG</span>
        <h1 id="history-title">Analysis history</h1>
        <p>Bug reports analyzed during this browser session.</p>
      </div>

      {analyses.length ? (
        <div className="route-record-list">
          {analyses.map((item, index) => {
            const decision = item.response.decision || "analyzed";
            const decisionClass = decision === "duplicate" ? "is-duplicate" : decision === "possible_duplicate" ? "is-possible" : "is-new";

            return (
              <button className="route-record history-record" key={item.id} type="button" onClick={() => onOpenAnalysis(item)}>
                <span className="history-index">{String(index + 1).padStart(2, "0")}</span>
                <span className="route-record-copy"><span className="route-record-title">{item.title}</span><span className="route-record-summary">Cluster {item.response.cluster_id || "—"}</span></span>
                <span className={`decision-tag ${decisionClass}`}>{decision.replaceAll("_", " ")}</span>
                <span className="route-record-confidence">{item.response.confidence || "—"} confidence</span>
                <Icon name="chevron" size={16} />
              </button>
            );
          })}
        </div>
      ) : (
        <div className="route-empty-state">
          <span className="route-empty-icon"><Icon name="history" size={21} /></span>
          <h2>No analysis history available yet.</h2>
          <p>Completed analyses from this session will appear here.</p>
        </div>
      )}
    </main>
  );
}

export default HistoryPage;