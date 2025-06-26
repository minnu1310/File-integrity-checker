import os
import hashlib
import json

def calculate_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def get_all_files(folder):
    file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def save_hashes(folder, output_file="hashes.json"):
    files = get_all_files(folder)
    file_hashes = {}

    print("\nSaving file hashes...\n")
    for file_path in files:
        hash_val = calculate_hash(file_path)
        if hash_val:
            file_hashes[file_path] = hash_val
            print(f"[SAVED]    {os.path.basename(file_path)}")

    with open(output_file, "w") as f:
        json.dump(file_hashes, f, indent=4)

    print(f"\nHashes saved to: {os.path.abspath(output_file)}\n")

def check_integrity(hash_file):
    try:
        with open(hash_file, "r") as f:
            saved_hashes = json.load(f)
    except FileNotFoundError:
        print("Error: Hash file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in hash file.")
        return

    print("\nChecking file integrity...\n")

    for file_path, saved_hash in saved_hashes.items():
        filename = os.path.basename(file_path)
        if not os.path.exists(file_path):
            print(f"[MISSING]  {filename}")
        else:
            current_hash = calculate_hash(file_path)
            if current_hash == saved_hash:
                print(f"[OK]       {filename}")
            else:
                print(f"[CHANGED]  {filename}")

def main():
    print("\nFILE INTEGRITY CHECKER\n")
    print("1. Save current file hashes")
    print("2. Check file integrity")
    print("3. Exit\n")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        folder = input("Enter folder path to scan: ").strip('"')
        save_hashes(folder)
    elif choice == "2":
        hash_file = input("Enter path to hash file (hashes.json): ").strip('"')
        check_integrity(hash_file)
    elif choice == "3":
        print("Exiting.")
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
