from collections import deque
import schedule, time
from logger import logger

queue = deque()

def add_to_queue(item):
    queue.append(item)
    logger.info(f"Queued tweet {item['tweet_id']}")

def process_queue(send_fn):
    if queue:
        send_fn(**queue.popleft())

def start_scheduler(send_fn):
    schedule.every(60).seconds.do(process_queue, send_fn)
    while True:
        schedule.run_pending()
        time.sleep(1)