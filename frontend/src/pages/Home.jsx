import { useState } from "react";
import BugForm from "../components/BugForm";
import ResultDisplay from "../components/ResultDisplay";
import SimilarBugs from "../components/SimilarBugs";
import ImprovedReport from "../components/ImprovedReport";
import Navbar from "../components/Navbar";
import Icon from "../components/Icon";
import { analyzeBug } from "../services/api";

function Home({ selectedAnalysis, onAnalysisComplete, onNewAnalysis }) {
  const [result, setResult] = useState(() => selectedAnalysis?.response || null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [lastRequest, setLastRequest] = useState(() => selectedAnalysis?.request || null);
  const [formVersion, setFormVersion] = useState(0);

  const handleAnalyze = async (data) => {
    setLastRequest(data);
    setLoading(true);
    setResult(null);
    setError("");

    try {
      const response = await analyzeBug(data);
      setResult(response);
      onAnalysisComplete({ id: Date.now(), title: data.title, request: data, response });
    } catch (error) {
      console.error(error);
      setError(error.message || "Unable to analyze the bug report.");
    } finally {
      setLoading(false);
    }
  };

  const startNewAnalysis = () => {
    setFormVersion((version) => version + 1);
    setResult(null);
    setLoading(false);
    setError("");
    setLastRequest(null);
    onNewAnalysis();
  };

  return (
    <main>
          <section className="hero" aria-labelledby="hero-title">
            <div className="eyebrow"><span className="eyebrow-icon"><Icon name="spark" size={14} /></span>AI-POWERED BUG INTELLIGENCE</div>
            <h1 id="hero-title">Find the bug.<br /><span>Understand the impact.</span></h1>
            <p className="hero-copy">Detect duplicate issues, improve bug reports, and turn raw reports into actionable engineering intelligence.</p>
            <div className="feature-list" aria-label="Platform capabilities">
              <span><Icon name="scan" size={15} />Duplicate detection</span>
              <span><Icon name="spark" size={15} />Semantic search</span>
              <span><Icon name="text" size={15} />AI enhancement</span>
            </div>
          </section>

          <section className="workspace" aria-label="Bug analysis workspace">
            <div className="workspace-heading">
              <div>
                <span className="section-kicker">WORKSPACE / NEW ANALYSIS</span>
                <h2>Bug intelligence</h2>
              </div>
              <span className="secure-label"><span className="status-light" />LOCAL ANALYSIS SESSION</span>
            </div>

            <div className="workspace-grid">
              <BugForm key={formVersion} onAnalyze={handleAnalyze} loading={loading} autoFocusTitle={formVersion > 0} />

              <section className="analysis-panel" aria-live="polite" aria-busy={loading}>
                <div className="panel-heading">
                  <div>
                    <span className="section-kicker">INTELLIGENCE ENGINE</span>
                    <h3>AI analysis</h3>
                  </div>
                  <span className="panel-mark"><Icon name="spark" size={16} /></span>
                </div>

                {loading ? (
                  <div className="loading-state">
                    <div className="analysis-orbit" aria-hidden="true"><span /><i /><b /></div>
                    <p className="state-title">Analyzing report</p>
                    <p className="state-copy">Comparing against the bug knowledge base and improving report clarity.</p>
                    <div className="loading-line"><span /></div>
                  </div>
                ) : error ? (
                  <div className="error-state" role="alert">
                    <span className="error-icon"><Icon name="alert" size={20} /></span>
                    <span className="section-kicker">ANALYSIS FAILED</span>
                    <h4>We couldn’t complete the analysis.</h4>
                    <p>{error}</p>
                    {lastRequest && <button className="retry-button" type="button" onClick={() => handleAnalyze(lastRequest)}><Icon name="retry" size={15} />Retry analysis</button>}
                  </div>
                ) : result ? (
                  <div className="result-stack">
                    <ResultDisplay result={result} />
                    <SimilarBugs bugs={result.top_matches} />
                    <ImprovedReport report={result.improved_report} />
                    <button className="new-analysis-button" type="button" onClick={startNewAnalysis}><Icon name="retry" size={15} />New Analysis</button>
                  </div>
                ) : (
                  <div className="empty-state">
                    <div className="empty-visual" aria-hidden="true">
                      <div className="visual-ring ring-outer" /><div className="visual-ring ring-inner" />
                      <span className="visual-core"><Icon name="bug" size={27} /></span>
                      <i className="visual-node node-one" /><i className="visual-node node-two" /><i className="visual-node node-three" />
                    </div>
                    <span className="section-kicker">READY WHEN YOU ARE</span>
                    <h4>Waiting for a bug report</h4>
                    <p>Submit a report and BugSense AI will analyze it for duplicate issues, similarity, and report improvements.</p>
                    <div className="empty-checks"><span><i />Duplicate matching</span><span><i />Report enhancement</span></div>
                  </div>
                )}
              </section>
            </div>
          </section>

    </main>
  );
}

export default Home;