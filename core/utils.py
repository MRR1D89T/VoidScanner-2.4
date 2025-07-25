import os
import random
import json
import datetime

# === GLOBAL USER AGENTS POOL (500+) ===
USER_AGENTS = []

# === 1. Browser Desktop User Agents ===
USER_AGENTS += [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.5735.91 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:117.0) Gecko/20100101 Firefox/117.0"
] * 20  # (x20 = 100 UA)

# === 2. Mobile Devices UA ===
USER_AGENTS += [
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 Chrome/103.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 10) AppleWebKit/537.36 Chrome/93.0.4577.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; vivo 1915) AppleWebKit/537.36 Chrome/87.0.4280.101 Mobile Safari/537.36"
] * 25  # (x25 = 100 UA)

# === 3. CLI Tools & Scanners ===
USER_AGENTS += [
    "curl/7.64.1",
    "Wget/1.21.1 (linux-gnu)",
    "sqlmap/1.5.12#dev",
    "python-requests/2.25.1",
    "nmap/7.93",
    "ffuf/1.4",
    "dirbuster/1.0-RC1",
    "Nikto/2.1.6 (Evasions: none)",
    "Go-http-client/2.0",
    "nuclei -v 3.0.1"
] * 10  # (x10 = 100 UA)

# === 4. Search Engine & Bot User Agents ===
USER_AGENTS += [
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "Bingbot/2.0 (+http://www.bing.com/bingbot.htm)",
    "DuckDuckBot/1.0 (+http://duckduckgo.com/duckduckbot.html)",
    "YandexBot/3.0 (+http://yandex.com/bots)",
    "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
    "Twitterbot/1.0",
    "Slackbot 1.0",
    "TelegramBot (like Twitterbot)"
] * 10  # (x10 = 80 UA)

# === 5. Fake/Obfuscated/Custom Scanner User Agents ===
USER_AGENTS += [
    f"Mozilla/5.0 (compatible; ScannerVoidBot/{i}.0; +https://voidsec.net)" for i in range(1, 101)
]

# === === FUNCTIONS === ===

def get_random_agent():
    """Return a random user-agent from the pool"""
    return random.choice(USER_AGENTS)

def current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def save_log(content, filename="scan_log.txt"):
    """Save logs to /logs/ folder"""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    full_path = os.path.join("logs", filename)
    with open(full_path, 'a', encoding='utf-8') as f:
        f.write(f"[{current_time()}] {content}\n")

def export_json(data, filename="result.json"):
    """Export dict to JSON in logs folder"""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    full_path = os.path.join("logs", filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def format_date(dt_string):
    """Format date to dd-mm-yyyy"""
    try:
        dt = datetime.datetime.strptime(dt_string, '%Y-%m-%d')
        return dt.strftime('%d-%m-%Y')
    except:
        return dt_string

def load_payloads(file_path):
    """Load payloads from file"""
    payloads = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    payloads.append(line)
    return payloads

def bypass_waf(payload):
    """Very simple obfuscation"""
    return payload.replace("'", "''").replace("=", " LIKE ").replace("<", "&lt;").replace(">", "&gt;")

def print_color(text, color='green'):
    """Print colorized output"""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'cyan': '\033[96m',
        'blue': '\033[94m',
        'end': '\033[0m'
    }
    print(f"{colors.get(color, '')}{text}{colors['end']}")
