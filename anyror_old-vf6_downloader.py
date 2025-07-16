import os
import requests
import json

# -------------------------
# Constants
# -------------------------
DATA_URL = "https://raw.githubusercontent.com/pulpyboy/Anyror/refs/heads/main/GJ_anyror_village_data.json"
BASE_URL = "https://anyror.gujarat.gov.in/WebHandler/Info6oldImage.ashx?"

# -------------------------
# Load JSON Data
# -------------------------
print("📥 Fetching district/taluka/village list...")
try:
    response = requests.get(DATA_URL)
    data = response.json()
except Exception as e:
    print(f"❌ Failed to load JSON data: {e}")
    exit(1)

# -------------------------
# Select District
# -------------------------
districts = sorted(set((row["District Code"], row["District Name"]) for row in data), key=lambda x: x[1])
print("\n🏙️ Select District:")
for idx, (_, name) in enumerate(districts, 1):
    print(f"{idx}. {name}")
d_idx = int(input("Enter choice: ")) - 1
d_code, d_name = districts[d_idx]

# -------------------------
# Select Taluka
# -------------------------
talukas = sorted(set((row["Taluka Code"], row["Taluka Name"])
                     for row in data if row["District Code"] == d_code), key=lambda x: x[1])
print("\n📍 Select Taluka:")
for idx, (_, name) in enumerate(talukas, 1):
    print(f"{idx}. {name}")
t_idx = int(input("Enter choice: ")) - 1
t_code, t_name = talukas[t_idx]

# -------------------------
# Select Village
# -------------------------
villages = sorted([row for row in data if row["District Code"] == d_code and row["Taluka Code"] == t_code],
                  key=lambda x: x["Village Name"])
print("\n🏘️ Select Village:")
for idx, row in enumerate(villages, 1):
    print(f"{idx}. {row['Village Name']}")
v_idx = int(input("Enter choice: ")) - 1
village = villages[v_idx]
v_name = village["Village Name"]
dtv_code = village["DTV Code"]  # Use DTV Code field from JSON

# -------------------------
# Ask Nondh No Range
# -------------------------
print("\n📄 Enter Nondh Number Range from-to (e.g. 10-15), 0 for all, or comma-separated (e.g. 12,15,18):")
user_input = input("Enter your choice: ").strip()

nondh_numbers = []

if user_input == "0":
    nondh_numbers = list(range(1, 10000))  # All from 1 to 9999
elif "-" in user_input:
    try:
        start_nondh, end_nondh = map(int, user_input.split("-"))
        if start_nondh > end_nondh:
            raise ValueError
        nondh_numbers = list(range(start_nondh, end_nondh + 1))
    except ValueError:
        print("❌ Invalid input. Use format like 5-25 or enter 0.")
        exit(1)
elif "," in user_input:
    try:
        nondh_numbers = [int(num.strip()) for num in user_input.split(",")]
    except ValueError:
        print("❌ Invalid list. Please enter numbers separated by commas.")
        exit(1)
else:
    print("❌ Invalid input.")
    exit(1)

# -------------------------
# Set Output Folder
# -------------------------
base_path = os.path.join(os.getcwd(), "old-vf6", d_name, t_name, v_name)
os.makedirs(base_path, exist_ok=True)

# -------------------------
# Download Images
# -------------------------
for nondh_no in nondh_numbers:
    first_page_file = os.path.join(base_path, f"{nondh_no}_1.jpg")
    if os.path.exists(first_page_file):
        print(f"[→] Nondh No. {nondh_no} already downloaded. Skipping.")
        continue

    page_no = 1
    found_any_page = False

    while True:
        params = {
            "dtv": dtv_code,
            "eno": nondh_no,
            "pagecnt": page_no
        }

        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
        except Exception as e:
            print(f"[!] Network error for Nondh No. {nondh_no}, Page {page_no}: {e}")
            break

        content_type = response.headers.get("Content-Type", "")
        if response.status_code != 200 or "image" not in content_type or len(response.content) < 1024:
            if page_no == 1 and not found_any_page:
                print(f"[×] Nondh No. {nondh_no} not found.")
            else:
                print(f"[-] Finished Nondh No. {nondh_no}, total {page_no - 1} pages.")
            break

        # Save the image
        filename = os.path.join(base_path, f"{nondh_no}_{page_no}.jpg")
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"[✓] Saved: {filename}")
        found_any_page = True
        page_no += 1
