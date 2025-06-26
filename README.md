# File Integrity Checker

This is a Python-based tool developed as part of an internship project to monitor changes in files by calculating and comparing their SHA-256 hash values. It helps ensure file integrity by detecting any unauthorized modifications, deletions, or changes.

---

##  Objective

To build a tool that:
- Calculates hash values of files (using hashlib)
- Stores those hash values
- Later checks whether any file has been changed or deleted by comparing current hash values with the saved ones

---

## Technologies Used

- **Python 3**
- hashlib – for hashing files
- os – for file and directory access
- json – to store and retrieve hashes

---

##  Features

- Save SHA-256 hash values of all files in a given folder
- Compare saved hash values with current ones to check integrity
- Detect:
  - Unchanged files
  - Modified files
  - Deleted or moved files
- Simple menu-based command-line interface (runs in IDLE too)

---

##  How to Use

1. **Run the script** using Python (in IDLE or terminal)
2. Choose an option from the menu:
   - `1` → Save file hashes
   - `2` → Check file integrity
3. Provide the required folder path or hash file path

---

##  Example Output

``plaintext
 FILE INTEGRITY CHECKER ?

1. Save current file hashes
2. Check file integrity
3. Exit

Enter your choice (1/2/3): 2
Enter path to hash file (hashes.json): C:/Users/Documents/hashes.json
 Checking file integrity...

[OK] File is unchanged: C:/Users/Documents/file1.txt
[CHANGED] File was modified: C:/Users/Documents/report.docx
[MISSING] File deleted or moved: C:/Users/Documents/data.xlsx
