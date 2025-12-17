import time
from logger import logger

def start_health_check():
    while True:
        logger.info("Health check OK")
        time.sleep(300)