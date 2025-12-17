import csv
from datetime import datetime

def log_event(event, meta=""):
    with open("analytics.csv", "a", newline="") as f:
        csv.writer(f).writerow([datetime.utcnow(), event, meta])