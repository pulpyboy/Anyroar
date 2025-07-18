
<h1 align="center">🧾 VF-6 Old Scanned Entry Downloader</h1>

<p align="center">
<b>This tool lets you download scanned VF-6 Nondh images from the <a href="https://anyror.gujarat.gov.in/">AnyROR Gujarat website</a> using a simple CLI interface.</b><br>
Select your <b>District</b> ➡️ <b>Taluka</b> ➡️ <b>Village</b> and fetch all or selected entries in just a few seconds!
<br><br>
✨ <b>Highlights:</b><br>
⚡️ Parallel downloads for faster performance<br>
📄 All pages of each Nondh are automatically downloaded<br>
🎯 Skips already downloaded entries
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
- ✅ **Skips already downloaded** nondh
- ✅ **Organizes images** in folder format:

  ```
  old-vf6/District/Taluka/Village/nondh_page.jpg
  ```

</details>

---

## <img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Windows_logo_-_2021.svg" alt="Windows 11" width="32" /> Windows Users – Just Run the `.exe`!

No need to install Python or any other dependencies!  
Just **double-click the `.exe` file** and enjoy.

✅ No setup required  
✅ Fully offline  
✅ Same features as Python script  

🔽 [Download EXE File (v1.0)](https://github.com/pulpyboy/Anyror/releases/download/v1.0/anyror_old-vf6_downloader.exe)

---

## 📦 Installation (for Python users)

<details>
  <summary>Click to expand</summary>

```bash
# Clone the repository
git clone https://github.com/pulpyboy/Anyror.git
cd Anyror

# Install required Python packages
pip install -r requirements.txt
```

</details>

---

## 🐍 Usage (Python)

<details>
  <summary>Click to expand</summary>

```bash
python3 anyror_old-vf6_downloader.py
```

🧭 Follow the on-screen prompts:

1. Select **District**  
2. Select **Taluka**  
3. Select **Village**  
4. Enter Nondh numbers:
   - `0` → All available
   - `15-30` → Range
   - `12,17,19` → Specific list

</details>

---

## 📁 Output Folder Structure

<details>
  <summary>Click to expand</summary>

Downloaded image files are stored as:

```
old-vf6/
└── District/
    └── Taluka/
        └── Village/
            ├── 15_1.jpg
            ├── 15_2.jpg
            ├── 16_1.jpg
            └── ...
```

</details>

---

## 🧠 Notes

<details>
  <summary>Click to expand</summary>

- Uses raw JSON from:  
  📄 [GJ_anyror_village_data.json](https://raw.githubusercontent.com/pulpyboy/Anyror/heads/main/GJ_anyror_village_data.json)
- No CAPTCHA or login required
- No modification of server data — 100% read-only

</details>

---

## ✅ License

This project is licensed under the **MIT License**.
