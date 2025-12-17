from logger import logger
from config import DRY_RUN
from analytics import log_event

def send_reply(client, tweet_id, text):
    if DRY_RUN:
        logger.info(f"[DRY_RUN] Would reply {tweet_id}: {text}")
        log_event("dry_reply", tweet_id)
        return

    client.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)
    log_event("reply_sent", tweet_id)