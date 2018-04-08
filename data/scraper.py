#!/usr/bin/env python3

from decouple import config
import praw
import pdb
from tinydb import TinyDB


""" Config """
# Client
CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")

# Developer
PASSWORD = config("PASSWORD")
USERNAME = config("USERNAME")

# Bot
USERAGENT = config("USERAGENT")
BOT_USERNAME = config("BOT_USERNAME")

# Data
PATH = config("DATABASE_PATH")
db = TinyDB(PATH)
# db.purge()
cnt = len(db.all())

# PRAW
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent=USERAGENT,
                     username=USERNAME)

subs = ["dankmemes"]


def process_subreddit(sub):
    global cnt

    subreddit = reddit.subreddit(sub)

    for submission in subreddit.top(limit=None):
        try:
            data = {
                "id"    : submission.id,
                "ups"   : submission.ups,
                "downs" : submission.downs,
                "media" : submission.preview
            }

            db.insert(data)
            cnt += 1

            print(f"\rProcessed {cnt} items", end='')
        except:
            pass

    print("\nDone")

if __name__ == "__main__":
    process_subreddit(subs[0])