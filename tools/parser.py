# modules/parser.py

import os
import re
from collections import Counter
from colorama import Fore, Style

LOG_DIR = "logs/"

def parse_log_file(filepath):
    """Parses a log file and returns useful stats."""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    total_payloads = 0
    success_payloads = 0
    failed_payloads = 0
    status_codes = Counter()
    targets = Counter()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # Extract status code
        match_status = re.search(r"Status:\s*(\d{3})", line)
        if match_status:
            status = match_status.group(1)
            status_codes[status] += 1

        # Extract URL
        match_url = re.search(r"Target:\s*(https?://[^\s]+)", line)
        if match_url:
            url = match_url.group(1)
            targets[url] += 1

        if "Payload:" in line:
            total_payloads += 1

        if "[+]" in line or "FOUND" in line.upper() or "VULN" in line.upper():
            success_payloads += 1
        elif "[-]" in line or "NOT VULNERABLE" in line.upper():
            failed_payloads += 1

    return {
        "file": os.path.basename(filepath),
        "total_payloads": total_payloads,
        "success": success_payloads,
        "failed": failed_payloads,
        "status_codes": dict(status_codes),
        "targets": dict(targets)
    }

def show_log_summary():
    print(f"\n📊 {Fore.YELLOW}Analyzing logs in: {LOG_DIR}{Style.RESET_ALL}\n")
    all_logs = [f for f in os.listdir(LOG_DIR) if f.endswith(".txt")]
    if not all_logs:
        print(f"{Fore.RED}[!] No logs found in logs folder.{Style.RESET_ALL}")
        return

    for log_file in all_logs:
        file_path = os.path.join(LOG_DIR, log_file)
        stats = parse_log_file(file_path)

        print(f"{Fore.CYAN}Log File: {stats['file']}{Style.RESET_ALL}")
        print(f"  🔹 Total Payloads : {stats['total_payloads']}")
        print(f"  ✅ Successful     : {Fore.GREEN}{stats['success']}{Style.RESET_ALL}")
        print(f"  ❌ Failed         : {Fore.RED}{stats['failed']}{Style.RESET_ALL}")
        print(f"  🔁 Targets        : {len(stats['targets'])} targets")
        print(f"  📶 Status Codes   : {stats['status_codes']}")
        print("-" * 50)

def menu_parser():
    print("\n=== Log Parser & Summary ===")
    show_log_summary()
