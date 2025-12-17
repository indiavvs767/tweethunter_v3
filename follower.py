import json
import os

FOLLOWERS_FILE = "followers.json"

def load_followers():
    if not os.path.exists(FOLLOWERS_FILE):
        return set()
    with open(FOLLOWERS_FILE, "r") as f:
        return set(json.load(f))

def save_followers(followers):
    with open(FOLLOWERS_FILE, "w") as f:
        json.dump(list(followers), f)

def get_new_followers(api, user_id):
    stored = load_followers()
    current = set(str(f.id) for f in api.get_followers(user_id=user_id))

    new_followers = current - stored
    save_followers(current)

    return new_followers