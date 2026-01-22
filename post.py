import feedparser
import requests
import json
import os

FEED_URL = "https://letterboxd.com/diazozco/rss/"
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

feed = feedparser.parse(FEED_URL)

last_file = "last.txt"
last_id = ""

try:
    with open(last_file, "r") as f:
        last_id = f.read().strip()
except:
    pass

for entry in feed.entries[:1]:
    if entry.id != last_id:
        message = {
            "content": f"🎬 **{entry.title}**\n{entry.link}"
        }
        requests.post(WEBHOOK_URL, json=message)
        with open(last_file, "w") as f:
            f.write(entry.id)
