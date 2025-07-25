import os
import re

LOG_DIR = "logs"  # ganti sesuai folder log Anda

def menu_parser():
    while True:
        print("\n=== Log Parser Menu ===")
        print("[1] List all log files")
        print("[2] Show contents of a log file")
        print("[3] Filter log entries by date")
        print("[0] Return to main menu")
        choice = input("Select option: ").strip()
        if choice == "1":
            list_logs()
        elif choice == "2":
            show_log_file()
        elif choice == "3":
            filter_logs_by_date()
        elif choice == "0":
            break
        else:
            print("Invalid option!")

def list_logs():
    print("\nAvailable log files:")
    try:
        files = [f for f in os.listdir(LOG_DIR) if f.endswith(".log")]
        if not files:
            print("No log files found.")
            return
        for idx, fname in enumerate(files):
            print(f"  [{idx+1}] {fname}")
    except Exception as e:
        print(f"Error: {e}")

def show_log_file():
    list_logs()
    fname = input("Enter log file name: ").strip()
    log_path = os.path.join(LOG_DIR, fname)
    if not os.path.isfile(log_path):
        print("Log file not found!")
        return
    print(f"\nContents of {fname}:")
    try:
        with open(log_path, "r") as logf:
            for line in logf:
                print(line.rstrip())
    except Exception as e:
        print(f"Error reading file: {e}")

def filter_logs_by_date():
    list_logs()
    fname = input("Enter log file name: ").strip()
    log_path = os.path.join(LOG_DIR, fname)
    if not os.path.isfile(log_path):
        print("Log file not found!")
        return
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    print(f"\nFiltered log entries for {date_str}:")
    pattern = re.compile(rf"\[{re.escape(date_str)} ")
    try:
        with open(log_path, "r") as logf:
            found = False
            for line in logf:
                if pattern.search(line):
                    print(line.rstrip())
                    found = True
            if not found:
                print("No entries found for that date.")
    except Exception as e:
        print(f"Error reading file: {e}")
