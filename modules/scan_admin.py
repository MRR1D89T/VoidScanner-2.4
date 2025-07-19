# modules/scan_admin.py

import requests
from core.utils import get_random_user_agent, save_log
from urllib.parse import urljoin

ADMIN_PATHS = [
    "admin", "admin.php", "admin/login", "administrator", "admin123",
    "cpanel", "admin_panel", "adminarea", "admin-login", "admin-console",
    "wp-admin", "wp-login.php", "login.php", "admin.asp", "admin.aspx",
    "admin.html", "login.html", "backend", "adm", "manage", "useradmin",
    "admin1", "admin2", "secureadmin", "adminlogin", "systemadmin",
    "moderator", "dashboard", "root", "auth", "adminarea/login",
    "cmsadmin", "console", "controlpanel", "webadmin", "siteadmin",
    "panel", "admin/home", "admin/home.php", "auth/login", "signin",
    "logon", "portal/admin", "adminuser", "secure", "manage/login",
    "login/admin", "admin/index", "admin/index.php"
]

# Auto-generate dummy variations
for word in ["admin", "login", "panel"]:
    for i in range(1, 101):
        ADMIN_PATHS.append(f"{word}{i}")
        ADMIN_PATHS.append(f"{word}_{i}")
        ADMIN_PATHS.append(f"{word}-{i}")
        ADMIN_PATHS.append(f"{word}{i}.php")

# Remove duplicates
ADMIN_PATHS = list(set(ADMIN_PATHS))


def scan_admin_panels(target_url, timeout=5):
    print(f"\n[🔎] Scanning Admin Panel: {target_url}")
    headers = {'User-Agent': get_random_user_agent()}
    found_admins = []

    for path in ADMIN_PATHS:
        full_url = urljoin(target_url, path)
        try:
            response = requests.get(full_url, headers=headers, timeout=timeout, allow_redirects=True)
            if response.status_code in [200, 401, 403]:
                print(f"[✅] Found: {full_url} ({response.status_code})")
                found_admins.append(full_url)
            else:
                print(f"[❌] {full_url} - {response.status_code}")
        except requests.RequestException:
            print(f"[⚠️] Failed: {full_url}")

    if found_admins:
        save_log("admin_panels", target_url, found_admins)
    else:
        print("[ℹ️] No accessible admin panels found.")
