import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.mule.co.kr/bbs/market"
WEBHOOK = "https://discord.com/api/webhooks/1486755928794595420/czAkncoTkQi91OM6p3vYD0pnWdibUkDjoBqsyI-YchAcFq3NPsS8yzTV-TJ5oBrsk-Oh"

KEYWORDS = ["THR"]

seen = set()

def send(msg):
    requests.post(WEBHOOK, json={"content": msg})

def check():
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    posts = soup.select("a")[:30]  # 🔥 최신 글만

    for post in posts:
        title = post.text.strip()
        link = post.get("href")

        if not title or not link:
            continue

        for keyword in KEYWORDS:
            if keyword.lower() in title.lower():
                if link not in seen:
                    seen.add(link)
                    send(f"🔥 THR 매물!\n{title}\nhttps://www.mule.co.kr{link}")

while True:
    check()
    time.sleep(60)
