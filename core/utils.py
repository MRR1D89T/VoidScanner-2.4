import os
import random
import string
import datetime

# Bersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Generate User-Agent acak dari list besar
def generate_user_agent():
    user_agents = [
        # Desktop
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.117 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        # Mobile
        "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.92 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; Redmi Note 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.154 Mobile Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
        # Bot & API
        "Googlebot/2.1 (+http://www.google.com/bot.html)",
        "curl/7.85.0",
        "Wget/1.21.2 (linux-gnu)",
        "python-requests/2.31.0",
        "Mozilla/5.0 zgrab/0.x",
        # Headless Browsers
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) HeadlessChrome/114.0.5735.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome Safari/537.36",
        # Uncommon
        "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    ]
    return random.choice(user_agents)

# Alias agar kompatibel dengan modul lama
def get_random_user_agent():
    return generate_user_agent()

# Alias agar bisa di-import langsung
random_user_agent = get_random_user_agent

# Simpan log eksploitasi
def save_log(vuln_type, data):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    date = datetime.now().strftime("%Y%m%d")
    filename = f"{log_dir}/{vuln_type}_{date}.txt"
    with open(filename, "a") as f:
        f.write(data + "\n")

# Generate nama file random (opsional)
def generate_random_filename(length=8):
    return ''.join(random.choices(string.ascii_letters + 
string.digits, k=length))
