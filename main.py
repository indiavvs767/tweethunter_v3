import tweepy
import logging
import os
import time
from dotenv import load_dotenv
import time
import logging

logging.info("TweetHunter V3 started successfully")

while True:
    logging.info("Heartbeat: bot running")
    time.sleep(300)  # every 5 minutes

from autodm import send_dm
from follower import get_new_followers
from config import DRY_RUN

load_dotenv()

logging.basicConfig(level=logging.INFO)

auth = tweepy.OAuth1UserHandler(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_SECRET")
)

api = tweepy.API(auth, wait_on_rate_limit=True)

me = api.verify_credentials()
logging.info(f"Logged in as @{me.screen_name}")
logging.info(f"DRY_RUN={DRY_RUN}")

while True:
    try:
        new_followers = get_new_followers(api, me.id)

        for fid in new_followers:
            user = api.get_user(user_id=fid)
            send_dm(api, fid, user.screen_name, user.description)

        time.sleep(300)  # check every 5 minutes

    except Exception as e:
        logging.error(e)
        time.sleep(60)