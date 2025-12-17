import time
import logging
from config import DRY_RUN, MAX_DMS_PER_HOUR
from ai import generate_dm

dm_counter = 0
hour_start = time.time()

def reset_hourly_counter():
    global dm_counter, hour_start
    if time.time() - hour_start >= 3600:
        dm_counter = 0
        hour_start = time.time()

def send_dm(api, user_id, username, bio=""):
    global dm_counter
    reset_hourly_counter()

    if dm_counter >= MAX_DMS_PER_HOUR:
        logging.warning("Hourly DM limit reached")
        return

    message = generate_dm(username, bio)

    if DRY_RUN:
        logging.info(f"[DRY_RUN] Would DM @{username}: {message}")
    else:
        api.send_direct_message(user_id, message)
        logging.info(f"DM sent to @{username}")

    dm_counter += 1
    time.sleep(30)  # human delay