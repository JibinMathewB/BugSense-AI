# 🎨 BugSense AI – Frontend

This folder contains the **React-based user interface** for **BugSense AI**, an AI-powered system that detects duplicate bug reports and enhances bug descriptions for QA teams.

The frontend provides a simple interface where testers can submit bug reports and instantly receive:

- Duplicate detection results
- Similar historical bug reports
- AI-enhanced bug descriptions
- Confidence scores and cluster information

The frontend communicates with the **FastAPI backend** via REST API.

---

# 🚀 Purpose of the Frontend

The goal of the frontend is to provide a **clean and simple QA interface** for interacting with the BugSense AI backend.

It allows users to:

- Submit bug reports
- Analyze defects using AI
- View similar historical bugs
- See improved bug descriptions
- Understand duplicate likelihood

This helps QA teams **triage bugs faster and avoid duplicate submissions.**

---

# 🧠 How the Frontend Works

The frontend collects bug report details and sends them to the backend API.

Workflow:

User enters bug report  
↓  
Frontend sends request to API  
↓  
Backend runs AI analysis  
↓  
Results returned to frontend  
↓  
Frontend displays insights

The frontend calls the following endpoint:

```
POST /check-defect
```

---

# ⚙️ Technology Stack

The BugSense AI frontend is built using modern web technologies.

### Framework

- **React**

Used for building a responsive user interface.

---

### Build Tool

- **Vite**

Provides fast development server and optimized builds.

Benefits include:

- extremely fast HMR (Hot Module Replacement)
- lightweight configuration
- fast builds

---

### HTTP Client

- **Axios**

Used to communicate with the FastAPI backend.

---

### UI Structure

The frontend is intentionally kept **simple and clean** for demonstration purposes.

The UI focuses on:

- bug report input
- analysis results
- similar bug display
- enhanced report display

---

# 📁 Project Structure

```
frontend
│
├── src
│   ├── components
│   │   ├── BugForm.jsx
│   │   ├── Results.jsx
│   │
│   ├── pages
│   │   ├── Home.jsx
│   │
│   ├── api
│   │   ├── api.js
│   │
│   ├── App.jsx
│   ├── main.jsx
│
├── public
│
├── index.html
├── package.json
└── vite.config.js
```

---

# 📡 Backend API Connection

The frontend connects to the FastAPI backend.

Default API endpoint:

```
http://127.0.0.1:8000
```

Main API call:

```
POST /check-defect
```

Example request sent from frontend:

```json
{
"title": "Login button not working",
"description": "User cannot login after clicking submit button",
"steps": "Enter username and password then click login",
"environment": "Chrome Windows 11"
}
```

Example response received:

```json
{
"decision": "possible_duplicate",
"confidence": "medium",
"cluster_id": "cluster_740609",
"top_matches": [
  { "bug_id": 740609, "score": 0.85 }
],
"improved_report": {
  "title": "App crashes on save",
  "summary": "Saving a file with special characters causes the application to crash."
}
}
```

---

# 🖥 Running the Frontend

Navigate to the frontend directory:

```
cd frontend
```

---

## Install Dependencies

```
npm install
```

---

## Start Development Server

```
npm run dev
```

The frontend will start at:

```
http://localhost:5173
```

---

# 🔗 Connecting to Backend

Ensure the backend server is running before using the frontend.

Start backend from project root:

```
python run_server.py
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

# 📊 Example User Flow

1. User enters bug details in the form
2. Frontend sends request to backend
3. AI model analyzes bug report
4. Similar bugs are retrieved
5. Duplicate likelihood is calculated
6. Results are displayed in the UI

Displayed results include:

- Duplicate decision
- Confidence score
- Cluster ID
- Similar bug reports
- Improved bug description

---

# 🎯 Why This Frontend Matters

For QA teams, this interface provides:

- quick bug analysis
- instant duplicate detection
- improved bug reporting
- faster triaging workflows

Instead of manually searching issue trackers, QA engineers can use **BugSense AI to detect duplicates instantly.**

---

# 🔮 Future Improvements

Potential UI improvements include:

- integration with Jira dashboards
- bug visualization charts
- cluster visualization graphs
- bug similarity heatmaps
- dark mode UI
- team collaboration features

---

# 🏁 Conclusion

The BugSense AI frontend provides a **simple but powerful interface** for interacting with the AI-driven bug analysis system.

Combined with the FastAPI backend and AI pipeline, the system helps QA teams **detect duplicate bugs and improve defect reports automatically.**