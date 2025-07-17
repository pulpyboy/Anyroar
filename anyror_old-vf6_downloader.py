# This file is part of the VF-6 Nondh Downloader project.
# Copyright (C) 2025 Pulpyboy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import json
import requests
import sys
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------------------------
# Village Data JSON URL
# -------------------------
JSON_URL = "https://raw.githubusercontent.com/pulpyboy/Anyror/heads/main/GJ_anyror_village_data.json"
BASE_URL = "https://anyror.gujarat.gov.in/WebHandler/Info6oldImage.ashx?"

# -------------------------
# Download JSON from GitHub
# -------------------------
def load_village_json():
    print("📥 Fetching Data From Server...")
    res = requests.get(JSON_URL)
    res.raise_for_status()
    return res.json()

# -------------------------
# Nondh Existence Checker
# -------------------------
def check_nondh_exists(dtv, eno):
    try:
        r = requests.get(BASE_URL, params={"dtv": dtv, "eno": eno, "pagecnt": 1}, timeout=10)
        return r.status_code == 200 and "image" in r.headers.get("Content-Type", "") and len(r.content) > 1024
    except:
        return False

def async_check_nondhs(dtv, enos):
    results = {}
    def task(eno):
        return eno, check_nondh_exists(dtv, eno)

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(task, eno): eno for eno in enos}
        for future in as_completed(futures):
            eno, result = future.result()
            results[eno] = result
    return results

def find_highest_nondh_async(dtv, step=500, limit=9999):
    print("🚀 Estimating highest Nondh using async scan...")
    test_points = list(range(step, limit + 1, step))
    results = async_check_nondhs(dtv, test_points)
    valid = [eno for eno in test_points if results.get(eno)]
    if not valid:
        return 0
    max_valid = max(valid)
    for eno in range(max_valid + 1, max_valid + step):
        if not check_nondh_exists(dtv, eno):
            return eno - 1
    return max_valid + step - 1

# -------------------------
# Page Downloader
# -------------------------
def download_nondh(dtv, output_dir, eno):
    page = 1
    saved = []
    while True:
        file = os.path.join(output_dir, f"{eno}_{page}.jpg")
        if os.path.exists(file):
            page += 1
            continue
        try:
            r = requests.get(BASE_URL, params={"dtv": dtv, "eno": eno, "pagecnt": page}, timeout=10)
        except Exception as e:
            return f"[!] Error {eno}_{page}: {e}"
        if r.status_code != 200 or "image" not in r.headers.get("Content-Type", "") or len(r.content) < 1024:
            if page == 1 and not saved:
                return f"[×] Nondh {eno} not found"
            return f"[✓] Nondh {eno} - {len(saved)} page(s)"
        with open(file, "wb") as f:
            f.write(r.content)
        saved.append(file)
        page += 1

# -------------------------
# Main Logic
# -------------------------
def run_downloader():
    data = load_village_json()


    # Select District
    districts = sorted(set((r["District Code"], r["District Name"]) for r in data), key=lambda x: x[1])
    print("\n🏙️ Select District:")
    for i, (_, name) in enumerate(districts, 1):
        print(f"{i}. {name}")
    d_code = districts[int(input("Enter choice: ")) - 1][0]

    # Select Taluka
    talukas = sorted(set((r["Taluka Code"], r["Taluka Name"]) for r in data if r["District Code"] == d_code), key=lambda x: x[1])
    print("\n📍 Select Taluka:")
    for i, (_, name) in enumerate(talukas, 1):
        print(f"{i}. {name}")
    t_code = talukas[int(input("Enter choice: ")) - 1][0]


    # Select Village
    villages = sorted([r for r in data if r["District Code"] == d_code and r["Taluka Code"] == t_code], key=lambda x: x["Village Name"])
    print("\n🏘️ Select Village:")
    for i, row in enumerate(villages, 1):
        print(f"{i}. {row['Village Name']}")
    village = villages[int(input("Enter choice: ")) - 1]

    # Confirm Selection
    print("\n📍 Selected Location:")
    print(f"   District: {village['District Name']}")
    print(f"   Taluka : {village['Taluka Name']}")
    print(f"   Village: {village['Village Name']}")
    confirm = input("✅ Is this correct? (y/n): ").strip().lower()
    if confirm != 'y':
        print("\n🔁 Restarting selection...\n")
        os.execv(sys.executable, [sys.executable] + sys.argv)

    dtv_code = village["DTV Code"]

    # Set output path
    out_path = os.path.join("old-vf6", village["District Name"], village["Taluka Name"], village["Village Name"])
    os.makedirs(out_path, exist_ok=True)

    # Ask for Nondh number input
    print("\n📄 Enter Nondh Number Range:")
    print("➤ 0 = All available Nondhs (auto estimate)")
    print("➤ 10-35 = Range")
    print("➤ 5,9,12 = Specific numbers")
    user_input = input("Enter your choice: ").strip()

    if user_input == "0":
        highest = find_highest_nondh_async(dtv_code)
        nondhs = list(range(1, highest + 1))
    elif "-" in user_input:
        try:
            start, end = map(int, user_input.split("-"))
            if start > end:
                raise ValueError
            nondhs = list(range(start, end + 1))
        except:
            print("❌ Invalid range. Use format like 10-35")
            return
    elif "," in user_input:
        try:
            nondhs = sorted(set(int(x) for x in user_input.split(",") if x.strip().isdigit()))
        except:
            print("❌ Invalid list of numbers.")
            return
    else:
        print("❌ Invalid input.")
        return

    skipped = []
    to_download = []
    for eno in nondhs:
        first_page = os.path.join(out_path, f"{eno}_1.jpg")
        if os.path.exists(first_page):
            skipped.append(eno)
        else:
            to_download.append(eno)

    print(f"\n🚀 Ready to download 0/{len(to_download)} Nondhs...\n")

    progress = tqdm(total=len(to_download), unit="nondh", ncols=80)
    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(download_nondh, dtv_code, out_path, eno): eno for eno in to_download}
        for future in as_completed(futures):
            results.append(future.result())
            progress.update(1)
    progress.close()

    print("\n📦 Download Summary:")
    for line in results:
        print(line)
    if skipped:
        print("\n⏩ Skipped (already downloaded):")
        for eno in skipped:
            print(f"[→] Nondh {eno} already downloaded (skipped)")

def show_author_banner():
    print("\n" + "="*50)
    print("🧾 Made with ❤️ by Pulpyboy (2025)")
    print("="*50 + "\n")

def main_loop():
    while True:
        print("\nMade with ❤️ by Pulpyboy (2025)\n")
        try:
            run_downloader()
        except Exception as e:
            print(f"\n⚠️ Error: {e}")
        
        again = input("\n✅ Download complete. Do you want to process another village? (y/n): ").strip().lower()
        if again != 'y':
            print("\n🙏 Thank you for using this tool.")
            break
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main_loop()
