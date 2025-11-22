import os

URLS = [u.strip() for u in os.getenv("URLS", "").split(",") if u.strip()]
INTERVAL = 300  # seconds

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}
