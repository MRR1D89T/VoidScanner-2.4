import subprocess
import os
import datetime
from core.utils import save_log

def run_nuclei_scan(target_url, template=None, severity="low,medium,high,critical"):
    print(f"\n[⚙️] Running Nuclei scan on: {target_url}")

    # Tentukan path output log
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"logs/nuclei_{timestamp}.txt"

    # Command dasar
    cmd = [
        "nuclei",
        "-u", target_url,
        "-severity", severity,
        "-o", output_file
    ]

    if template:
        cmd.extend(["-t", template])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        print("[📤] Nuclei output:\n")
        print(result.stdout)

        # Simpan hasil ke log dengan kategori nuclei
        if os.path.exists(output_file):
            with open(output_file, "r") as f:
                content = f.read()
            save_log("nuclei", target_url, content)

        print(f"[💾] Results saved to {output_file}")

    except subprocess.TimeoutExpired:
        print("[⏱️] Nuclei scan timeout reached (5 minutes).")
    except Exception as e:
        print(f"[❌] Failed to run nuclei: {str(e)}")

def run_nuclei():
    print("\n=== Nuclei Integration ===")
    target_url = input("Enter target URL: ").strip()
    if not target_url:
        print("Target URL cannot be empty.")
        return
    template = input("Template (leave blank for default): ").strip() or None
    severity = input("Severity (default: low,medium,high,critical): ").strip() or "low,medium,high,critical"
    run_nuclei_scan(target_url, template, severity)
