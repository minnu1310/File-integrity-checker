import hashlib
import os
import json

# ---------------------------------------------
# Function to calculate SHA-256 hash of a file
# ---------------------------------------------
def calculate_hash(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):  # Read in chunks for large files
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

# ------------------------------------------------
# Save hashes of all files in a folder (and subfolders)
# ------------------------------------------------
def save_hashes(directory, output_file="hashes.json"):
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = calculate_hash(filepath)
            if file_hash:
                hashes[filepath] = file_hash

    with open(output_file, 'w') as f:
        json.dump(hashes, f, indent=4)
    
    print(f"\n Hashes saved to {output_file}.\n")

# -----------------------------------------------------
# Check if files have changed, been deleted, or added
# -----------------------------------------------------
def check_integrity(hash_file):
    try:
        with open(hash_file, 'r') as f:
            saved_hashes = json.load(f)
    except FileNotFoundError:
        print(" Hash file not found.")
        return

    print("\n Checking file integrity...\n")

    for filepath, old_hash in saved_hashes.items():
        if not os.path.exists(filepath):
            print(f"[MISSING] File deleted or moved: {filepath}")
        else:
            new_hash = calculate_hash(filepath)
            if new_hash != old_hash:
                print(f"[CHANGED] File was modified: {filepath}")
            else:
                print(f"[OK] File is unchanged: {filepath}")

# ------------------------
# Main Menu (CLI-style)
# ------------------------
def main():
    print(" FILE INTEGRITY CHECKER \n")
    print("1. Save current file hashes")
    print("2. Check file integrity")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == '1':
        folder = input("Enter the full folder path to scan: ").strip('" ')
        save_hashes(folder)
    elif choice == '2':
        hash_file = input("Enter path to hash file (hashes.json): ").strip('" ')
        check_integrity(hash_file)
    elif choice == '3':
        print("Exiting. Bye!")
    else:
        print("Invalid choice. Try again.")

# Run the script
if __name__ == "__main__":
    main()
