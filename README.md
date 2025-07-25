# ⚔️ VoidScannerPro v2.4 — Web Vulnerability Scanner Framework ⚔️
**Author:** MR.S13xVoid  
**Status:** Actively Maintained  
**License:** For Educational & Authorized Testing Only

---

## 🔥 Overview
`VoidScanner2.4` is a powerful and modular web vulnerability scanner built for bug bounty hunters, red teamers, and security researchers.  
Version 2.4 brings massive improvements — more payloads, auto-exploit capabilities, and log analysis tools.

---

## 🧠 Features
- 🔍 **Auto Vulnerability Scanning**
  - SQL Injection (`scan_sql.py`) — 50+ advanced payloads
  - Cross Site Scripting (`scan_xss.py`) — 60+ payloads & bypass
  - Admin Panel Finder (`scan_admin.py`)
  - Header Analysis (`scan_headers.py`)
- 💥 **Auto SQLi Exploiter** (`exploit_sqli.py`)
- 🧪 **Nuclei Plugin Integration** (`nuclei_runner.py`)
- 🗂️ **Log Grabber by Date** (`log_grabber.py`)
- 📊 **Log Filter & Parser** — auto-format and categorize scan results
- 🧰 **Modular Engine** — Easily extend with your own modules
- 🔐 **Random User-Agent, Bypass Filters, and more**

---

---

## ⚙️ Installation
```bash
git clone https://github.com/MRR1D89T/VoidScanner-2.4.git
cd VoidScanner-2.4
pip install -r requirements.txt
python void.py


---

🧪 Sample Usage

python void.py -u https://target.com
python void.py --scan all
python void.py --exploit-sqli
python tools/log_grabber.py --date 2025-07-15

📌 Notes

Requires Python 3.8+

Works on Linux / Termux / MacOS / WSL

Use responsibly — for legal penetration testing only



---

📡 Contact

Telegram: @MRS13xVoid



Forum: GhostSec / CrackingForum / Private Boards



---

> 🧨 “Exploit the void, automate the hunt.” — MR.S13xVoid
