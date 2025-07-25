import requests
from core.utils import get_random_user_agent, save_log

# Header kelemahan umum
VULNERABLE_HEADERS = {
    "X-Frame-Options": ["", "ALLOWALL", "ALLOW-FROM"],
    "X-XSS-Protection": ["0"],
    "Strict-Transport-Security": [""],
    "Content-Security-Policy": [""],
    "Access-Control-Allow-Origin": ["*"],
    "X-Content-Type-Options": [""],
    "Server": ["Apache", "Nginx", "Microsoft-IIS"]
}

def analyze_headers(headers):
    findings = []
    for header, values in VULNERABLE_HEADERS.items():
        if header in headers:
            val = headers[header]
            for vuln_val in values:
                if vuln_val.lower() in val.lower():
                    findings.append(f"[⚠️] {header}: '{val}' (Potential Issue)")
        else:
            if header != "Server":
                findings.append(f"[❌] Missing Header: {header}")
    return findings

def scan_headers(target_url):
    print(f"\n[🔍] Scanning HTTP Headers: {target_url}")
    headers = {'User-Agent': get_random_user_agent()}

    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        target_headers = response.headers

        print("\n[📋] Headers Received:")
        for key, value in target_headers.items():
            print(f"  {key}: {value}")

        findings = analyze_headers(target_headers)

        if findings:
            print("\n[🧠] Header Vulnerability Findings:")
            for f in findings:
                print(f"  {f}")
        else:
            print("\n[✅] No obvious header misconfigurations found.")

        save_log("headers", target_url, target_headers)

    except requests.RequestException as e:
        print(f"[❌] Failed to connect to {target_url}")
        print(f"[Error] {e}")

def run():
    print("\n=== Scan Headers ===")
    target_url = input("Enter target URL (e.g. https://example.com): ").strip()
    if not target_url:
        print("Target URL cannot be empty.")
        return
    scan_headers(target_url)
