import asyncio
import aiohttp

URLS = [
    "https://code-bot-lwjd.onrender.com/",
    "https://niepid-b0t2.onrender.com/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

async def ping_url(session, url):
    try:
        async with session.get(url, headers=HEADERS, timeout=20) as res:
            print(f"[PING] {url} → {res.status}")
    except Exception as e:
        print(f"[ERROR] {url} → {e}")

async def ping_loop():
    async with aiohttp.ClientSession() as session:
        while True:
            await asyncio.gather(*(ping_url(session, u) for u in URLS))
            await asyncio.sleep(300)

asyncio.run(ping_loop())