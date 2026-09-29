import sys
import os
import uvicorn
import config

# Add project root
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)

# Add api-backend folder explicitly
sys.path.append(os.path.join(PROJECT_ROOT, "api-backend"))


def main():
    print("🚀 Starting Duplicate Defect Finder API...")
    print(f"Host: {config.API_HOST}")
    print(f"Port: {config.API_PORT}")

    uvicorn.run(
        "api.main:app",
        host=config.API_HOST,
        port=config.API_PORT,
        reload=True,
        log_level="info"
    )


if __name__ == "__main__":
    main()