# void.py

import os
import sys
from core.banner import show_banner
from core.utils import clear_screen
from modules import (
    scan_headers,
    scan_sql,
    scan_xss,
    scan_admin,
    exploit_sqli,
    parser,
    filter_logs,
    log_grabber,
)
from plugins import pelari_nuclei

modules = {
    "1": ("🧠 Scan Headers", scan_headers.run),
    "2": ("🩸 Scan SQLi", scan_sql.run),
    "3": ("☠️  Scan XSS", scan_xss.run),
    "4": ("🛡️  Scan Admin Panel", scan_admin.run),
    "5": ("💣 Exploit SQLi (Auto)", exploit_sqli.run),
    "6": ("📊 Log Parser", parser.menu_parser),
    "7": ("🧹 Filter Logs by Date", filter_logs.run_filter),
    "8": ("📥 Grabber by Date", log_grabber.menu_grabber),
    "9": ("🚀 Nuclei Integration", pelari_nuclei.run_nuclei),
    "0": ("🚪 Exit", sys.exit)
}

def main():
    while True:
        clear_screen()
        show_banner()
        print("\n📌 Select Module:\n")
        for key, (desc, _) in sorted(modules.items()):
            print(f"  [{key}] {desc}")
        choice = input("\n🧩 Choice: ").strip()

        if choice in modules:
            try:
                clear_screen()
                print(f"🧪 Running: {modules[choice][0]}\n")
                modules[choice][1]()
            except Exception as e:
                print(f"\n❌ Error running module: {e}")
            input("\n⏎ Press Enter to return to menu...")
        else:
            print("❌ Invalid option!")
            input("⏎ Try again...")

if __name__ == "__main__":
    main()
