import os
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

def get_health() -> str:
    try:
        r = requests.get(f"{BASE_URL}/health", timeout=5)
        r.raise_for_status()
        data = r.json()
        return f"API status: {data.get('status','unknown')}"
    except Exception as e:
        return f"API error: {e}"
