# 🛡 Task 1 - File Integrity Checker

##  Objective
Build a Python tool to monitor changes in files by calculating and comparing hash values using SHA-256. This ensures file integrity and alerts if any file is modified, deleted, or missing.

---

##  Features

-  Monitors any folder and its files
-  Calculates SHA-256 hash for each file
-  Stores hash values in a JSON file (`hashes.json`)
-  Compares current file hashes with original ones
-  Detects modified, deleted, or safe (unchanged) files
-  Simple command-line/IDLE interface
-  Clean, commented, beginner-friendly code

---

##  Technology Stack

- **Language**: Python 3.13  
- **Hashing**: `hashlib` (SHA-256)  
- **File Handling**: `os`, `json` modules  
- **Platform**: Works in IDLE, terminal, or any Python environment

---

##  How to Run the Project

1. Open the script in **IDLE** or terminal
2. Run `file_integrity_checker.py`
3. Select an option from the menu:
   - Save file hashes
   - Check file integrity

---

##  Example Output

```
 FILE INTEGRITY CHECKER 

1. Save current file hashes
2. Check file integrity
3. Exit

Enter your choice (1/2/3): 2
Enter path to hash file: C:/Users/Minnu/Desktop/hashes.json

 Checking file integrity...

[OK] File is unchanged: notes.txt
[CHANGED] File was modified: report.docx
[MISSING] File deleted or moved: data.xlsx
```

---

##  Notes

- File hashes are calculated using SHA-256.
- `hashes.json` must be kept safe and not edited manually.
- If any file is changed, its hash won’t match the original.
- You must provide the correct path when checking integrity.

---
