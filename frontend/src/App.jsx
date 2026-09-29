import { useEffect, useState } from "react";
import Navbar from "./components/Navbar";
import HistoryPage from "./pages/History";
import Home from "./pages/Home";
import Reports from "./pages/Reports";

const validRoutes = ["/analyze", "/reports", "/history"];

function App() {
  const [route, setRoute] = useState(() => validRoutes.includes(window.location.pathname) ? window.location.pathname : "/analyze");
  const [theme, setTheme] = useState(() => localStorage.getItem("bugsense-theme") || "dark");
  const [history, setHistory] = useState([]);
  const [activeAnalysis, setActiveAnalysis] = useState(null);

  useEffect(() => {
    if (!validRoutes.includes(window.location.pathname)) {
      window.history.replaceState({}, "", "/analyze");
    }

    const handlePopState = () => {
      setRoute(validRoutes.includes(window.location.pathname) ? window.location.pathname : "/analyze");
    };

    window.addEventListener("popstate", handlePopState);
    return () => window.removeEventListener("popstate", handlePopState);
  }, []);

  const navigateTo = (nextRoute) => {
    if (window.location.pathname !== nextRoute) {
      window.history.pushState({}, "", nextRoute);
    }
    setRoute(nextRoute);
  };

  const toggleTheme = () => {
    const nextTheme = theme === "dark" ? "light" : "dark";
    setTheme(nextTheme);
    localStorage.setItem("bugsense-theme", nextTheme);
  };

  const recordAnalysis = (item) => {
    setHistory((previous) => [item, ...previous.filter((entry) => entry.id !== item.id)].slice(0, 6));
    setActiveAnalysis(item);
  };

  const openAnalysis = (item) => {
    setActiveAnalysis(item);
    navigateTo("/analyze");
  };

  return (
    <div className="app-shell" data-theme={theme} id="top">
      <div className="ambient-grid" aria-hidden="true" />
      <div className="page-frame">
        <Navbar theme={theme} onToggleTheme={toggleTheme} route={route} onNavigate={navigateTo} />
        {route === "/reports" ? (
          <Reports analyses={history} onOpenAnalysis={openAnalysis} />
        ) : route === "/history" ? (
          <HistoryPage analyses={history} onOpenAnalysis={openAnalysis} />
        ) : (
          <Home
            selectedAnalysis={activeAnalysis}
            onAnalysisComplete={recordAnalysis}
            onNewAnalysis={() => setActiveAnalysis(null)}
          />
        )}
        <footer className="page-footer"><span>BUGSENSE AI <span className="footer-dot">/</span> DEFECT INTELLIGENCE</span><span>Built for clearer engineering signals</span></footer>
      </div>
    </div>
  );
}

export default App;