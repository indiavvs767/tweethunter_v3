import os

DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

# SAFETY LIMITS (EDIT THESE)
MAX_DMS_PER_HOUR = int(os.getenv("MAX_DMS_PER_HOUR", 20))
MAX_DMS_PER_DAY = int(os.getenv("MAX_DMS_PER_DAY", 100))

MAX_FOLLOWS_PER_HOUR = int(os.getenv("MAX_FOLLOWS_PER_HOUR", 30))
MAX_FOLLOWS_PER_DAY = int(os.getenv("MAX_FOLLOWS_PER_DAY", 150))