<h1 align="center">🧾 VF-6 Old Scanned Entry Downloader</h1>

<p align="center">
  <b>This tool lets you download scanned VF-6 Nondh images from the <a href="https://anyror.gujarat.gov.in/">AnyROR Gujarat website</a> using a simple CLI interface.</b><br>
  Select your District ➡️ Taluka ➡️ Village and fetch all or selected entries in a few seconds!
</p>

---

## 🚀 Features

<details>
  <summary>Click to expand</summary>

- ✅ **Command-line interface** for selecting:
  - District
  - Taluka
  - Village
- ✅ **Supports 3 types of Nondh downloads:**
  - All available (`0`)
  - Range (`e.g. 15-25`)
  - Specific list (`e.g. 12,15,17`)
- ✅ **Asynchronous check** to find the highest Nondh number quickly
- ✅ **Skips already downloaded** image files
- ✅ **Organizes images** in folder format:
  old-vf6/<District>/<Taluka>/<Village>/<nondh_page>.jpg


</details>

---

## 📦 Installation

<details>
<summary>Click to expand</summary>

```bash
# Clone the repository
git clone https://github.com/your-username/GJ_anyror_update.git
cd GJ_anyror_update

# Install required Python packages
pip install -r requirements.txt
</details>

🐍 Usage
<details> <summary>Click to expand</summary>
bash
Copy
Edit
python3 anyror_old-vf6_downloader.py
🧭 Follow the on-screen prompts:

Select District

Select Taluka

Select Village

Enter Nondh numbers:

0 → All available

15-30 → Range

12,17,19 → Specific list

</details>
📁 Output Folder Structure
<details> <summary>Click to expand</summary>
Downloaded image files are stored as:

markdown
Copy
Edit
old-vf6/
└── District/
    └── Taluka/
        └── Village/
            ├── 15_1.jpg
            ├── 15_2.jpg
            ├── 16_1.jpg
            └── ...
</details>
🧠 Notes
<details> <summary>Click to expand</summary>
Uses raw JSON from:
📄 GJ_anyror_village_data.json

No CAPTCHA or login required

No modification of server data — 100% read-only

</details>
✅ License
This project is licensed under the MIT License.
