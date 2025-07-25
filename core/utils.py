import random
import os
from datetime 
import datetime

# List user-agent acak (bisa diperluas)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X)",
    "Mozilla/5.0 (Android 11; Mobile; rv:84.0) Gecko/84.0 Firefox/84.0",
]

def generate_user_agent():
    return random.choice(USER_AGENTS)

def save_log(log_type, message):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    log_path = os.path.join(log_dir, f"{log_type}_{date_str}.log")

    with open(log_path, "a") as log_file:
        log_file.write(f"[{time_str}] {message}\n")
