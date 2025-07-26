# plugins/pelari_nuclei.py

import os

def run_nuclei():
    print("🚀 Menjalankan dummy Nuclei Integration...")

    # Coba cari executable nuclei
    nuclei_path = os.system("which nuclei")
    if nuclei_path != 0:
        print("❌ Nuclei tidak ditemukan di PATH. Pastikan sudah diinstal.")
        return

    # Contoh target dummy (sebenarnya kamu bisa masukkan target dari user)
    target = input("🔗 Masukkan target URL untuk scan (misalnya http://example.com): ").strip()

    if not target.startswith("http"):
        print("❌ URL tidak valid.")
        return

    # Contoh command pemanggilan nuclei
    print("📡 Menjalankan Nuclei scan (dummy command)...")
    os.system(f"nuclei -u {target}")

    print("✅ Selesai menjalankan scan dengan Nuclei.")
