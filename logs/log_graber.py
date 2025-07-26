import os
import datetime
import zipfile

LOG_DIR = "logs"

# Auto-create logs directory
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def list_logs():
    try:
        files = os.listdir(LOG_DIR)
        log_files = [f for f in files if f.endswith(".txt")]
        if not log_files:
            print("No log files found.")
            return []
        print("\nAvailable log files:")
        for f in log_files:
            print(f"- {f}")
        return log_files
    except Exception as e:
        print(f"Error listing logs: {e}")
        return []

def grab_logs_by_date():
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    found_files = []
    for filename in os.listdir(LOG_DIR):
        if filename.startswith(f"log-{date_str}"):
            found_files.append(os.path.join(LOG_DIR, filename))

    if not found_files:
        print("No logs found for that date.")
        return

    zip_name = f"logs_{date_str.replace('-', '')}.zip"
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in found_files:
            zipf.write(file, os.path.basename(file))

    print(f"\nLogs zipped as: {zip_name}")
    print("→ You can now download or move it manually.\n")

def show_log_contents():
    files = list_logs()
    if not files:
        return
    file_name = input("Enter log file name: ").strip()
    file_path = os.path.join(LOG_DIR, file_name)
    if not os.path.exists(file_path):
        print("Log file not found!")
        return

    print(f"\nContents of {file_name}:")
    print("-" * 40)
    try:
        with open(file_path, "r") as f:
            print(f.read())
    except Exception as e:
        print(f"Error reading file: {e}")

def log_grabber_menu():
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
            show_log_contents()
        elif choice == "0":
            break
        else:
            print("Invalid option!")

# Jika dipanggil langsung
if __name__ == "__main__":
    log_grabber_menu()
