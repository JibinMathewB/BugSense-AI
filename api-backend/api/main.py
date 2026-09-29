from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(
    title="Duplicate Defect Finder API",
    description="AI system for detecting duplicate bug reports",
    version="1.0"
)

# Allow frontend (React/Vite) to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for hackathon demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)