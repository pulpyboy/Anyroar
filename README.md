🧾 VF-6 Old Scanned Entry Downloader
This project lets you download scanned VF-6 Nondh images from the AnyROR Gujarat website using district, taluka, and village selection.

🚀 Features
✅ Command-line interface for selecting:

District

Taluka

Village

✅ Supports 3 types of Nondh downloads:

All available (0)

Range (e.g. 15-25)

Specific list (e.g. 12,15,17)

✅ Asynchronous check to find maximum Nondh number

✅ Skips already downloaded images

✅ Organizes images in folders:
old-vf6/<District>/<Taluka>/<Village>/nondh_page.jpg

📂 Files in This Repository
File	Description
anyror_old-vf6_downloader.py	Main Python script
GJ_anyror_village_data.json	Village database with DTV codes
requirements.txt	Required Python packages

📦 Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/GJ_anyror_update.git
cd GJ_anyror_update
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🐍 Usage
bash
Copy
Edit
python3 anyror_old-vf6_downloader.py
Follow the on-screen instructions:

Select district, taluka, and village

Enter Nondh numbers:

0 = all available

15-30 = range

12,17,19 = specific list

📁 Output Folder Structure
Images will be saved as:

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
🧠 Notes
Uses raw JSON from:
GJ_anyror_village_data.json

No token or login required

No data is modified on the server — this is read-only scraping

✅ License
This project is open-source under the MIT License.
