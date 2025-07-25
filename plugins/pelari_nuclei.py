import os
import subprocess

def menu_nuclei():
    while True:
        print("\n=== Nuclei Scanner Menu ===")
        print("[1] Scan target with Nuclei")
        print("[2] Show available Nuclei templates")
        print("[0] Return to main menu")
        choice = input("Select option: ").strip()
        if choice == "1":
            scan_with_nuclei()
        elif choice == "2":
            show_templates()
        elif choice == "0":
            break
        else:
            print("Invalid option!")

def scan_with_nuclei():
    target = input("Enter target URL or IP: ").strip()
    template = input("Enter template name (or leave blank for default): ").strip()
    cmd = ["nuclei", "-u", target]
    if template:
        cmd.extend(["-t", template])
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("\n--- Nuclei Output ---")
        print(result.stdout)
        if result.stderr:
            print("\n--- Errors/Warnings ---")
            print(result.stderr)
    except Exception as e:
        print(f"Error running Nuclei: {e}")

def show_templates():
    print("\n--- Available Nuclei Templates ---")
    nuclei_templates_dir = os.path.expanduser("~/.nuclei/templates")
    if not os.path.isdir(nuclei_templates_dir):
        print("Nuclei templates directory not found!")
        return
    try:
        for root, dirs, files in os.walk(nuclei_templates_dir):
            for file in files:
                if file.endswith(".yaml"):
                    print(os.path.join(root, file))
    except Exception as e:
        print(f"Error listing templates: {e}")
