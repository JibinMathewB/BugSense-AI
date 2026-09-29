import Icon from "./Icon";

function Navbar({ theme, onToggleTheme, route, onNavigate }) {
  const handleNavigation = (event, nextRoute) => {
    event.preventDefault();
    onNavigate(nextRoute);
  };

  return (
    <header className="topbar">
      <a className="brand" href="/analyze" aria-label="BugSense AI home" onClick={(event) => handleNavigation(event, "/analyze")}>
        <span className="brand-mark"><Icon name="bug" size={20} /></span>
        <span className="brand-name">BugSense<span>AI</span></span>
      </a>

      <div className="engine-status"><span className="status-light" />AI ENGINE ONLINE</div>

      <nav className="main-nav" aria-label="Main navigation">
        <a className={route === "/analyze" ? "active" : undefined} href="/analyze" aria-current={route === "/analyze" ? "page" : undefined} onClick={(event) => handleNavigation(event, "/analyze")}><Icon name="scan" size={16} /><span>Analyze</span></a>
        <a className={route === "/reports" ? "active" : undefined} href="/reports" aria-current={route === "/reports" ? "page" : undefined} onClick={(event) => handleNavigation(event, "/reports")}><Icon name="reports" size={16} /><span>Reports</span></a>
        <a className={route === "/history" ? "active" : undefined} href="/history" aria-current={route === "/history" ? "page" : undefined} onClick={(event) => handleNavigation(event, "/history")}><Icon name="history" size={16} /><span>History</span></a>
      </nav>

      <div className="topbar-actions">
        <button className="icon-button" type="button" onClick={onToggleTheme} title={`Switch to ${theme === "dark" ? "light" : "dark"} theme`} aria-label={`Switch to ${theme === "dark" ? "light" : "dark"} theme`}>
          <Icon name={theme === "dark" ? "sun" : "moon"} size={17} />
        </button>
      </div>
    </header>
  );
}

export default Navbar;