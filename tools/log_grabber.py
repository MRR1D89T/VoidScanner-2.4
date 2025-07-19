# modules/log_grabber.py

import os
import re
from datetime import datetime
from colorama import Fore, Style

def parse_logs_by_date(log_dir="logs", target_date=None):
    if not os.path.exists(log_dir):
        print(f"{Fore.RED}[!] Log folder not found: {log_dir}{Style.RESET_ALL}")
        return

    if not target_date:
        target_date = input(f"{Fore.CYAN}[?] Enter date (YYYY-MM-DD): {Style.RESET_ALL}").strip()
    
    try:
        datetime.strptime(target_date, "%Y-%m-%d")
    except ValueError:
        print(f"{Fore.RED}[!] Invalid date format.{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}[*] Searching logs for date: {target_date}{Style.RESET_ALL}")

    pattern = re.compile(r"(\d{4}-\d{2}-\d{2})\s+\|\s+(.*?)\s+\|\s+(.*?)\s+\|\s+(.*?)$")

    found = False
    for file in os.listdir(log_dir):
        if file.endswith(".log"):
            with open(os.path.join(log_dir, file), "r") as f:
                for line in f:
                    match = pattern.match(line)
                    if match:
                        log_date, vuln_type, url, status = match.groups()
                        if log_date == target_date:
                            print(f"{Fore.GREEN}[+] {line.strip()}{Style.RESET_ALL}")
                            found = True
    if not found:
        print(f"{Fore.RED}[-] No logs found for {target_date}{Style.RESET_ALL}")
