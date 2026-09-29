import { useState } from "react";
import Icon from "./Icon";

function BugForm({ onAnalyze, loading, autoFocusTitle = false }) {
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    steps: "",
    environment: ""
  });
  const [validationError, setValidationError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
    setValidationError("");
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.title.trim() || !formData.description.trim()) {
      setValidationError("Bug title and description are required.");
      return;
    }

    onAnalyze({ ...formData });
  };

  return (
    <section className="form-panel" aria-labelledby="form-title">
      <div className="form-panel-heading">
        <div className="form-title-wrap"><span className="form-index">01</span><div><span className="section-kicker">BUG REPORT</span><h3 id="form-title">Submit bug report</h3></div></div>
        <span className="required-note"><i /> REQUIRED FIELDS</span>
      </div>

      <form onSubmit={handleSubmit} noValidate>
        <div className="field-group">
          <label htmlFor="bug-title"><span className="field-label"><Icon name="title" size={15} />Bug title <span className="required-mark">*</span></span><span className="char-count">{formData.title.length} chars</span></label>
          <input id="bug-title" name="title" placeholder="e.g. Session expires during file upload" value={formData.title} onChange={handleChange} autoComplete="off" aria-required="true" autoFocus={autoFocusTitle} />
        </div>

        <div className="field-group">
          <label htmlFor="bug-description"><span className="field-label"><Icon name="text" size={15} />Bug description <span className="required-mark">*</span></span><span className="char-count">{formData.description.length} chars</span></label>
          <textarea id="bug-description" name="description" placeholder="Describe what happened and what you expected instead..." value={formData.description} onChange={handleChange} rows="5" aria-required="true" />
        </div>

        <div className="field-group">
          <label htmlFor="bug-steps"><span className="field-label"><Icon name="steps" size={15} />Steps to reproduce</span><span className="optional-label">OPTIONAL</span></label>
          <textarea id="bug-steps" name="steps" placeholder={"1. Open the affected page\n2. Perform the action\n3. Observe the result"} value={formData.steps} onChange={handleChange} rows="3" />
        </div>

        <div className="field-group">
          <label htmlFor="bug-environment"><span className="field-label"><Icon name="terminal" size={15} />Environment</span><span className="optional-label">OPTIONAL</span></label>
          <input id="bug-environment" name="environment" placeholder="Browser, OS, version, or device" value={formData.environment} onChange={handleChange} autoComplete="off" />
        </div>

        {validationError && <p className="validation-message" role="alert"><Icon name="alert" size={15} />{validationError}</p>}

        <div className="form-bottom">
          <span className="form-hint"><Icon name="book" size={14} /> Required fields marked with <span>*</span></span>
          <button className="analyze-button" type="submit" disabled={loading}>
            {loading ? <><span className="button-spinner" />Analyzing Bug...</> : <>Analyze Bug <Icon name="arrow" size={16} /></>}
          </button>
        </div>
      </form>
    </section>
  );
}

export default BugForm;