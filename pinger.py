import asyncio
import aiohttp
from config import URLS, INTERVAL, HEADERS
from status_store import mark_success, mark_error

async def ping_url(session, url):
    try:
        async with session.get(url, headers=HEADERS, timeout=20) as res:
            print(f"[UP] {url} → {res.status}")
            mark_success(url, res.status)
    except Exception as e:
        print(f"[DOWN] {url} → {e}")
        mark_error(url, str(e))

async def ping_loop():
    async with aiohttp.ClientSession() as session:
        while True:
            print("\n=== Pinging URLs ===")
            await asyncio.gather(*(ping_url(session, url) for url in URLS))
            print("=== Sleeping 5 minutes ===")
            await asyncio.sleep(INTERVAL)