import time
from config import URLS

# In-memory status store
status_data = {
    url: {
        "url": url,
        "status": "Unknown",
        "code": None,
        "last_success": None,
        "last_error": None,
        "success_count": 0,
        "error_count": 0,
        "last_checked": None
    }
    for url in URLS
}

def mark_success(url, code):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    s = status_data[url]
    s["status"] = "UP"
    s["code"] = code
    s["last_success"] = now
    s["success_count"] += 1
    s["last_checked"] = now

def mark_error(url, error_msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    s = status_data[url]
    s["status"] = "DOWN"
    s["code"] = None
    s["last_error"] = error_msg
    s["error_count"] += 1
    s["last_checked"] = now
