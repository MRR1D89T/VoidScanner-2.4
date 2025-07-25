import os
import re

LOG_DIR = "logs"  # Ganti sesuai lokasi folder log kamu

def menu_grabber():
    while True:
        print("\n=== Log Grabber Menu ===")
        print("[1] List all log files")
        print("[2] Grab logs by date")
        print("[3] Show contents of a log file")
        print("[0] Return to main menu")
        choice = input("Select option: ").strip()
        if choice == "1":
            list_logs()
        elif choice == "2":
            grab_logs_by_date()
        elif choice == "3":
            show_log_file()
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

def grab_logs_by_date():
    list_logs()
    fname = input("Enter log file name: ").strip()
    log_path = os.path.join(LOG_DIR, fname)
    if not os.path.isfile(log_path):
        print("Log file not found!")
        return
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    output_file = input("Enter output file name (e.g., grabbed.log): ").strip()
    pattern = re.compile(rf"\[{re.escape(date_str)} ")
    try:
        grabbed = []
        with open(log_path, "r") as logf:
            for line in logf:
                if pattern.search(line):
                    grabbed.append(line)
        if not grabbed:
            print("No entries found for that date.")
            return
        with open(os.path.join(LOG_DIR, output_file), "w") as out:
            out.writelines(grabbed)
        print(f"{len(grabbed)} log entries grabbed and saved to {output_file}")
    except Exception as e:
        print(f"Error grabbing logs: {e}")
