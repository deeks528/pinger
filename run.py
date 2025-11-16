from threading import Thread
import asyncio
from app import app
from pinger import ping_loop

def start_flask():
    app.run(host="0.0.0.0", port=6000)

def start():
    Thread(target=start_flask).start()
    asyncio.get_event_loop().run_until_complete(ping_loop())

if __name__ == "__main__":
    start()