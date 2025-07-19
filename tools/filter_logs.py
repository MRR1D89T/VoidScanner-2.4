# modules/filter_logs.py

import os
import datetime
from colorama import Fore, Style

LOG_FOLDER = "logs/"
EXPORT_FILE = os.path.join(LOG_FOLDER, "filtered_logs_export.txt")

def filter_logs_by_date(start_date, end_date, category=None, export=False):
    """
    Menyaring file log berdasarkan rentang tanggal dan kategori (opsional).
    Dapat mengekspor hasil ke satu file jika export=True.
    """
    try:
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print(f"{Fore.RED}[!] Invalid date format. Use YYYY-MM-DD.{Style.RESET_ALL}")
        return

    print(f"\n📁 Filtering logs from {start_date} to {end_date}...\n")

    if export:
        with open(EXPORT_FILE, "w", encoding="utf-8") as ef:
            ef.write(f"# Filtered Logs from {start_date} to {end_date}\n\n")

    found_logs = 0
    for file in os.listdir(LOG_FOLDER):
        if not file.endswith(".txt"):
            continue

        try:
            file_date_str = file.split("_")[1].split(".")[0]  # YYYYMMDD
            file_date = datetime.datetime.strptime(file_date_str, "%Y%m%d")
        except Exception:
            continue

        if start <= file_date <= end:
            if category and not file.startswith(category):
                continue

            file_path = os.path.join(LOG_FOLDER, file)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                print(f"{Fore.CYAN}[+] {file}{Style.RESET_ALL}")
                print(content[:500] + "\n... (truncated)\n")
                print("-" * 50)

                if export:
                    with open(EXPORT_FILE, "a", encoding="utf-8") as ef:
                        ef.write(f"\n=== {file} ===\n")
                        ef.write(content + "\n")

                found_logs += 1

    if found_logs == 0:
        print(f"{Fore.YELLOW}[!] No logs found for specified range.{Style.RESET_ALL}")
    elif export:
        print(f"\n{Fore.GREEN}[✓] Exported to: {EXPORT_FILE}{Style.RESET_ALL}")


def menu_filter_logs():
    print("\n=== Log Filter by Date ===")
    start = input("Start Date (YYYY-MM-DD): ").strip()
    end = input("End Date (YYYY-MM-DD): ").strip()
    category = input("Log Category (xss/sql/nuclei/etc) [optional]: ").strip()
    export = input("Export result to file? (y/N): ").strip().lower() == "y"

    if not start or not end:
        print(f"{Fore.RED}[!] You must enter both start and end date.{Style.RESET_ALL}")
        return

    filter_logs_by_date(start, end, category if category else None, export)
